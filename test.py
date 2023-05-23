money = 5000000
name = None

#要求客户输入姓名
name = input("请输入您的姓名:")
#定义查询函数
def query():
    print("----------查询余额----------")
    print(f"您好，{name}，您的余额剩余:{money}元")
#定义存款函数
def saving(num):
    global money
    money += num
    print(f"您好，{name}，成功存入{num}元,您的余额剩余:{money}元")
#定义取款函数
def withdraw(num):
    global money
    money -= num
    print(f"您好，{name}，成功取出{num}元,您的余额剩余:{money}元")
#定义主菜单函数
def show_menu():
    print("欢迎来到北国银行")
    print("1.查询余额")
    print("2.存款")
    print("3.取款")
    option = int(input("请输入您需要的服务: "))
    if option == 1:
        query()
    elif option == 2:
        money = int(input("请输入您要存的金额: "))
        saving(money)
    elif option == 3:
        money = int(input("请输入您要取出的金额: "))
        withdraw(money)
#设置无限循环，确保程序不退出
while True:
    show_menu()