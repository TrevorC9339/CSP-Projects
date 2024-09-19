#include <stdio.h>
#include <string.h>
int main(void){
       char name[15];
       printf("What is your name?");
       scanf("%s", &name);
       char prefix[4] = "<<<";
       char profix[4] = ">>>";
        strcat(name, profix);
       strcat(prefix, name);
       printf("%s\n", prefix);


char parent1[4] = "(((";
char parent2[4] = ")))";
        strcat(name, parent2);
        strcat(parent1, name);
        printf("%s\n", parent1);

       char prefix2[] = "---";
       char profix2[] = "---";
        strcat(name, profix2);
       strcat(prefix2, name);
       printf("%s\n", prefix2);


       char prefix3[] = " :):):)";
       char profix3[] = ":):):)";
        strcat(name, profix3);
       strcat(prefix3, name);
       printf("%s\n", prefix3);


       char prefix4[] = "###";
       char profix4[] = "###";
        strcat(name, profix4);
       strcat(prefix4, name);
       printf("%s\n", prefix4);
 
       char prefix5[] = "+++";
       char profix5[] = "+++";
        strcat(name, profix5);
       strcat(prefix5, name);
       printf("%s\n", prefix5);

       char prefix6[] = "~~~";
       char profix6[] = "~~~";
        strcat(name, profix6);
       strcat(prefix6, name);
       printf("%s\n", prefix6);


       char prefix7[] = "===";
       char profix7[] = "===";
        strcat(name, profix7);
       strcat(prefix7, name);
       printf("%s\n", prefix7);
return 0;
}