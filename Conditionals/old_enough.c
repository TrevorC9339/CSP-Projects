#include <stdio.h>
int age;

int main(void){
    printf("how old are you?");
    scanf("%d", &age);
if (age >= 18){
        printf("you can vote\n");
}else if (age >=16){
        printf("you can get your drivers license\n");
}else  if (age >=15){
        printf("you can get a learners permit\n");
}else if (age >=5){
        printf("you can start school\n");
}else  printf("go drink some milk baby");
return 0;
}