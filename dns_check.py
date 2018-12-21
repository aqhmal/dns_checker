#!/usr/bin/env python
import sys
import dns.resolver

# Show error if user doesn't insert domain
if len(sys.argv) <= 1:
    print('Please insert your domain')
    # Exit the program
    exit()

# Get user input
domain = sys.argv[1]

print('DNS Records for :', domain)

# Common DNS Record Type
types = ['A', 'AAAA', 'CNAME', 'MX', 'TXT', 'NS']

# Do loop for all dns record types
for type in types:
    try:
        # Query DNS Record
        records = dns.resolver.query(domain, type)
        # Only show record if there are record
        if len(records) > 0:
            print('\n' + type, 'Record :-')
            # Loop and print records
            for key, value in enumerate(records):
                print(key + 1, '=>', value)
    except:
        # Error handler
        # print('\nUnable to retrieve', type, 'records')
        pass
