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

'''
Watch for changes in all .py files. If changes, run nosetests. 
'''
def checkSumRecurse():
    val = 0
    for dirpath, dirs, files in os.walk('.'):
        for file in [file for file in files if file[-3:] == '.py']:
            absoluteFileName = os.path.join( dirpath, file)
            stats = os.stat(absoluteFileName)
            val += stats [stat.ST_SIZE] + stats [stat.ST_MTIME]
    return val 

def main():
    val=0
    if len(sys.argv) > 1:
        command = " ".join(sys.argv[1:])
    else:
        command = "nosetests"

    while (True):
        if checkSumRecurse() != val:
            val=checkSumRecurse()
            os.system('reset')
            ret = os.system(command)
            if ret != 0:
                notify("Broken build", "Your command of %s returned exit code %s. Please verify the console output for more info." % (command, ret))
        time.sleep(1)

def notify(title, message):
    try:
        import pynotify
    except:
        return

    if pynotify.init("Nosy"):
        n = pynotify.Notification(title, message)
        n.show()

if __name__ == '__main__':
    sys.exit(main())


