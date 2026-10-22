def temp(t):
     if t >= 35 and t <= 40:
         print(f"现在是{t}摄氏度,天气炎热，不能出去玩。")
     elif t >= 22 and t <= 35:
         print(f"现在是{t}摄氏度,天气合适，适合出去玩。")
     elif t >= 10 and t <= 22:
         print(f"现在是{t}摄氏度,天气比较凉，出去玩多穿衣服。")
     else:
         print("极端天气，不能出去玩。")

t=int(input("请输入的温度："))
temp(t)