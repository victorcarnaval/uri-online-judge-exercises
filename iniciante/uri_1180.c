#include <stdio.h>

int main()
{
    int n, x[1000], menor , posicao, i;
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        scanf("%d", &x[i]);
        if (x[i] < menor)
        {
            menor = x[i];
            posicao = i;
        }
    }
    printf("Menor valor: %d\n", menor);
    printf("Posicao: %d\n", posicao);

return 0;
}