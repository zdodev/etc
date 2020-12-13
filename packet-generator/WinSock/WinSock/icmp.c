#include <stdio.h>
#include <stdlib.h>
#include <WS2tcpip.h>
#include <WinSock2.h>
#include <netiodef.h>

USHORT checksum(USHORT* ptr, int nbytes)
{
	int sum;
	USHORT oddbyte;
	USHORT answer;

	sum = 0;
	while (nbytes > 1) {
		sum += *ptr++;
		nbytes -= 2;
	}

	if (nbytes == 1) {
		oddbyte = 0;
		*((UCHAR*)&oddbyte) = *(UCHAR*)ptr;
		sum += oddbyte;
	}

	sum = (sum >> 16) + (sum & 0xffff);
	sum += (sum >> 16);
	answer = ~sum;

	return (answer);
}

int main(int argc, char* argv[]) {
	WSADATA wsaData;
	SOCKET hSocket;
	SOCKADDR_IN serverAddr;
	char buf[sizeof(ICMP_MESSAGE) + 32] = { 0 };
	ICMP_MESSAGE* icmp = (ICMP_MESSAGE*)buf;

	icmp->Header.Type = 8;
	icmp->Header.Code = 0;
	icmp->Header.Checksum = 0;
	icmp->Data.Data16[0] = GetCurrentProcessId();
	icmp->Data.Data16[1] = 1;

	icmp->Header.Checksum = checksum((USHORT*)icmp, sizeof(ICMP_MESSAGE) + 32);

	if (argc != 2) {
		printf("Usage : %s <IP>\n", argv[0]);
		exit(EXIT_FAILURE);
	}

	if (WSAStartup(MAKEWORD(2, 2), &wsaData))
		printf("WSAStartup() Error...\n");

	hSocket = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP);
	if (hSocket == INVALID_SOCKET)
		printf("socket() Error...\n");
	serverAddr.sin_family = AF_INET;
	InetPtonA(AF_INET, (PCSTR)argv[1], &serverAddr.sin_addr);
	serverAddr.sin_port = htons(0);

	while (TRUE) {
		sendto(hSocket, buf, sizeof(ICMP_MESSAGE) + 32, 0, (SOCKADDR*)&serverAddr, sizeof(serverAddr));
		Sleep(1000);
	}

	closesocket(hSocket);
	WSACleanup();
	return 0;
}
