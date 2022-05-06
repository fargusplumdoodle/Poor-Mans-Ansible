#!python3

import sys
import subprocess

FUNCTIONS_SCRIPT="run.sh"
arg = sys.argv[0]

def get_command(fn: str) -> str:
    return ['bash', '-c', f'. {FUNCTIONS_SCRIPT}; {fn}']

def run_command(fn: str) -> subprocess.CompletedProcess:
    return subprocess.run(get_command(fn), capture_output=True)




print(run_command('success'))
print(run_command('fail'))


