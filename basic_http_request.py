import http.client

# HTTP Request 설정
method = 'GET'
# method = 'POST'
url = '/'
body = None
# body = 'body_value'
headers = {'header_line' : 'value'}
conn = http.client.HTTPConnection('my.skidc.net')
# HTTP Request
conn.request(method, url, body, headers)

# HTTP Responsea
res = conn.getresponse()

# Version Check
version = res.version
if version == 11:
    version = 'HTTP/1.1'
elif version == 10:
    version = 'HTTP/1.0'
else:
    version = 'unknown'

st_line = version + ' ' + str(res.status) + ' ' + res.reason
print(st_line)
print(res.msg, end='')
# print(res.read().decode('utf-8'))
print(res.read().decode('euc-kr'))
#eessddd
