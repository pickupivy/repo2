
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

//char *p_stable, *p_move;

int inverse(char *str1)
{
	int length = 0;
	char *p1 = NULL;
	char *p2 = NULL;
	if (str1 == NULL)
	{
		return -1;
	}
	length  = strlen(str1);
	p1 = str1;                 //指针指向字符串的开头;
	p2 = str1 + (length - 1);  //指针指向字符串的最后一个;
	while (p1 < p2)
	{
		char c = *p1;
		*p1 = *p2;
		*p2 = c;
		++p1;
		--p2;
	}
	return 0;
}

void inverse_stack(char *str1)
{
	if (str1 == NULL)  //递归结束的异常条件
	{
		return;
	}
	if (*str1 == '\0')  //递归结束的正常条件
	{
		return;
	}

	inverse_stack(str1 + 1);
	printf("%c", *str1);
}

int Add(int x, int y)
{
	int z = 0;
	z = x + y;
	return z;
}

int main(void)
{
/*
	int a = 20;
	int b = 10;
	int ret = Add(a, b);
	printf("ret=%d\n", ret);
	return 0;
*/
	//p_stable=p_move;
	char buf[] = "abcg1234";   //buf[] 会在栈上对全局区的字符串拷贝。
	
	//inverse_stack(buf);
	inverse(buf);
	printf("%s", buf);
	
	printf("\n");
	return 0;
	
}

