#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "tool.h"

int root();
int user();
int rootr(char );
int userr();

char o[10] = "root", t[10] = "toor";   
char e[10] = "window", r[10] = "windows";
//先这样简单粗暴地解决一下账户密码验证的问题就好wwwww

//C++ bate版，算法参考python版
int main()
{
	char kef[10], usef[10];

	printf("Ocean |版本 1.0.0\n");
	printf("©2013-2019  RED \n");
	printf("  \n");
	printf("户名:");
	scanf_s("%s",&usef);

	if (strcmp(usef,o)==0)
	{
		printf("密码:");
		scanf_s("%s",&kef);
		if (strcmp(kef,t)==0)
		{
			root();			
		}
		else
		{
			printf("对不起，您输入的密码有误\n");
			printf("  \n");
		}
	}
	if (strcmp(usef, e) == 0)
	{

		printf("密码:");
		scanf_s("%s", &kef);
		if (strcmp(kef, r) == 0)
		{
			user();
		}
		else
		{
			printf("对不起，您输入的密码有误\n");
			printf("  \n");
		}
	}
	else
	{
		printf("不存在的账户，请检查后重试");
		printf("   \n");
	}
	return 0;
}

int root()
{
	printf("Ocean [版本 1.0.0 bate] \n");
	printf("(c) 2020 Dream_Programmer \n");
	printf(" \n");
	char raw_input[20];
	char tool[10] = "tool", ip[10] = "ip";
	scanf_s("-->%s", &raw_input);
	return ;

}


int user()
{
	printf("Ocean [版本 1.0.0 bate] \n");
	printf("(c) 2020 Dream_Programmer \n");
	printf(" \n");
	char raw_input[20];
	char tool[10] = "tool", ip[10] = "ip";
	scanf_s("-->%s", &raw_input);
}

int rootr()
{

}