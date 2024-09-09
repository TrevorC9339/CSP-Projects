#include <stdio.h>

int main(void){
    printf("Hello World!");
    
    char name[20];
    printf("What is your name?");
    scanf("%s", name);
    printf("Hello %s", name);
        
    return 0;
}
