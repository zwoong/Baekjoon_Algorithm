#include <stdio.h>

int main(){
	  int n,init, count = 0;
    scanf("%d", &n);
    init = n;
    int a, b, d;
    do {
        a = n/10;
        b = n%10;
        d = (a+b)%10; // 더한 값에 오른쪽 값
        n = b*10 + d; // 이전 값에 오른쪽 값
      
        count++;
    }while(n != init);
      printf("%d", count);
    return 0;
}