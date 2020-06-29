import http.client
import time

def request_enum(met, url, bod, hea):
    # HTTP Request
    conn.request(method, url, body, headers)
    print(url)

    time.sleep(1)

    # HTTP Response
    res = conn.getresponse()

    # Version Check
    version = res.version
    if version == 11:
        version = 'HTTP/1.1'
    elif version == 10:
        version = 'HTTP/1.0'
    else:
        version = 'unknown'

    # st_line = version + ' ' + str(res.status) + ' ' + res.reason
    st_line = version + ' ' + str(res.getheader('Content-Length'))
    return st_line


# HTTP Request 설정
method = 'GET'
# method = 'POST'
url = '/'
domain = 'my.skidc.net'
body = None
# body = 'body_value'
headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
           'Accept-Language': 'ko-KR',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'my.skidc.net',
            'Connection': 'close',
            'Cookie': 'JSESSIONID=AFD1B73AEF6E5F231F22FBB65464B660.jvm2; eventCheck2=done'}

conn = http.client.HTTPSConnection(domain)

stub = ('', '.bak', '.back', '.backup', '.org', '.old',
        '.zip', '.log', '.sql', '.new', '.txt', '.tmp', '.temp')

wf = open("result.txt", "w")
with open("url.txt", "r") as f:
    while True:
        line = f.readline()
        if not line: break

        line = line[:-1]
        
        for plus in stub:
            line1 = line + plus
            result = request_enum(method, line1, body, headers)
            result1 = "{0:60}, {1}".format(line1, result)
            # print("{0:50}, {1}".format(line1, result))
            print(result1)
            result1 = result1 + '\n'
            wf.write(result1)

wf.close()