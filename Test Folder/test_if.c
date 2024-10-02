#include <stdio.h>
int grade;
int main(void){
    printf("what is yout grade percent?\n");
    scanf("%d", &grade);
if (grade >= 90){
    printf("You have an A\n");
}else if (grade >= 80){
    printf("You have a B\n");
}else if (grade >= 70){
    printf("You have a C\n");
}else if (grade >= 60){
    printf("You have a D\n");
}else printf("You have an F\n");
    return 0;
}