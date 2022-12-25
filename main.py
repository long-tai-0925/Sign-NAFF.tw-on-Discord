#import一些東西
import webbrowser #import webbrowser
import time #import time
import keyboard #import keyboard

#變數設定
times = 0 #時間的變數
urL='https://discord.com/channels/991097038382964777/1007154010085662721' #設定開啟的網址

#不斷重複
while True: #就是我讓這裡不會停的
	times += 1 #把times +1
	time.sleep(1) #等一秒Code也是會累的
	if times == 28800: #如果時間過了八小時(我真的去算成秒)
		webbrowser.get('windows-default').open_new(urL) #開啟https://discord.com/channels/991097038382964777/1007154010085662721
		time.sleep(15) #等待15秒(DC開啟需要時間)
		keyboard.write("!s") #打簽到指令
		keyboard.press_and_release("enter") #傳送出去
		times = 0 #重製時間
	print (f"{times}") #顯示現在經過幾秒
