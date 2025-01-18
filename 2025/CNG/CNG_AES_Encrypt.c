#include <Windows.h>
#include <bcrypt.h>
#include <stdio.h>
#include <stdlib.h>

#pragma comment(lib, "bcrypt.lib")

#define NT_SUCCESS(Status)	(((NTSTATUS)(Status)) >= 0)
#define STATUS_UNSUCCESSFUL	((NTSTATUS)0xC0000001L)

void Encrypt() 
{
	NTSTATUS status;
	BYTE Plain[] = {
		'F', 'a', 'S', ' ', 
		'2', '0', '2', '5',
		' ', 'N', 'i', 'c', 
		'e', ' ', 'H', 'a', 
		'p', 'p', 'y', ' ', 
		'G','o', 'o', 'd', '~', '\0' };
	BYTE* Cipher = NULL;

	// AES algorithm setting value
	BCRYPT_ALG_HANDLE algHandle = BCRYPT_AES_CBC_ALG_HANDLE;
	BCRYPT_KEY_HANDLE KEY_HANDLE = NULL;
	BYTE IV[16] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
	BYTE Key[16] = {
		0x20, 0x19, 0x22, 0x43,
		0x20, 0x25, 0x01, 0x14,
		0xFF, 0xFF, 0x10, 0x11,
		0x12, 0x13, 0x14, 0x15 };
	DWORD IVLength = 16;
	DWORD BlockLength = 16;
	DWORD CipherLength = 0;
	DWORD bufferSize = 0;

	// Generate Key Object
	status = BCryptGenerateSymmetricKey(
		algHandle,
		&KEY_HANDLE,
		NULL,
		0,
		Key,
		sizeof(Key),
		0);
	if (!NT_SUCCESS(status)) { printf("Failed to Generate Key Object: %x\n", status); return; };

	// Calculate Ciphertext Length
	status = BCryptEncrypt(
		KEY_HANDLE,
		Plain,
		sizeof(Plain),
		NULL,
		IV,
		IVLength,
		NULL,
		0,
		&CipherLength,
		BCRYPT_BLOCK_PADDING);
	if (!NT_SUCCESS(status)) {
		printf("Failed to Calculate Ciphertext Length: %x\n", status);
		return;
	}

	// Operate Encryption
	Cipher = (PBYTE)calloc(CipherLength, sizeof(BYTE));
	if (Cipher == NULL) return;
	status = BCryptEncrypt(
		KEY_HANDLE,
		Plain,
		sizeof(Plain),
		NULL,
		IV,
		IVLength,
		Cipher,
		CipherLength,
		&bufferSize,
		BCRYPT_BLOCK_PADDING);
	if (!NT_SUCCESS(status)) {
		printf("Failed to Encrypt plaintext: %x\n", status);
		return;
	}

	// Print Ciphetext
	// 중간에 꼬였던 점: Cipher 배열을 어디까지 출력해야 할지에 대해 상수로 for문을 돌렸다가 꼬임
	printf("Ciphertext: ");
	for (int cnt_i = 0; cnt_i < CipherLength; cnt_i++) { printf("%02X ", Cipher[cnt_i]); } 

	// Destroy Key and Close Algorithm Provider
	BCryptDestroyKey(KEY_HANDLE);
	BCryptCloseAlgorithmProvider(algHandle, 0);
	free(Cipher);

	return;
}

int main() 
{
	Encrypt();

	return 0;
}
