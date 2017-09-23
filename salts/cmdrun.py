# -*- coding: utf-8 -*-
# author: itimor

import sys
import subprocess

def run(cmd):
    try:
        results = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stderr = ''
    except:
        results = ''
        stderr = str(sys.exc_info()[1])
    if len(stderr):
        return stderr
    else:
        return results.stdout