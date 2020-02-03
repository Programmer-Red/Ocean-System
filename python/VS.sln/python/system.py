#encoding:utf-8

import os
import sys
import urllib2
import time
reload(sys)
sys.setdefaultencoding("utf-8")

def system():
	a=0
	print "请先输入您的账号以及密码		\n"
	Acc=raw_input("账号：")
	Pas=raw_input("密码：")
	if Acc=="root":
		#默认账号是root
		if Pas=="toor":
                        print "      \n"
                        print "       \n"
			print "欢迎使用Ocean，现在的时间是:"
			os.system("date \n")
			print "		\n"
			print "========================================================\n"
			print "您可以使用“帮助”命令来查看相应的命令提示 	\n"
                        def fonr():
				fonrf=raw_input("-->")
				if fonrf=="设置":
					def shzr():
						#↑↑↑这个是设置的缩写
						print "您可以通过输入下面选项前的数字来介入相关内容\n"
						print "1.网络	2.编程	\n"
						print "3.退出	\n"
						print "	\n"
						shzrf=input("-->")
						if shzrf==3:
							fonr()
						if shzrf==1:
							def wlanr():
								print "1.网络测试	2.退出"
								wlanrf=input("-->")
								if wlanrf==1:
									print "请稍后，我们将为您载入网络测试模式...... 	\n"
									print "提示：如果您看到“请求超时”等字样，就说明您的计算机网络连接存在问题，请及时检查网卡以及驱动或者网口是否连接正常\n"
									#先等待五秒让用户看一会儿。。。。
									time.sleep(5)
									os.system("ping www.baidu.com")
									time.sleep(2)
									print "测试结束，我们将为您转入“网络”设置的选择界面\n"

									wlanr()
								if wlanrf==2:
									shzr()
							wlanr()
						if shezrf==2:
							def bcszr():
								print "请问需要将默认编程语言转换为哪一种？"
								print "1.Python    2.ken \n"
								print "3.退出\n"
								bcszrf=input("-->")
								if bcszrf==1:

									print "已将编程语言设置为了python\n"
									a=0
									bcszr()
								if bcszrf==2:
									print "已将编程语言设置为了ken\n"
									a=1
									bcszr()
							bcszr()
					shzr()
				if fonrf=="编程":
					def bcr():
						if a==0:
							print "我们将为您打开python，请稍后...... \n"
							time.sleep(3)
							os.system("python")
						if a==1:
							print "我们将为您转入ken的Ocean版，请稍后....... \n"
							time.sleep(3)
							os.system("ken")
					bcr()
				if fonrf=="关于":
					def aboutr():
						aboutrr=open("about.txt")
						aboutr=aboutrr.readline()
						print aboutr
					aboutr()
				if fonrf=="":
					print "您还没有输入命令"
					fonr()
				if fonrf=="帮助":
					def helpr():
						helprr=open("./help.txt")
						helpr=helprr.readline()
						print helpr
					helpr()
				if fonrf=="计算器":
					print "请直接输入您想计算的公式(输入“退出”即可回到初始界面)\n"
					def outworkr():
						#千万不能改成raw_input,不然会出现无法输入数字字符的BUG
						owrf=input("-->")
						input(owrf)
						outworkr()
					outworkr()
				if fonrf=="安全模式":
					#不能用直接调试SU的函数
					def fon():
						print "欢迎使用Ocean系统，现在的时间是:"
						os.system("date /t")
						print "		\n"
						print "========================================================\n"
						print "您可以使用“帮助”命令来查看相应的命令提示 	\n"
						fonf=raw_input("-->")
						if fonf=="设置":
							def shz():
								#↑↑↑这个是设置的缩写
								print "您可以通过输入下面选项前的数字来介入相关内容\n"
								print "1.网络	2.编程	\n"
								print "3.退出	\n"
								print "	\n"
								shzf=input("-->")
								if shzf==3:
									fon()
								if shzf==1:
									def wlan():
										print "1.网络测试	2.退出"
										wlanf=input("-->")
										if wlanf==1:
											print "请稍后，我们将为您载入网络测试模式...... 	\n"
											print "提示：如果您看到“请求超时”等字样，就说明您的计算机网络连接存在问题，请及时检查网卡以及驱动或者网口是否连接正常\n"
											#先等待五秒让用户看一会儿。。。。
											time.sleep(5)
											os.system("ping www.baidu.com")
											time.sleep(2)
											print "测试结束，我们将为您转入“网络”设置的选择界面\n"

											wlan()
										if wlanf==2:
											shz()
									wlan()
								if shezf==2:
									def bcsz():
										print "请问需要将默认编程语言转换为哪一种？"
										print "1.Python    2.ken \n"
										print "3.退出\n"
										bcszf=input("-->")
										if bcszf==1:

											print "已将编程语言设置为了python\n"
											a=0
											bcsz()
										if bcszf==2:
											print "已将编程语言设置为了ken\n"
											a=1
											bcsz()
									bcsz()
					   		shz()
				  	  	if fonf=="编程":
					   		def bc():
						 	    if a==0:
								    print "我们将为您打开python的移植版，请稍后...... \n"
								    time.sleep(3)
								    os.system("python")
							    if a==1:
							   		print "我们将为您转入ken的Ocean版，请稍后....... \n"
									time.sleep(3)
									os.system("ken")
							bc()
						if fonf=="关于":
							def about():
								aboutr=open("about.txt")
								about=aboutr.readline()
								print about
							about()
						if fonf=="":
							print "您还没有输入命令"
						if fonf=="帮助":
							def help():
								helprr=open("help.txt")
								helpr=helprr.readline()
								print helpr
							help()
						if fonf=="计算器":
							print "请直接输入您想计算的公式(输入“退出”即可回到初始界面)\n"
							def outwork():
								#千万不能改成raw_input,不然会出现无法输入数字字符的BUG
								owf=input("-->")
								input(owf)
								outwork()
							outwork()
						else:
							print "您输入的指令有误"
							fon()
					fon()
				else:
					print "您输入的指令有误"
                		        fonr()
			fonr()
		else:
			print "对不起，您输入的密码不正确"
			system()
	elif Acc=="oceaner":
		#普通用户的账号是windows
		if Pas=="boot":
			def fon():
				print "欢迎使用Ocean系统，现在的时间是:"
				os.system("date /t")
				print "		\n"
				print "========================================================\n"
				print "您可以使用“帮助”命令来查看相应的命令提示 	\n"
				fonf=raw_input("-->")
				if fonf=="设置":
					def shz():
						#↑↑↑这个是设置的缩写
						print "您可以通过输入下面选项前的数字来介入相关内容\n"
						print "1.网络	2.编程	\n"
						print "3.退出	\n"
						print "	\n"
						shzf=input("-->")
						if shzf==3:
							fon()
						if shzf==1:
							def wlan():
								print "1.网络测试	2.退出"
								wlanf=input("-->")
								if wlanf==1:
									print "请稍后，我们将为您载入网络测试模式...... 	\n"
									print "提示：如果您看到“请求超时”等字样，就说明您的计算机网络连接存在问题，请及时检查网卡以及驱动或者网口是否连接正常\n"
									#先等待五秒让用户看一会儿。。。。
									time.sleep(5)
									os.system("ping www.baidu.com")
									time.sleep(2)
									print "测试结束，我们将为您转入“网络”设置的选择界面\n"

									wlan()
								if wlanf==2:
									shz()
							wlan()
						if shezf==2:
							def bcsz():
								print "请问需要将默认编程语言转换为哪一种？"
								print "1.Python    2.ken \n"
								print "3.退出\n"
								bcszf=input("-->")
								if bcszf==1:

									print "已将编程语言设置为了python\n"
									a=0
									bcsz()
								if bcszf==2:
									print "已将编程语言设置为了ken\n"
									a=1
									bcsz()
							bcsz()
					shz()
				if fonf=="编程":
					def bc():
						if a==0:
							print "我们将为您打开python的移植版，请稍后...... \n"
							time.sleep(3)
							os.system("python")
						if a==1:
							print "我们将为您转入ken的Ocean版，请稍后....... \n"
							time.sleep(3)
							os.system("ken")
					bc()
				if fonf=="关于":
					def about():
						aboutr=open("about.txt")
						about=aboutr.readline()
						print about
					about()
				if fonf=="":
					print "您还没有输入命令"
				if fonf=="帮助":
					def help():
						helprr=open("help.txt")
						helpr=helprr.readline()
						print helpr
					help()
				if fonf=="计算器":
					print "请直接输入您想计算的公式(输入“退出”即可回到初始界面)\n"
					def outwork():
						#千万不能改成raw_input,不然会出现无法输入数字字符的BUG
						owf=input("-->")
						input(owf)
						outwork()
					outwork()
				else:
					print "您输入的指令有误"
					fon()
			fon()
		else:
			print "对不起，您输入的密码不正确"
	if Acc=="su":
		def kalib():
			print "您确定进入安全模式吗？\n"
			kalib=raw_input("是 or 否：")
			if kalib=="是":
				print "我们将自动转入普通用户来开启Ocean，但是我们将不会打开大部分功能，而是开启一些常用功能并且您的使用经过将会被记录在Ocean的超级用户中\n"
				def fon():
					print "欢迎使用Ocean系统，现在的时间是:"
					os.system("date /t")
					print "		\n"
					print "========================================================\n"
					print "您可以使用“帮助”命令来查看相应的命令提示 	\n"
					fonf=raw_input("-->")
					if fonf=="设置":
						def shz():
							#↑↑↑这个是设置的缩写
							print "您可以通过输入下面选项前的数字来介入相关内容\n"
							print "1.网络	2.编程	\n"
							print "3.退出	\n"
							print "	\n"
							shzf=input("-->")
							if shzf==3:
								fon()
							if shzf==1:
								def wlan():
									print "1.网络测试	2.退出"
									wlanf=input("-->")
									if wlanf==1:
										print "请稍后，我们将为您载入网络测试模式...... 	\n"
										print "提示：如果您看到“请求超时”等字样，就说明您的计算机网络连接存在问题，请及时检查网卡以及驱动或者网口是否连接正常\n"
										#先等待五秒让用户看一会儿。。。。
										time.sleep(5)
										os.system("ping www.baidu.com")
										time.sleep(2)
										print "测试结束，我们将为您转入“网络”设置的选择界面\n"

										wlan()
									if wlanf==2:
										shz()
								wlan()
							if shezf==2:
								def bcsz():
									print "请问需要将默认编程语言转换为哪一种？"
									print "1.Python    2.ken \n"
									print "3.退出\n"
									bcszf=input("-->")
									if bcszf==1:

										print "已将编程语言设置为了python\n"
										a=0
										bcsz()
									if bcszf==2:
										print "已将编程语言设置为了ken\n"
										a=1
										bcsz()
								bcsz()
						shz()
					if fonf=="编程":
						def bc():
							if a==0:
								print "我们将为您打开python的移植版，请稍后...... \n"
								time.sleep(3)
								os.system("python")
							if a==1:
								print "我们将为您转入ken的Ocean版，请稍后....... \n"
								time.sleep(3)
								os.system("ken")
						bc()
					if fonf=="关于":
						def about():
							aboutr=open("about.txt")
							about=aboutr.readline()
							print about
						about()
					if fonf=="":
						print "您还没有输入命令"
					if fonf=="帮助":
						def help():
							helprr=open("help.txt")
							helpr=helprr.readline()
							print helpr
						help()
					if fonf=="计算器":
						print "请直接输入您想计算的公式(输入“退出”即可回到初始界面)\n"
						def outwork():
							#千万不能改成raw_input,不然会出现无法输入数字字符的BUG
							owf=input("-->")
							input(owf)
							outwork()
						outwork()
					else:
						print "您输入的指令有误"
						fon()
				fon()
			
				
			elif kalib=="否":
				system()
			else:
				print "您输入的指令有误，请重新输入\n"
				kalib()
		kalib()
	else:
		print "对不起，您输入的账号不存在，请重新尝试	\n"
		system()
system()

