#include <stdio.h>
int main() {
    double a, b, MEDIA;

    MEDIA = 0;

    scanf("%lf %lf", &a, &b);

    a = a * 3.5;
    b = b * 7.5;
    MEDIA = (a + b) / 11;
    
    printf("MEDIA = %.5lf\n", MEDIA);
    return 0;
}