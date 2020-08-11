#include <stdio.h>
int main() {
    int func, h;
    float vh;

    scanf("%d %d %f", &func, &h, &vh);
    printf("NUMBER = %d\n", func);
    printf("SALARY = U$ %.2f\n", (h * vh));
    
    return 0;
}