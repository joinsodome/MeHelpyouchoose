import random,time
list = []
def helpyouchoose():
        print('''Kangzexi 帮你选择 v1.0
        版权所有 <c> Kangzexi 保留所有权利。
        ''')
        test = True
        while test:
            choose = input('依次输入让你头晕的选择吧（注：完成后请输入Y）：')
            if choose != 'Y':
                list.append(choose)
            if choose == 'Y':
                test = False
        while True:
            listchoise = random.choice(list)
            choosen = input('我选择了【'+listchoise+'】，你觉得行吗？行了输入Y，不行就回车：')
            if choosen == 'Y':
                print('那我们就这么决定啦！')
                break
helpyouchoose()
print('感谢您的使用！')
time.sleep(1)