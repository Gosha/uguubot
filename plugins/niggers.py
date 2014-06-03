import re

from util import hook
@hook.regex(r'(id/[^\s]*)')
def niggers(inp):
    "Automatically convert id/x to a nigge.rs URL"
    return "http://nigge.rs/" + inp.group(1)
