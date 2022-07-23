#include <stdio.h>

int main(void) {
    
    int a,b,c, sum=0, input=0;
    int num[10]={};

    scanf("%d %d %d", &a, &b, &c);
    sum = a*b*c;

    for(int i=0; sum > 0; i++) { // 각 숫자가 몇 번 쓰였는지 구하기
        input = sum % 10;
        num[input] += 1;
        sum /= 10;
    }
    
    for(int i=0; i<10; i++) printf("%d\n", num[i]);
}