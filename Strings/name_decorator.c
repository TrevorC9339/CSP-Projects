#include <stdio.h>
#include <string.h>
int main(void){
       char name[] = "Trevor";  
       char prefix[] = "<<<";
       char profix[] = ">>>";
        strcat(name, profix);
       strcat(prefix, name);
       printf("%s\n", prefix);

char name1[] = "Trevor";
char parent1[] = "(((";
char parent2[] = ")))";
        strcat(name1, parent2);
        strcat(parent1, name1);
        printf("%s\n", parent1);

        char name2[] = "Trevor";  
       char prefix2[] = "---";
       char profix2[] = "---";
        strcat(name2, profix2);
       strcat(prefix2, name2);
       printf("%s\n", prefix2);

           char name3[] = "Trevor";  
       char prefix3[] = " :):):)";
       char profix3[] = ":):):)";
        strcat(name3, profix3);
       strcat(prefix3, name3);
       printf("%s\n", prefix3);

        char name4[] = "Trevor";  
       char prefix4[] = "###";
       char profix4[] = "###";
        strcat(name4, profix4);
       strcat(prefix4, name4);
       printf("%s\n", prefix4);

        char name5[] = "Trevor";  
       char prefix5[] = "+++";
       char profix5[] = "+++";
        strcat(name5, profix5);
       strcat(prefix5, name5);
       printf("%s\n", prefix5);

        char name6[] = "Trevor";  
       char prefix6[] = "~~~";
       char profix6[] = "~~~";
        strcat(name6, profix6);
       strcat(prefix6, name6);
       printf("%s\n", prefix6);

        char name7[] = "Trevor";  
       char prefix7[] = "===";
       char profix7[] = "===";
        strcat(name7, profix7);
       strcat(prefix7, name7);
       printf("%s\n", prefix7);
return 0;
}