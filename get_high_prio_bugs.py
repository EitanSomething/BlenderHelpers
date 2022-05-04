#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import urllib.request
import re
from datetime import date

modules = {
    "Animation & Rigging" : "https://developer.blender.org/maniphest/query/2P2UxkYF35n6/#R",
    "Core" : "https://developer.blender.org/maniphest/query/ZUhbQbYsFhS0/#R",
    "Grease Pencil" : "https://developer.blender.org/maniphest/query/3aBqTtUGGL6S/#R",
    "Modeling" : "https://developer.blender.org/maniphest/query/1yhH.uryM5Jd/#R",
    "Nodes & Physics" : "https://developer.blender.org/maniphest/query/U0sxIFNLA8wR/#R",
    "Pipeline, Assets & I/O" : "https://developer.blender.org/maniphest/query/qlpBH9sXDwgu/#R",
    "Platforms, Builds, Test & Devices" : "https://developer.blender.org/maniphest/query/HwtwBTQAkUVl/#R",
    "Python API" : "https://developer.blender.org/maniphest/query/.LXrMzP9eb8T/#R",
    "Render & Cycles" : "https://developer.blender.org/maniphest/query/TMa3_XQRcvFL/#R",
    "EEVEE & Viewport" : "https://developer.blender.org/maniphest/query/Ir0LS4F3sUT6/#R",
    "Sculpt, Paint & Texture" : "https://developer.blender.org/maniphest/query/bkxbTQs_g0oU/#R",
    "User Interface" : "https://developer.blender.org/maniphest/query/QAiqNkWtQQT1/#R",
    "VFX & Video" : "https://developer.blender.org/maniphest/query/OIkVntw4V74i/#R",
    "Total" : "https://developer.blender.org/maniphest/query/hsOX9Fm3BmXk/#R"
}


def get_source(url):
    source = urllib.request.urlopen(url)
    source_bytes = source.read()
    source.close()

    return source_bytes.decode("utf8")


def get_number_of_bugs(source):  
    high = re.search('<span class="phui-header-header">High (.+?)</span>', source)
    unbreak_now = re.search('<span class="phui-header-header">Unbreak Now! (.+?)</span>', source)

    if (high and unbreak_now):
        high = int(high.group(1).strip("()"))
        unbreak_now = int(unbreak_now.group(1).strip("()"))

        return (high+unbreak_now)
    elif (high or unbreak_now):
        if high:
            return int(high.group(1).strip("()"))
        else:
            return int(unbreak_now.group(1).strip("()"))
    else:
        return 0


# Get number of all bugs from modules and assemble a summary for the chat
report = "Open High Priority bugs as of %s:\n\n" % date.today()

for module in modules:
    bugs = get_number_of_bugs(get_source(modules[module]))
    if module == "Total":
        report+= "\n"
    report += ("[%s](%s): %s\n" % (module, modules[module], bugs))

file = open('bugs_report.txt', 'w')
file.write(report)
file.close()
