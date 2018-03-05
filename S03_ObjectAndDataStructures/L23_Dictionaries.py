myDict = {'key1':'value1','key2':'value2'}

print(myDict)
print(myDict['key1'])

pricesLookup = {'apple':2.99, 'orange':1.99, 'milk':5.80}

print(pricesLookup['apple'])

#dictionaries are flexible with types
d = {'k1':123, 'k2':[0,1,2], 'k3':{'insideKey':100}}

print(d['k2'])
print(d['k3']['insideKey'])

d = {'key1':['a', 'b', 'c']}

print(d)

print(d['key1'][2].upper())

#assigning new keys
d = {'k1':100, 'k2':200}
d['k3'] = 300
print(d)

d['k1'] = 'NEW VALUE'
print(d)

d = {'k1':100, 'k2':200}

print(d.keys())
print(d.values())
print(d.items())
