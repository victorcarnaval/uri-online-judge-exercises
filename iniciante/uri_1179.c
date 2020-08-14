#include <stdio.h>
int main()
{
    int par[5], impar[5], cont = 0, num, contP = 0, contI = 0, k;
    while (cont < 15)
    {
        scanf("%d", &num);
        if (num % 2 == 0)
        {
            par[contP] = num;
            contP++;
        }
        else
        {
            impar[contI] = num;
            contI++;
        }
        if (contP == 5)
        {
            k = 0;
            while (k < 5)
            {
                printf("par[%d] = %d\n", k, par[k]);
                k++;
            }
            k = 0;
            while (k < 5)
            {
                par[k] = 0;
                k++;
            }
            contP = 0;

        }
        if (contI == 5)
        {
            k = 0;
            while (k < 5)
            {
                printf("impar[%d] = %d\n", k, impar[k]);
                k++;
            }
            k = 0;
            while (k < 5)
            {
                impar[k] = 0;
                k++;
            }
            contI = 0;

        }

        cont++;
        }
        k = 0;
        while (k < contI)
        {
            printf("impar[%d] = %d\n", k, impar[k]);
            k++;
        }
        k = 0;
        while (k < contP)
        {
            printf("par[%d] = %d\n", k, par[k]);
            k++;
        }
    return 0;
}