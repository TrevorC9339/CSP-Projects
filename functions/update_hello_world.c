#include <stdio.h>
#include <string.h>
char name;
char john[5] = "john";
char sam[5] = "sam";
char joe[5] = "joe";
char ty[5] = "Ty";
char dan[5] = "Dan";

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