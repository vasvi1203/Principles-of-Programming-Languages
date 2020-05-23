#include<unistd.h>

void virus() {
	char *s[2];
	s[0] = "/bin/sh";
	s[1] = NULL;
	execve(s[0], s, NULL);	
}

void smash() {
	int a[2] = {5, 8};
	a[2] = 6;
	a[3] = 0x00005555; 
	a[4] = 0x55555139;
}

int main() {
	smash();
	return 0;
}
