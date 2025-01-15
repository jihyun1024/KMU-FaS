#include <Windows.h>
#include <bcrypt.h>
#include <stdio.h>
#include <stdlib.h>

#pragma comment(lib, "bcrypt.lib")

#define NT_SUCCESS(Status)	(((NTSTATUS)(Status)) >= 0)
#define STATUS_UNSUCCESSFUL	((NTSTATUS)0xC0000001L)

void test() {
	NTSTATUS status;
	BCRYPT_ALG_HANDLE algHandle = NULL;

	// Open Algorithm Provider
	status = BCryptOpenAlgorithmProvider(
		&algHandle,
		BCRYPT_RNG_ALGORITHM,
		NULL,
		0);
	if (!NT_SUCCESS(status)) return;

	// Generate Random Number
	BYTE random[48] = { 0, };
	status = BCryptGenRandom(
		algHandle,
		random,
		48,
		BCRYPT_RNG_USE_ENTROPY_IN_BUFFER);
	if (!NT_SUCCESS(status)) return;

	// Close Algorithm Provider
	status = BCryptCloseAlgorithmProvider(
		algHandle,
		0);
	if (!NT_SUCCESS(status)) return;

	// for debug
	printf("Random 48 bytes: ");
	for (int cnt_i = 0; cnt_i < 48; cnt_i++) {
		printf("%02X ", random[cnt_i]);
	}
}

int main() {
	test();
	return 0;
}
