#include <stdio.h>
int main() {
    int n, cont;

    cont = 0;

    scanf("%d", &n);
    printf("%d\n", n);

    while (n != 0) {
        while (n >= 100) {
            cont++;
            n = n - 100;
        }
        printf("%d nota(s) de R$ 100,00\n", cont);
        cont = 0;

        while (n >= 50) {
            cont++;
            n = n - 50;
        }
        printf("%d nota(s) de R$ 50,00\n", cont);
        cont = 0;

        while (n >= 20) {
            cont++;
            n = n - 20;
        }
        printf("%d nota(s) de R$ 20,00\n", cont);
        cont = 0;

        while (n >= 10) {
            cont++;
            n = n - 10;
        }
        printf("%d nota(s) de R$ 10,00\n", cont);
        cont = 0;

        while (n >= 5) {
            cont++;
            n = n - 5;
        }
        printf("%d nota(s) de R$ 5,00\n", cont);
        cont = 0;

        while (n >= 2) {
            cont++;
            n = n - 2;
        }
        printf("%d nota(s) de R$ 2,00\n", cont);
        cont = 0;

        while (n >= 1) {
            cont++;
            n = n - 1;
        }
        printf("%d nota(s) de R$ 1,00\n", cont);
        cont = 0;
    }
    return 0;
}