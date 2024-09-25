#include <stdio.h>
 
 float income, rent, transport, utilities, grocieries, expenses, savings, total;

float input(char type[], float var){
    printf("How much is your %s: \n", type);
    scanf("%f", &var);
    return var;
}

void percent(char type[], int amount){
   int per = amount/income*100;
    printf("your %s  is  %d%% of your income.\n" , type, per);
    
}

int main(void){
    printf("This is going to calculate your budget for the month\n");
    input("income", income);
    input("rent", rent);
    input("utilities", utilities);
    input("grocieries", grocieries);
    input("transport", transport);
    expenses = income-(rent + utilities + transport + grocieries);
    savings = income *.2;
    total = income + expenses;
    percent("rent", rent);
    percent("expenses", expenses);
    percent("savings", savings);
    percent("transport", transport);
    percent("utlilities", utilities);
    printf("Hello World!");
    return 0;
 }
    
