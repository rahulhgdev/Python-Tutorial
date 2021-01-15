laptop = {}
laptop['aspire_7'] = {
    'cpu' : 'i5-9300h',
    'gpu' : 'gtx 1650 4gb ddr5',
    'ram' : '8gb',
    'refresh rate' : '60hz',
    'weight': '2.2kg',
    'wifi ' : 6
}
laptop['nitro_5'] = {
    'cpu' : 'r5-3500h',
    'gpu' : 'gtx 1650 4gb ddr5',
    'ram' : '8gb',
    'refresh rate' : '120hz',
    'weight': '2.5kg',
    'wifi ' : 5
}

import json
s = json.dumps(laptop)              # convert dictionary to JSON format i.e is exchangeable
print(s)

# to store json in a file

with open("E:\\Python\Beginner_Level\\working with json\\file.txt",'w') as f:
    f.write(s)