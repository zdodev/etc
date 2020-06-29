print('')

import dns.resolver
with open('domain.txt', "r") as f:
    for url in f:
        url = url[:-1]
        result = dns.resolver.query(url)
        print(result.rrset)
