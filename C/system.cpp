#include <cstdlib>
#include <cstdio>
#include <string.h>

int root(char r);
int user(char u);
int
char r[10] = "root", t[10] = "toor";

//首个C++的bate版本，算法基本和旧版Python一致

int main()
{
	char kef[10], usef[10];

	printf("Ocean |版本 1.0.0\n");
	printf("©2013-2019  RED \n");
	printf("  \n");
	printf("户名:");
	scanf_s("%c",&usef);

	if (strcmp(usef,r)==1)
	{
		printf("密匙");
		scanf_s("%c",&kef);
		if (strcmp(kef,t)==1)
		{
			printf("Ocean [版本 1.0.0 bate] \n");
			printf("(c) 2020 Dream_Programmer \n");
			prinft(" \n");
			char raw_input[20];
			char tool[10] = "tool", ip[10] = "ip";
			scanf("-->",&raw_input);

		}
		else
		{

			printf("对不起，您输入的密码有误");


		}



	}
	else
	{
		printf("库中不存在您的信息，请检查后重试");


	}
	
	return 0;
}

