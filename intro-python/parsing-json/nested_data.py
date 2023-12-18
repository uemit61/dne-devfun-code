#!/usr/bin/env python
"""Working with nested data hands-on exercise / coding challenge.

Copyright (c) 2018-2021 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import json
import os


# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname("interfaces.json"))


with open(os.path.join(here, "interfaces.json")) as file:
    file_contents = file.read()
    file_data = json.loads(file_contents)


for interface in file_data['ietf-interfaces:interfaces']['interface']:
    print(interface['name'])
    for addr in interface['ietf-ip:ipv4']['address']:
        print(addr['ip'])
        print(addr['netmask'])

        
