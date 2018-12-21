#!/usr/bin/env python
import sys
import dns.resolver

if len(sys.argv) <= 1:
    print('Please insert your domain')
    exit()

domain = sys.argv[1]

print('DNS Records for :', domain)

# Common DNS Record Type
types = ['A', 'AAAA', 'CNAME', 'MX', 'TXT', 'NS']

for type in types:
    try:
        records = dns.resolver.query(domain, type)
        # Only show record if there are record
        if len(records) > 0:
            print('\n' + type, 'Record :-')
            for key, value in enumerate(records):
                print(key + 1, '=>', value)
    except:
        # print('\nUnable to retrieve', type, 'records')
        pass
