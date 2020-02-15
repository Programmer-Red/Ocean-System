#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Windows.h>
#define che 3

//声明函数
void network();

//申请输入变量
char input[che] = 0;

//申请函数内局部变量
char net[che];

void tool()
{
	printf("您可以通过输入下面选项前的数字来介入相关内容\n");
	printf("   \n");
	printf("1.网络 \n");
	printf("-->");
	scanf_s("%s",input,che);
	if (input==net)
	{
		network();
	}
	
	system("pause");
}

void network()
{
	printf("1.网络测试   2.返回上一级菜单 \n");
	printf("-->");
	scanf_s("%s",input,che);
	if (input == "1")
	{
		printf("请问您的使用地点是否为中国大陆(PRC)或朝鲜地区（PRK）？\n");
		printf("1.是的   2.不是 \n");
		printf("-->");
		scanf_s("%s", input, che);
		if (input == "1")
		{
			printf("请稍后，将为您载入网络测试模式...... 	\n");
			printf("提示：如果您看到“请求超时”等字样，说明您的计算机网络连接存在问题，请及时检查网络驱动或网口是否连接正常\n");
			printf("      数据包收发测试将不会自动停止，请在检查收发状况正常后按“ctrl”和“c”来终止测试 \n");
			sleep(3000);
			system("ping www.baidu.com");
			sleep(2000);
			printf("测试结束，我们将为您转入“网络”设置界面 \n");
		}
		if(input=="2")
		{
			printf("请稍后，将为您载入网络测试模式...... 	\n");
			printf("提示：如果您看到“请求超时”等字样，说明您的计算机网络连接存在问题，请及时检查网络驱动或网口是否连接正常\n");
			printf("      数据包收发测试将不会自动停止，请在检查收发状况正常后按“ctrl”和“c”来终止测试 \n");
			sleep(3000);
			system("ping www.google.com");
			sleep(2000);
			printf("测试结束，我们将为您转入“网络”设置界面 \n");
		}
		else
		{
			printf("对不起，您输入的指令有误 \n");
			network();
		}
	}
	if(input=="2")
	{
		tool();
	}
	else
	{
		printf("对不起，您输入的指令有误 \n");
		network();
	}
}