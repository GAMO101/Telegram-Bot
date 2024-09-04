import json

import re

with open('data.json') as f:

    data = json.load(f)



#print(data[0]['data'][15])

pattern = r'"Datum":"\d{2}\.\d{2}\.\d{4}"'

match = re.match(pattern, data)

print(match)