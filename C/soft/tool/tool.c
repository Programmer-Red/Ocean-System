#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Windows.h>
#define che 3

//��������
void network();

//�����������
char input[che] = 0;

//���뺯���ھֲ�����
char net[che];

void tool()
{
	printf("������ͨ����������ѡ��ǰ�������������������\n");
	printf("   \n");
	printf("1.���� \n");
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
	printf("1.�������   2.������һ���˵� \n");
	printf("-->");
	scanf_s("%s",input,che);
	if (input == "1")
	{
		printf("��������ʹ�õص��Ƿ�Ϊ�й���½(PRC)���ʵ�����PRK����\n");
		printf("1.�ǵ�   2.���� \n");
		printf("-->");
		scanf_s("%s", input, che);
		if (input == "1")
		{
			printf("���Ժ󣬽�Ϊ�������������ģʽ...... 	\n");
			printf("��ʾ�����������������ʱ����������˵�����ļ�����������Ӵ������⣬�뼰ʱ������������������Ƿ���������\n");
			printf("      ���ݰ��շ����Խ������Զ�ֹͣ�����ڼ���շ�״�������󰴡�ctrl���͡�c������ֹ���� \n");
			sleep(3000);
			system("ping www.baidu.com");
			sleep(2000);
			printf("���Խ��������ǽ�Ϊ��ת�롰���硱���ý��� \n");
		}
		if(input=="2")
		{
			printf("���Ժ󣬽�Ϊ�������������ģʽ...... 	\n");
			printf("��ʾ�����������������ʱ����������˵�����ļ�����������Ӵ������⣬�뼰ʱ������������������Ƿ���������\n");
			printf("      ���ݰ��շ����Խ������Զ�ֹͣ�����ڼ���շ�״�������󰴡�ctrl���͡�c������ֹ���� \n");
			sleep(3000);
			system("ping www.google.com");
			sleep(2000);
			printf("���Խ��������ǽ�Ϊ��ת�롰���硱���ý��� \n");
		}
		else
		{
			printf("�Բ����������ָ������ \n");
			network();
		}
	}
	if(input=="2")
	{
		tool();
	}
	else
	{
		printf("�Բ����������ָ������ \n");
		network();
	}
}