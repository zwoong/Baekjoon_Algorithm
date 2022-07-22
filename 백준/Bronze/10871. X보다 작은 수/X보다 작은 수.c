#include <stdio.h>

int main(){
	int n, min, input;
	scanf("%d %d", &n, &min);

  for(int i=0; i<n; i++){
    scanf("%d", &input);

    if(min>input){
      printf("%d ", input);
    }
      
  }
  
	return 0;
}