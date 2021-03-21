#include <stdio.h>
int max4(int a, int b, int c, int d)
{
    int max = a;
    if(b > max) max = b;
    if(c > max) max = c;
    if(d > max) max = d;
    return max;
}

int min4(int a, int b, int c, int d)
{
    int min = a;
    if(b < min) min = b;
    if(c < min) min = c;
    if(d < min) min = d;
    return min;
}

int main()
{
    int a, b, c, d;
    printf("max4(%d,%d,%d,%d)=%d\n", scanf("%d", & a), scanf("%d", & b), scanf("%d", & c), scanf("%d", & d), max4(a,b,c,d));
    printf("min(%d,%d,%d,%d)=%d\n", a, b, c, d, min4(a, b, c, d));
    return 0;
}