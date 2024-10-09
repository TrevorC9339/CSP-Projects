#include <stdio.h>
char siblings[3][20] = {"Jenna", "Zac", "Gage"};
int i;
int main(void){
    for(i=0; i < 3; i++){
        printf("%s Christensen\n", siblings[i]);
    }

    return 0;

}