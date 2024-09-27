#include <stdio.h>
#include <string.h>
char name;

void namer(char name[]){
  printf("Hello %s!\n", name);


}

int main(void){
    printf("Hello World!\n");
    
  namer("john");
  namer("dan");
  namer("sam");
  namer("joe");
  namer("ty");
     








    return 0;
}