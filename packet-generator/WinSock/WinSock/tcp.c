#include <stdio.h>
#include <stdlib.h>
#include <WS2tcpip.h>
#include <WinSock2.h>
#include <netiodef.h>

int main(int argc, char* argv[]) {
	WSADATA wsaData;
	SOCKET hSocket;
	SOCKADDR_IN serverAddr;
	char buf[100];
	char ipHeader[sizeof(IPV4_HEADER)];
	IPV4_HEADER* ipHeaderInit = (IPV4_HEADER*)ipHeader;
	IPV4_HEADER* ipHeaderInit = (IPV4_HEADER*)buf;
	char tcpHeader[sizeof(TCP_HDR)];
	TCP_HDR* tcpHeaderInit = (TCP_HDR*)tcpHeader;
	TCP_HDR* tcpHeaderInit = (TCP_HDR*)&buf[sizeof(IPV4_HEADER)];
	int optval = 1;

	ipHeaderInit->Version = 4;
	ipHeaderInit->HeaderLength = 5;
	ipHeaderInit->TypeOfService = 0;
	ipHeaderInit->EcnField = 0;
	ipHeaderInit->TotalLength = htons(sizeof(IPV4_HEADER) + sizeof(TCP_HDR));
	ipHeaderInit->Identification = htons(2);
	ipHeaderInit->Reserved = 0;
	ipHeaderInit->DontFragment = 1;
	ipHeaderInit->MoreFragments = 0;
	ipHeaderInit->DontUse1;
	ipHeaderInit->DontUse2;
	ipHeaderInit->TimeToLive = 128;
	ipHeaderInit->Protocol = IPPROTO_TCP;
	ipHeaderInit->HeaderChecksum = 0;
	ipHeaderInit->SourceAddress.S_un.S_addr = inet_addr("172.16.143.128");
	ipHeaderInit->DestinationAddress.S_un.S_addr = inet_addr("192.168.35.25");

	tcpHeaderInit->th_sport = htons(12345);
	tcpHeaderInit->th_dport = htons(80);
	tcpHeaderInit->th_seq;
	tcpHeaderInit->th_ack;
	tcpHeaderInit->th_x2;
	tcpHeaderInit->th_len;
	tcpHeaderInit->th_flags;
	tcpHeaderInit->th_win;
	tcpHeaderInit->th_sum = 0;
	tcpHeaderInit->th_urp;

	if (argc != 2) {
		printf("Usage : %s <IP>\n", argv[0]);
		exit(EXIT_FAILURE);
	}

	if (WSAStartup(MAKEWORD(2, 2), &wsaData))
		printf("WSAStartup() Error...\n");

	hSocket = socket(AF_INET, SOCK_RAW, IPPROTO_RAW);
	if (hSocket == INVALID_SOCKET)
		printf("socket() Error...\n");
	printf("%d\n", WSAGetLastError());

	serverAddr.sin_family = AF_INET;
	InetPtonA(AF_INET, (PCSTR)argv[1], &serverAddr.sin_addr);
	serverAddr.sin_port = htons(0);

	if (setsockopt(hSocket, IPPROTO_IP, IP_HDRINCL, (char*)&optval, sizeof(optval)))
		printf("setsockopt() Error...\n");

	sendto(hSocket, buf, 40, 0, (SOCKADDR*)&serverAddr, sizeof(serverAddr));

	int a = 0;
	while (TRUE) {
		a = sendto(hSocket, tcpHeader, sizeof(tcpHeader), 0, (SOCKADDR*)&serverAddr, sizeof(serverAddr));
		printf("%d\n", a);
		Sleep(1000);
	}

	char buffer[10000];
	int nDataLength;
	while ((nDataLength = recv(hSocket, buffer, 10000, 0)) > 0) {
		int i = 0;
		while (buffer[i] >= 32 || buffer[i] == '\n' || buffer[i] == '\r') {
			printf("%c", buffer[i]);
			i += 1;
		}
	}

	closesocket(hSocket);
	WSACleanup();
	return 0;
}