# -*- coding: utf-8 -*-
# author: itimor

import sys
from subprocess import check_output

def _execute(cmd):
    '''
    execute cmd
    '''
    result = {}
    try:
        stdout = check_output(cmd)
        stderr = ''
    except:
        stdout = ''
        stderr = str(sys.exc_info())
    result['stdout'] = stdout
    result['stderr'] = stderr
    return result

def execute(request):
    if request.method == 'POST' and request.is_ajax():
        cmd = ['ping','-c','10','www.baidu.com']
        cmd_exec = _execute(cmd)
        stdout = cmd_exec['stdout']
        stderr = cmd_exec['stderr']
        print stdout
        try:
            stdout = str(stdout)
            stdout = stdout.splitlines()
        except:
            e = sys.exc_info()[0]
            print "error" + str(e)
