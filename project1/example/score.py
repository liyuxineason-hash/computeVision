def score_c(e, c, m):
    scores = {"英语": e, "语文": c, "数学": m}

    score_max = max(scores.values())
    score_min = min(scores.values())
    score_sum = sum(scores.values())

    max_name = max(scores, key=scores.get)  # 得分最高的科目名
    min_name = min(scores, key=scores.get)  # 得分最低的科目名

    print(f"小米的最高成绩是{max_name}:{score_max}")
    print(f"小米的最低成绩是{min_name}:{score_min}")
    print(f"小米的总成绩是{score_sum}")

e = int(input("请输入英语成绩："))
c = int(input("请输入语文成绩："))
m = int(input("请输入数学成绩："))

score_c(e, c, m)
