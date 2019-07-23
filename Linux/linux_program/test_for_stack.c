#include<stdio.h>

int Add(int x, int y)
{
	int z = 0;
	z = x + y;
	return z;
}
int main()
{
	int a = 20;
	int b = 10;
	int ret = Add(a, b);
	printf("ret=%d\n", ret);
	return 0;
}

