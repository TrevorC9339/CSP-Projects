#include <stdio.h>
#include <string.h>
#include <time.h>
int i, usr;
char one[50], two[50], three[50];

void delay(int sec){
    int mili = 1000*sec;
    clock_t start = clock();
    while (clock()< start+mili);
}
int main(void){
printf("How high do you want the number?\n");
scanf("%d", &usr);
printf("give me a word\n");
scanf("%s", one);
printf("Give me another word\n");
scanf("%s", two);
strcat(three, two);
strcat(one, three);
    
    for(i=1; i<=usr; i++){
        if(i%3 == 0 && i%5 == 0)
            printf("%s\n", three);
        else if(i%3==0)
            printf("%s\n", one);
        else if(i%5==0)
            printf("%s\n", two);
        else
            printf("%d\n", i);
            delay(500);
    }
    return 0;
}