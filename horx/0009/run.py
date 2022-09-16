#!/usr/bin/env python3

import re
import requests

r = requests.get('https://github.com')
matches = re.findall('(?:https?|ftp)://[^\s/$\.?#].[^\s]+', r.text)

for i in range(len(matches)):
    print(f'matche >>>: {matches[i]} \n')
