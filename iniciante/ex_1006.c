#include <stdio.h>
int main() {
    double a, b, c, MEDIA;

    MEDIA = 0;

    scanf("%lf %lf %lf", &a, &b, &c);

    a = a * 2;
    b = b * 3;
    c = c * 5;
    MEDIA = (a + b + c) / 10;
    
    printf("MEDIA = %.1lf\n", MEDIA);
    return 0;
}