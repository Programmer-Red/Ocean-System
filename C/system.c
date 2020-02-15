#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "..\C\soft\tool\tool.h"
#define cat 50

void root();
void user();
void rootr(char input[cat]);



char o[cat] = "root", t[cat] = "toor";   
char e[cat] = "window", r[cat] = "windows";
char error[1] = "";
//先这样简单粗暴地解决一下账户密码验证的问题就好wwwww



//C++ bate版，算法参考python版
int main()
{
	char kef[cat], usef[cat];



	printf("户名:");
	scanf_s("%s",&usef,cat);

	if (strcmp(usef,o)==0)
	{
		printf("密码:");
		scanf_s("%s",&kef,cat);
		if (strcmp(kef,t)==0)
		{
			char Rraw_input[cat];
			printf("   \n");
			printf("   \n");
			printf("Ocean [版本 1.0.0 bate] \n");
			printf("(c) 2020 Dream_Programmer \n");
			printf("现在时间是：");
			system("date");
			printf("  \n");
			root();
		}
		else
		{
			printf("对不起，您输入的密码有误\n");
			printf("  \n");
			main();
		}
	}
	if (strcmp(usef,e) == 0)
	{

		printf("密码:");
		scanf_s("%s", &kef,cat);
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
	if (strcmp(usef,error)==0)
	{
		printf("不存在的账户，请检查后重试");
		printf("   \n");
		main();
	}
	else
	{
		printf("不存在的账户，请检查后重试");
		printf("   \n");
		main();
	}
	system("pause");
	return 0;
}

void root()
{
	char Rraw_input[cat];
	printf("-->");
	scanf_s("%s", Rraw_input, cat);
	rootr(Rraw_input);
	system("pause");
}


void user()
{
	char raw_input[cat];
	printf("Ocean [版本 1.0.0 bate] \n");
	printf("(c) 2020 Dream_Programmer \n");
	printf(" \n");
	printf("-->");
	scanf_s("%s", raw_input,cat);

}

void rootr(char input[cat])
{

	char toolr[cat]="工具";
	char outwork[cat]="计算器";




	if (strcmp(input,toolr)==0)
	{
		tool();
		
	}
	if (strcmp(input,outwork)==0)
	{
		
	}
	else
	{
		printf("您输入的指令有误");
		root();
	}
	system("pause");
}