def bmi_func(sg,tz):

    b=tz/(sg*sg)
    print(f"你的bmi是：{b:.2f}")

sg=float(input("请输入你的身高(米)："))
tz=float(input("请输入你的体重(千克)："))
bmi_func(sg,tz)