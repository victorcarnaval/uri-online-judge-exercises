#include <stdio.h>

int main()
{
   char nome[10];
   double salarioFixo,vendas, salarioTotal;
   scanf("%s", &nome);
   scanf("%lf", &salarioFixo);
   scanf("%lf", &vendas);

   salarioTotal = salarioFixo + (vendas * 0.15);

   printf("TOTAL = R$ %.2lf\n", salarioTotal);

   return 0;
}