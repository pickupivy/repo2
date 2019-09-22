
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int g_var=6;	// external variable in data section
char bufword[]="a write to stdout.\n";	

int main(void)
{
	pid_t pid;
	int l_var;

	l_var=88;
	if(write(STDOUT_FILENO, bufword, sizeof(bufword)-1) != sizeof(bufword)-1)
		printf("write error");
	printf("before fork\n");

	if((pid = fork()) < 0) {
		printf("fork error.\n");
	} else if(pid > 0) {	// parent
		printf("this is parent.\n");
		sleep(2);
	} else {
		printf("child!\n");
		g_var++;
		l_var++;
	}

	printf("pid=%ld, glob=%d, loc=%d\n", (long)getpid(), g_var, l_var);
	
	exit(0);
}