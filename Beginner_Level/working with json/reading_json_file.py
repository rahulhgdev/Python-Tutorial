Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> f=open("E:\\Python\\Beginner_Level\\working with json\\file.txt",'r')
>>> s=f.read()
>>> s
'{"aspire_7": {"cpu": "i5-9300h", "gpu": "gtx 1650 4gb ddr5", "ram": "8gb", "refresh rate": "60hz", "weight": "2.2kg", "wifi ": 6}, "nitro_5": {"cpu": "r5-3500h", "gpu": "gtx 1650 4gb ddr5", "ram": "8gb", "refresh rate": "120hz", "weight": "2.5kg", "wifi ": 5}}'
>>> # convert from json to dictionary
>>> import json
>>> laptop = json.loads(s)
>>> laptop
{'aspire_7': {'cpu': 'i5-9300h', 'gpu': 'gtx 1650 4gb ddr5', 'ram': '8gb', 'refresh rate': '60hz', 'weight': '2.2kg', 'wifi ': 6}, 'nitro_5': {'cpu': 'r5-3500h', 'gpu': 'gtx 1650 4gb ddr5', 'ram': '8gb', 'refresh rate': '120hz', 'weight': '2.5kg', 'wifi ': 5}}
>>> # difference above 2 output is 1st one is json/string and 2nd one is dictionary
>>> type(laptop)
<class 'dict'>
>>> type(s)
<class 'str'>
>>> laptop['aspire_7']['gpu']
'gtx 1650 4gb ddr5'
>>> laptop['nitro_5']['']
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    laptop['nitro_5']['']
KeyError: ''
>>> # to print weight of laptop in laptop dictionary
>>> for weight in laptop:
	print(laptop['weight'])

	
Traceback (most recent call last):
  File "<pyshell#15>", line 2, in <module>
    print(laptop['weight'])
KeyError: 'weight'
>>> for weight in laptop:
	print(laptop[weight])

	
{'cpu': 'i5-9300h', 'gpu': 'gtx 1650 4gb ddr5', 'ram': '8gb', 'refresh rate': '60hz', 'weight': '2.2kg', 'wifi ': 6}
{'cpu': 'r5-3500h', 'gpu': 'gtx 1650 4gb ddr5', 'ram': '8gb', 'refresh rate': '120hz', 'weight': '2.5kg', 'wifi ': 5}
>>> 