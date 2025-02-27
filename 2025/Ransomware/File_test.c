#define _CRT_SECURE_NO_WARNINGS

#include <Windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 파일 경로를 입력받아 내용물과 확장자를 바꾸는 함수
void change_FileName(const char* filePath)
{
	FILE* fp;
	int result;

	// Encrypted File에 들어갈 것들 -> 나중에 RSA_test와 합칠 때 참고
	BYTE CIPHER[] = { 0x00, };
	BYTE EncryptedKEYIV = { 0x00, };
	DWORD CIPHERSize = 0;
	DWORD EncryptedKEYIVSize = 0;

	fp = fopen(filePath, "wb");

	if (fp == NULL) {
		printf("No such file...\n");
		return;
	}
	else {
		// Write File
		fwrite(CIPHER, sizeof(BYTE), CIPHERSize, fp);
		//fwrite(EncryptedKEYIV, sizeof(BYTE), EncryptedKEYIVSize, fp);

		// Change File extension
		char newFilePath[100];
		strcpy(newFilePath, filePath);
		char* ext = strrchr(newFilePath, '.');
		if (ext != NULL) {
			*ext = '\0';
		}
		strcat(newFilePath, ".cry");

		result = fclose(fp);
		if (result != 0) {
			printf("File was not closed!\n");
			return;
		}
		else {
			printf("File was closed\n");
		}

		if (rename(filePath, newFilePath) != 0) {
			printf("Failed to change file name\n");
		}
		else {
			printf("File renamed successfully!\n");
		}
	}
}

// 파일 경로나 이름을 입력받아 원본 파일을 지우는 함수
void delete_FileName(const char* fileName)
{
	int res = remove(fileName);
	if (res == 0) {
		printf("deleted file successfully!\n");
	}
	else {
		printf("Failed to delete file!\n");
	}
}

int main()
{
	// 다른 디렉터리의 파일을 개방하고자 하면 파일의 경로를 모두 적어야 함
	// 절대 경로인 경우 parameter는 const char* 타입이 됨

	change_FileName("sample_text.txt");
	delete_FileName("sample_text2.txt");
	// 전부 구현 완료 -> 합치는 일만 남음

	return 0;
}
