#include <Windows.h>
#include <bcrypt.h>
#include <stdio.h>
#include <stdlib.h>

#pragma comment(lib, "bcrypt.lib")

#define NT_SUCCESS(Status)	(((NTSTATUS)(Status)) >= 0)
#define STATUS_UNSUCCESSFUL	((NTSTATUS)0xC0000001L)

void Decrypt() {
	NTSTATUS status = 0;
	BYTE Cipher[] = {
		0xE7, 0x1B, 0xA0, 0x08, 
		0x97, 0x36, 0x17, 0xD7, 
		0xE7, 0xDB, 0x34, 0xDC, 
		0x2A, 0xEB, 0x1E, 0x0E,
		0x53, 0x4B, 0x56, 0x75, 
		0xB6, 0x83, 0xC2, 0xC6, 
		0xF7, 0xDA, 0xFB, 0x2E, 
		0x4F, 0x32, 0x38, 0xD9
	};
	BYTE* Plain = NULL;

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
	DWORD PlainLength = 0;
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
	if (!NT_SUCCESS(status)) { 
		printf("Failed to Generate Key Object: %x\n", status);
		return; 
	};

	// Calculate Plaintext Length
	status = BCryptDecrypt(
		KEY_HANDLE,
		Cipher,
		sizeof(Cipher),
		NULL,
		IV,
		IVLength,
		NULL,
		0,
		&PlainLength,
		BCRYPT_BLOCK_PADDING);
	if (!NT_SUCCESS(status)) {
		printf("Failed to Calculate Plaintext Length: %x\n", status);
		return;
	}

	// Operate Decryption
	Plain = (PBYTE)calloc(PlainLength, sizeof(BYTE));
	if (Plain == NULL) return;
	status = BCryptDecrypt(
		KEY_HANDLE,
		Cipher,
		sizeof(Cipher),
		NULL,
		IV,
		IVLength,
		Plain,
		PlainLength,
		&bufferSize,
		BCRYPT_BLOCK_PADDING);
	if (!NT_SUCCESS(status)) {
		printf("Failed to Decrypt ciphertext: %x\n", status);
		return;
	}

	// Print Plaintext
	printf("Plaintext: %s\n", Plain);

	// Destroy Key and Close Algorithm Provider
	BCryptDestroyKey(KEY_HANDLE);
	BCryptCloseAlgorithmProvider(algHandle, 0);
	free(Plain);

	return;
}

int main() {
	Decrypt();

	return 0;
}
