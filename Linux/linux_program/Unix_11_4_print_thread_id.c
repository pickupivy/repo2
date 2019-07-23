
#include "apue.h"
#include <pthread.h>

typedef unsigned long u32;

pthread_t g_tid;

void printids(const char *s)
{
    pid_t pid;
    pthread_t tid;
    pid=getpid();
    tid=pthread_self();
    printf("%s: pid %lu tid %lu (0x%lx)\n", s, (u32)pid, (u32)tid, (u32)tid);
}

void* thr_fn(void* arg)
{
    printids("New thread");
    //return ((void*)0);
    return 0;
}

int main(void)
{
    int err;
    err=pthread_create(&g_tid, NULL, thr_fn, NULL);
	printf("g_tid=%lu\n", (u32)g_tid);
    if(err != 0) {
		printf("can't creat thread");
		exit(1);
	}
    printids("Main thread");
    sleep(1);
    exit(0);
}
