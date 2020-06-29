#include <stdio.h>
#include <tchar.h>
#include <Windows.h>

int _tmain(int argc, TCHAR* argv[]) {
	LPTSTR str1 = _T("MBCS or WBCS 1");
	TCHAR str2[] = _T("MBCS or WBCS 2");
	TCHAR str3[100];
	TCHAR str4[50];

	LPCTSTR pStr = str1;

	_tprintf(_T("string size: %d \n"), sizeof(str2));
	_tprintf(_T("string length: %d \n"), sizeof(pStr));

	_fputts(_T("Input String 1 : "), stdout);
	_tscanf(_T("%s"), str3);
	_fputts(_T("Input String 2 : "), stdout);
	_tscanf(_T("%s"), str4);

	_tcscat(str3, str4);
	_tprintf(_T("String1 + String2 : %s\n"), str3);

	_tprintf(_T("%p\n"), pStr);

	return 0;
}