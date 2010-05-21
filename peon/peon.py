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
import glob,os,stat,time
from os.path import abspath, dirname, join

class Urgency(object):
    low = 0
    normal = 1
    critical = 2

def _get_checksum_from_dir(dirpath, pattern):
    result = 0
    for file in glob.glob(os.path.join(dirpath, pattern)):
        absoluteFileName = os.path.join(dirpath, file)
        stats = os.stat(absoluteFileName)
        result += stats[stat.ST_SIZE] + stats[stat.ST_MTIME]
    return result

'''
Watch for changes in all .py files. If changes, run nosetests. 
'''
def checkSumRecursive(directory, pattern='*.py'):
    result = 0
    for dirpath, dirs, files in os.walk(directory):
        result += _get_checksum_from_dir(dirpath, pattern)
    return result

def main():
    val = 0
    command = " ".join(sys.argv[1:]) or 'nosetests'
    is_build_broken = False

    try:
        while (True):
            if checkSumRecursive('.') != val:
                val = checkSumRecursive('.')
                os.system('reset')
                status = os.system(command)
                if status != 0:
                    is_build_broken = True
                    notify("Broken build", "Your command of '%s' returned exit code '%s'. Please verify the console output for more info." % (command, ret), "stop.png", urgency=Urgency.critical)
                else:
                    if is_build_broken:
                        is_build_broken = False
                        notify("Build fixed", "Your build with command of '%s' IS FIXED!" % (command), "tick.png")

            time.sleep(1)
    except KeyboardInterrupt:
        return

def notify(title, message, image, urgency=Urgency.normal):
    try:
        import pynotify
    except:
        return

    urgencies = {
        Urgency.low:pynotify.URGENCY_LOW,
        Urgency.normal:pynotify.URGENCY_NORMAL,
        Urgency.critical:pynotify.URGENCY_CRITICAL,
    }

    if pynotify.init("Nosy"):
        n = pynotify.Notification(title, message, abspath(join(dirname(__file__), image)))
        n.set_urgency(urgencies[urgency])
        n.show()
        time.sleep(2)
        n.close()

if __name__ == '__main__':
    sys.exit(main())


