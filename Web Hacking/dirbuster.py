import http.client
import time
# # #
def request_http(conn, method, url, body, headers):
    conn.request(method, url, body, headers)
    return conn.getresponse()

# HTTP Request 설정
host = "zk.iptime.org"
conn = http.client.HTTPConnection(host)
method = 'GET'
# method = 'POST'
url = '/'
body = None
# body = 'body_value'
headers = {'Host' : 'bizring.skbroadband.com',
           'Upgrade-Insecure-Requests' : 1,
           'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36',
           'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Referer' : 'http://bizring.skbroadband.com/view/intro/intro.do',
           'Accept-Encoding' : 'gzip, deflate',
           'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
           'Cookie' : 'JSESSIONID=E94510CA205104479FEBE72A22580303; _ga=GA1.2.278996465.1528690732; _gid=GA1.2.1046804771.1528690732; _gat=1',
           'Connection' : 'close'
           }

# HTTP Response
dir_file = open('dir_result.txt', 'w')
with open('foo.txt', 'r') as f:
    for url in f:
        url = url.replace('.do', '')
        url = url.replace('\n', '')
        res = request_http(conn, method, url, body, headers)
        time.sleep(1)

        version = res.version
        if version == 11:
            version = 'HTTP/1.1'
        elif version == 10:
            version = 'HTTP/1.0'
        else:
            version = 'unknown'

        st_line = version + ' ' + str(res.status) + ' ' + res.reason
        result_txt = '{0:40}'.format(url) + ' ' + st_line
        print(result_txt)
        dir_file.write(result_txt + '\n')
        dir_file.flush()
dir_file.close()
#print(res.msg, end='')
#print(res.read().decode('utf-8')) 