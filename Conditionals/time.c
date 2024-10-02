#include <stdio.h>
#include <time.h>
int hour;
int main(void){
    time_t now;
    struct tm*now_tm;
    now = time(NULL);
    now_tm = localtime(&now);
    hour = now_tm->tm_hour;
    printf("%d\n", hour);

    if ((hour-6) <= 12){
        printf("good morning\n");
    }else if ((hour-6) <= 18){
        printf("good afternoon\n");
    }else if (hour-6) <= 22){
        printf("good evening");
    }else printf("good evening\n");

    return 0;
}