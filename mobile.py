import subprocess
import time
# drozer 실행
# subprocess.run(['drozer', 'console', '-c' 'run app.package.list', 'connect'], shell=True)

# init variable
app_name = 'com.shinhan.sbanking'

print('1. App Storage Download')
print('2. App Heap Memory Dump')
print('Choice: ', end='')
choice = int(input())

# Switch Case
def switchCase(num):
    return {1: appStorageDownload,
            2: appHeapMemoryDump}[num]

# 앱 Local Storage 다운로드
def appStorageDownload(app_name):
    print('app storage download start')
    app_path = '/data/data/'
    subprocess.run(['adb', 'shell', 'su', '-c', 'chmod -R 755 ' + app_path + app_name])
    subprocess.run(['adb', 'pull', app_path + app_name])
    print('app storage download end.')

# 앱 힙 메모리 덤프 및 다운로드
def appHeapMemoryDump(app_name):
    print('app heap memory dump start')
    app_path = '/data/local/tmp/'
    ext = '.memdump'
    subprocess.run(['adb', 'shell', 'touch ' + app_path + app_name + ext])
    subprocess.run(['adb', 'shell', 'am dumpheap ' + app_name + ' ' + app_path + app_name + ext])
    time.sleep(3) # 메모리 덤프 시간 대기
    subprocess.run(['adb', 'pull', app_path + app_name + ext])
    subprocess.run(['adb', 'shell', 'rm -rf ' + app_path + app_name + ext])
    print('app heap memory dump end')

func = switchCase(choice)
func(app_name)
