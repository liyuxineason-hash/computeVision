def eat(time):
    if time>=7 and time<=9:
        print(f"现在是{time}点,该吃早饭。")
    elif time>=11 and time<=14:
        print(f"现在是{time}点，去吃午饭。")
    elif time>=17 and time<=19:
        print(f"现在是{time}点,去吃晚饭。")
    else:
        print("现在还不是饭点")

t=int(input("请输入现在是几点："))
eat(t)