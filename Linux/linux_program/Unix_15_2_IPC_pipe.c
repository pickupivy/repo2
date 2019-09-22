
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main(void)
{
	pid_t pid;
	int fd[2];
	int n;
	char line[20];

	if(pipe(fd) < 0) 
		printf("pipe error.\n");
	printf("fd0=%d, fd1=%d", fd[0], fd[1]);

	if((pid = fork()) < 0) {
		printf("fork error.\n");
	} else if(pid > 0) {	// parent
		printf("this is parent.\n");	
		close(fd[0]);
		write(fd[1], "hello to child~\n", 16);
		sleep(3);
	} else {
		printf("child!\n");
		//write(1, "child~\n", 20);
		close(fd[1]);
		n=read(fd[0], line, 16);
		
		//write(STDOUT_FILENO, line, n);
		//write(0, line, n);
		write(1, line, n);
		//write(2, line, n);
	}
	exit(0);
}