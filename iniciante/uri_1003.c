#include <stdio.h>

int main(void) {
	int a, b, SOMA;

	SOMA = 0;

	scanf("%d\n", &a);
	scanf("%d\n", &b);

	SOMA = a + b;
    
	printf("SOMA = %d\n", SOMA);
	return 0;
}