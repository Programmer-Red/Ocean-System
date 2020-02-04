#include <cstdlib>
#include <cstdio>
#include <string.h>

int root(char r);
int user(char u);

char r[10] = "root", t[10] = "toor";

//C++ bate版，算法参考python版

int main()
{
	char kef[10], usef[10];

	printf("Ocean |版本 1.0.0\n");
	printf("©2013-2019  RED \n");
	printf("  \n");
	printf("户名:");
	scanf_s("%s",&usef);

	if (strcmp(usef,r)==0)
	{
		printf("密匙");
		scanf_s("%s",&kef);
		if (strcmp(kef,t)==1)
		{
			printf("Ocean [版本 1.0.0 bate] \n");
			printf("(c) 2020 Dream_Programmer \n");
			printf(" \n");
			int k();
				char raw_input[20];
				char tool[10] = "tool", ip[10] = "ip";
				scanf_s("-->%s",&raw_input);

			
		}
		else
		{

			printf("对不起，您输入的密码有误\n");
			printf("  \n");

		}



	}
	else
	{

		printf("库中不存在您的信息，请检查后重试");
		printf("");

	}
	
	return 0;
}