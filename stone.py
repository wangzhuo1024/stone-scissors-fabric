



import os
import random  #库导入
import time
import sys
def inte(a,p):
    if not a.isdigit():
        print('\033[31m你在耍我?🙂,\033[0m',p)
def loading():
    sum = random.randint(6,10)/10        # 设置倒计时时间
    timeflush = 0.25                        # 设置屏幕刷新的间隔时间
    for i in range(0, int(sum/timeflush)):
        list = ["\\", "|", "/", "—"]
        index = i % 4
        print("\r loading {}  \r".format(list[index]), end="")
        time.sleep(timeflush)

rule = {1: '石头', 2: '剪刀', 3: '布'}
print('欢迎游玩stone scissors fabric v0.4,这是一个石头剪刀布程序')
print('更新时间:2024-06-23_12-25-05')
print('')
run = 1

while run == 1:
    time.sleep(0.2)
    n = input('\033[33m请输入回合数:\033[0m')
    inte(n,'赶紧毁灭吧') #初始化
    n = int(n)          #总回合数
    r = 0               #当前回合数
    Pc=''
    Pcc=0
    Plc=0
    Los=0

    level=input('\033[33m请选择难度:1:简单 2,适中 3,困难 4,难哭。请输入数字:\033[0m')
    time.sleep(0.2)   #难度选择
    if level.isdigit():
        level = int(level)
        if  level >= 5:
            print('\033[31m🙂故意找茬是不是\033[0m')
            level = 4
        else:
            pass


        if level == 4:
            qs=input('\033[31m你真的确定么???是的话请按1,否则请按2\033[0m')
            if not qs.isdigit():
                print('\033[31m🙂\033[0m')
                print('\033[31m🙂呵呵呵\033[0m')
                print('\033[31m🤬\033[0m')
                print('\033[31m🙂看你脑子不大灵光的份上,给你换成极易模式\033[0m')
                level=5
            else:
                qs=int(qs)
                if qs == 1:
                    print('\033[31m🙂好吧,输到哭别来找我\033[0m')
                    level=4
                else:
                    print('\033[31m🙂好吧,给你呼死你适中模式\033[0m')
                    level=2
    elif level == '#':
        level = 5
    else:
        print('\033[31m🙂你觉得你很搞笑?\033[0m')
        level=4


    while r < n:           #重复执行回合数次
        
        time.sleep(0.2)
        
        print('手势编号:',rule)
        p = input('\033[33m请输入手势编号:\033[0m')
        if p.isdigit():
            p = int(p)
            if p < 4:
                print('\033[32m玩家选择:\033[0m', rule[p])  # 玩家输入
            else:
                print('\033[31m🙂你觉得你很搞笑?编号错误,请重新输入\033[0m')
                continue
        else:
            print('\033[31m🙂你觉得你很搞笑?编号错误,请重新输入\033[0m')
            continue
        # 电脑难度
    #电脑手势

        if level==4:                                 #超难
            if p == 1:                               #电脑跟玩家对着干，根本赢不了zzzz
                Pc=3
            if p == 2:
                Pc=1
            if p == 3:
                Pc=2

        elif level==3:                               #难
            sjs=random.randint(1,2)                  #随机选择超难，random随机数 1，超难 2，随机
            if sjs == 1:
                if p == 1:                               # 电脑跟玩家对着干，根本赢不了zzzz
                    Pc = 3
                if p == 2:
                    Pc = 1
                if p == 3:
                    Pc = 2
            else:
                Pc=random.randint(1,3)
        elif level == 1:
            sjs = random.randint(1, 2)  # 随机选择是不是极易，random随机数 1，极易 2，随机
            if sjs == 1:
                if p == 1:  # 全是玩家赢
                    Pc = 2
                if p == 2:
                    Pc = 3
                if p == 3:
                    Pc = 1
            else:
                Pc = random.randint(1, 3)
        elif level == 5:                                                  #彩蛋
            if p == 1:                                              #全是玩家赢
                Pc = 2
            if p == 2:
                Pc = 3
            if p == 3:
                Pc = 1

        else:                                           #简单
            Pc = random.randint(1, 3)                                                    #只有随机数
        
        #loading()
        print('\033[34m电脑选择:\033[0m',rule[Pc])                                         #胜负判断
        r += 1
        if (p == 1 and Pc == 2) or (p == 2 and Pc == 3) or (p == 3 and Pc == 1):
            print()
            time.sleep(0.2)
            print('     胜利🙂')
            
            Plc+=1
        elif p == Pc:
            print()
            time.sleep(0.2)
            print('     平局🙂')
            
            
        else:
            print()
            time.sleep(0.2)
            print('     失败🙂')
            
            Pcc+=1
            Los+=1

        shengfubi = str(Plc)+'/'+str(Pcc)
        print('\033[35m胜负比:\033[0m',shengfubi,end='')
        print(';',end='')
        print('\033[36m回合数\033[0m',str(r)+'/'+str(n))
        #print(Los/r)#当前局数
        #print(Los/n)#总局数
        #os.system('cls')
        time.sleep(1)
        



    if Plc>Pcc:
        time.sleep(0.2)
        print()                                            #最后的胜负判断
        print('\033[32m》》》》》》胜利✌《《《《《《\033[0m')
    elif Pcc==Plc:
        time.sleep(0.2)
        print()
        print('》》》》》》平局🙂《《《《《《')
    else:
        time.sleep(0.2)
        print()
        print('\033[31m》》》》》》失败🙂《《《《《《\033[0m')
        if  Los/n >0.6:
            time.sleep(0.2)
            print('\033[31m🙂啊啊啊额,怎么说呢,额...\033[0m',end = '')
            print('\033[31m🙂你是真的厉害\033[0m',end = '')
            print('\033[31m🙂失败率:\033[0m',(Los/r)*100,'%')

    exit = input('按q退出按r再来一局:')
    if exit == 'q' or exit == 'Q':
        sys.exit()
    elif exit == 'r' or exit == 'R':
        continue
    else:
        print('\033[31m你在耍我?🙂\033[0m',p)
        time.sleep(0.6)
        sys.exit()