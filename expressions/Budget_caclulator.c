#include <stdio.h>

int main(void){
    float prent, putilities, ptransport, pexpenses, pgrocieries;
    float income, rent, transport, utilities, grocieries, expenses, savings, total;
    printf("This is going to calculate your budget for the month\n");
    printf("How much do you make a month?\n");
    scanf("%f", &income);
    printf("How much do you pay for rent?\n");
    scanf("%f", &rent);
    printf("How much do your utilities cost?\n");
    scanf("%f", &utilities);
    printf("How much do you spend on grocieries?\n");
    scanf("%f", &grocieries);
    printf("How much do you spend on trasport?\n");
    scanf("%f", &transport);
    expenses = rent + utilities + transport + grocieries;
    savings = income *.2;
    total = income + expenses;
    prent = (rent/income);
    putilities = (utilities/income;)
    ptransport = (transport/income;)
    pgrocieries = (grocieries/income);
    pexpenses = (expenses/income);
    printf("your income is:  $%.2f\n" , income);
    printf("your expenses is:  $%.2f\n" , expenses);
    printf("your savings is:  $%.2f\n" , total);
    printf("your rent is:  $%.2f\n" , prent);
    printf("Hello World!");
    return 0;
 }
    
