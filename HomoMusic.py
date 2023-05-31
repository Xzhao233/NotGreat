import os
a=0
input('按下Enter开始游戏...')
os.system('cls')
print('计数君：' + str(a))
while 1:
    input('Press Enter')
    os.system('start mshta vbscript:MSGBOX("我们是乐子人",20,"HomoMusic")(window.close)')
    a += 1
    os.system('cls')
    print('计数君：' + str(a))
