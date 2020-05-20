//Write a program to implement clock with 3 threads, one for hours, second for minutes and third for seconds counter. If required use semaphores or mutex if clock is treated as critical section.

#include<pthread.h>
#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<time.h>

pthread_t tid[3];
pthread_mutex_t lock;


void *func(void *arg) {
	pthread_mutex_lock(&lock);
	time_t now;
	time(&now);
	struct tm *local = localtime(&now);
	int h = local->tm_hour, m = local->tm_min, s = local->tm_sec;
	
	int *id = (int *)arg;
	if(*id == 0) {
		while(s < 60) {
			sleep(1);
			system("clear");	//system("cls"); for windows
			printf("%02d:%02d:%02d\n", h, m, s);
			s++;
		}
	}
	
	else if(*id == 1) {
		m += 1;
	}
	
	else if(*id == 2) {
		if(m >= 60) {
			m = 0;
			h += 1;
		}
		if(h >= 24) {
			h = 0;
			m = 0;
			s = 0;
		}
	}
	
	pthread_mutex_unlock(&lock);
	
	return NULL;
}
		

int main() {
	int i;
	while(1) {
		for(i = 0; i < 3; i++) {		
			pthread_create(&(tid[i]), NULL, func, (void *)&i);
			pthread_join(tid[i], NULL);
		}
		//pthread_mutex_destroy(&lock);
	}
	return 0;
}
