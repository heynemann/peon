#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Original By Jeff Winkler, http://jeffwinkler.net
# Got the code at http://jeffwinkler.net/2006/04/27/keeping-your-nose-green/

# Copyright Bernardo Heynemann <heynemann@gmail.com>

# Licensed under the Open Software License ("OSL") v. 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.opensource.org/licenses/osl-3.0.php

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import glob
import os
import stat
import time
import optparse
from os.path import abspath, dirname, join


_checksum = 0
_pattern = None


class Urgency(object):
    low = 0
    normal = 1
    critical = 2


def _get_stats_from_filename(filename):
    stats = os.stat(filename)
    return stats[stat.ST_SIZE] + stats[stat.ST_MTIME]


def _get_checksum_from_dir(dirpath, pattern):
    result = 0
    for file in glob.glob(os.path.join(dirpath, pattern)):
        absolute_filename = os.path.abspath(file)
        result += _get_stats_from_filename(absolute_filename)
    return result


def checksum_recursively(directory, pattern):
    result = 0
    for dirpath, dirs, files in os.walk(directory):
        result += _get_checksum_from_dir(dirpath, pattern)
    return result


def something_has_changed(dir, pattern):
    global _checksum
    global _pattern
    if _pattern != pattern:
        _pattern = pattern
        _checksum = checksum_recursively(dir, _pattern)
    new_checksum = checksum_recursively(dir, _pattern)
    if new_checksum != _checksum:
        _checksum = new_checksum
        return True
    return False

    
def clear_screen():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('reset')


def main():
    '''
    Watch for changes in files that match the pattern in a directory.
    Default dir is '.' and default pattern is '*.py'.
    Whenever a change to any matched file in directory happens, peon runs
    the command specified or nosetests by default
    '''
    parser = optparse.OptionParser()
    parser.add_option('-d', '--dir', default='.', dest='directory',
                      help='the directory peon will watch for changes')
    parser.add_option('-p', '--pattern', default='*.py', dest='pattern',
                      help='the glob pattern to watch for changes. '\
                            '(default is "*.py)"')
    parser.add_option('--no-reset', default=True, dest='reset', action="store_false", 
                      help='do not clear the screen between runs. '\
                            '(default is True)')
    options, args = parser.parse_args()
    directory = options.directory
    pattern = options.pattern
    reset = options.reset
    command = ' '.join(args) or 'nosetests'
    is_build_broken = False

    try:
        while True:
            if something_has_changed(directory, pattern):
                if reset:
                    clear_screen()
                status = os.system(command)
                if status != 0:
                    is_build_broken = True
                    notify("Broken build",
                            "Your command of '%s' returned exit"\
                            "code '%s'. Please verify the console output for"\
                            "more info." % (command, status),
                            "stop.png",
                            urgency=Urgency.critical)
                elif is_build_broken:
                    is_build_broken = False
                    notify("Build fixed",
                           "Your build with command '%s' IS FIXED!" % command,
                           "tick.png")

            time.sleep(1)
    except KeyboardInterrupt:
        return


def notify(title, message, image, urgency=Urgency.normal):
    try:
        import pynotify
    except:
        return

    urgencies = {
        Urgency.low: pynotify.URGENCY_LOW,
        Urgency.normal: pynotify.URGENCY_NORMAL,
        Urgency.critical: pynotify.URGENCY_CRITICAL,
    }

    if pynotify.init("Nosy"):
        n = pynotify.Notification(title,
                                  message,
                                  abspath(join(dirname(__file__), image)))
        n.set_urgency(urgencies[urgency])
        n.show()
        time.sleep(2)
        n.close()

if __name__ == '__main__':
    sys.exit(main())
