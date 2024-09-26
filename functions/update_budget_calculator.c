#include <stdio.h>
#include<math.h>

float income, rent, transport, utilities, grocieries, expenses, savings, total;

float input(char type[], float var){
    printf("How much is your %s: \n", type);
    scanf("%f", &var);
    return var;
}

void percent(char type[], int amount){
   int per = amount/income*100;
   printf("%d\n", per);
    printf("your %s  is  %d%% of your income.\n" ,type,  per);
    
}

int main(void){
    printf("This is going to calculate your budget for the month\n");
    income = input("income", income);
    rent = input("rent", rent);
    utilities = input("utilities", utilities);
    grocieries = input("grocieries", grocieries);
    transport = input("transport", transport);
    expenses =  + transport + grocieries;
    savings = income * .2;
    total = income - expenses;

    printf("Your rent is %f\n", rent);
    printf("Your savings is %f \n", savings);
    printf("Your income is %f\n", income);
    printf("Your total expenses is %f\n", expenses);

    percent("rent", rent);
    percent("expenses", expenses);
    percent("savings", savings);
    percent("transport", transport);
    percent("utlilities", utilities);
    return 0;
 }
    
