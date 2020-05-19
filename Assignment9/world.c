//Write two threads, one which displays Hello World and the other which displays Goodbye World.

#include<pthread.h>
#include<stdio.h>
#include<unistd.h>

pthread_mutex_t lock;

void *hello(void *arg) {
	pthread_mutex_lock(&lock);
	printf("Hello World\n");
	pthread_mutex_unlock(&lock);
	return NULL;
}

void *goodbye(void *arg) {
	pthread_mutex_lock(&lock);
	printf("Goodbye World\n");
	pthread_mutex_unlock(&lock);
	return NULL;
}

int main() {
	pthread_t thread_id1, thread_id2;
	while(1) {
		pthread_create(&thread_id1, NULL, hello, NULL);
		sleep(1);
		pthread_create(&thread_id2, NULL, goodbye, NULL);
		sleep(1);
		pthread_join(thread_id1, NULL);
		pthread_join(thread_id2, NULL);
	}
	return 0;
}
