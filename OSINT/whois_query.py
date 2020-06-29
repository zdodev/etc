from ipwhois import IPWhois

print('')

with open('domain.txt', "r") as f:
    for ip in f:
        ip = ip[:-1]
        obj = IPWhois(ip)
        results = obj.lookup_rdap()
        print(ip, results['asn_description'])

'''
for keys in results.keys():
    print(keys)
    '''
'''
print('')

import dns.resolver
with open('domain.txt', "r") as f:
    for url in f:
        url = url[:-1]
        result = dns.resolver.query(url)
        print(result.rrset)
'''
#