#include <stdio.h>

int sumof(int a, int b)
{
    int sum = 0;
    while (a != b)
    {
        if(a > b){
            sum += a;
            a--;
        }
        else{
            sum += a;
            a++; 
        }
    }
    sum += a;
    return sum;
    
}

int main(void)
{
    int i, n;
    int sum;
    printf("n을 입력하세요.\n");
    scanf("%d", & n);

    sum = 0;

    for(i = 1; i <= n; i++){
        sum += i;
        if(i < n)
            printf("%d + ", i);
        else
            printf("%d = %d\n", i, sum);
    }

    printf("가우스의 덧셈식으로 계산결과 : %d\n", (1+n)*n/2);

    int a, b;
    printf("a, b를 입력하세요.\n"); scanf("%d", & a); scanf("%d", & b);
    printf("%d와 %d사이의 합은 %d입니다.\n", a, b, sumof(a, b));


    return 0;
}