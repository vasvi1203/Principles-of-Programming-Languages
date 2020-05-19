//Write a program with thread which displays a Hello after every second.

#include<pthread.h>
#include<stdio.h>
#include<unistd.h>

void *hello(void *arg) {
	while(1) {
		printf("Hello\n");
		sleep(1);
	}
	return NULL;
}

int main() {
	pthread_t thread_id;
	pthread_create(&thread_id, NULL, hello, NULL);
	pthread_join(thread_id, NULL);
	return 0;
}
