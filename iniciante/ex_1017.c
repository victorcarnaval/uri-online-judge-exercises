#include <stdio.h>
int main() {
    int tempo, velocidade, distancia;
    float litros = 12.0;

    scanf("%d", &tempo);
    scanf("%d", &velocidade);

    distancia = tempo * velocidade;
    litros = distancia / litros;

    printf("%.3f\n", litros);
    
    return 0;
}