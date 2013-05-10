from util import hook
import subprocess

@hook.command
def perl(inp):
    ".perl -e <code>"
    return subprocess.Popen(["perl", inp], stderr=subprocess.STDOUT, stdout=subprocess.PIPE).communicate()
