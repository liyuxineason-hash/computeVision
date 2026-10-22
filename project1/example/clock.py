import cv2
import numpy as np
import math
import time

cx = 300
cy = 300
R = 220

# ---------- 静态表盘：只画一次 ----------
image = np.zeros((560, 560, 3), dtype="uint8") + 255

cv2.circle(image, (cx, cy), R, (0, 0, 0), 4, cv2.LINE_AA)
cv2.circle(image, (cx, cy), R - 8, (200, 200, 200), -1, cv2.LINE_AA)

# ---------- 标题 ----------
cv2.putText(image, 'OPENCV CLOCK', (120, 68),
            cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 255), 3, cv2.LINE_AA)

# ---------- 刻度 ----------
# 老规定：0° = 12点，顺时针 → 直接用 i*6，不用减90
for i in range(60):
    angle = math.radians(i * 6)          # ← 和新代码的区别1：没有 - 90
    if i % 5 == 0:
        r1 = R - 25                      # 整点刻度：长、粗、黑
        thickness = 4
        color = (0, 0, 0)
    else:
        r1 = R - 15                      # 分钟刻度：短、细、灰
        thickness = 2
        color = (80, 80, 80)

    # 老规定公式：sin管x，cos管y，y取减号
    x1 = int(cx + r1 * math.sin(angle))
    y1 = int(cy - r1 * math.cos(angle))          # ← 区别2：减号
    x2 = int(cx + (R - 12) * math.sin(angle))
    y2 = int(cy - (R - 12) * math.cos(angle))    # ← 区别2：减号
    cv2.line(image, (x1, y1), (x2, y2), color, thickness, cv2.LINE_AA)

# ---------- 数字 1~12 ----------
font = cv2.FONT_HERSHEY_SIMPLEX
for h in range(1, 13):
    angle = math.radians(h * 30)         # ← 区别1：没有 - 90
    r_text = R - 48
    x = int(cx + r_text * math.sin(angle))
    y = int(cy - r_text * math.cos(angle))       # ← 区别2：减号
    text = str(h)
    (tw, th), _ = cv2.getTextSize(text, font, 1.0, 2)
    cv2.putText(image, text, (x - tw // 2, y + th // 2),
                font, 1.0, (0, 0, 0), 2, cv2.LINE_AA)

# ---------- 指针 ----------
def draw_hand(canvas, angle_deg, length, thickness, color):
    """angle_deg: 从12点方向顺时针起算的钟表角度，直接传入即可"""
    angle = math.radians(angle_deg)      # ← 区别1：没有 - 90，更直观！
    x = int(cx + length * math.sin(angle))
    y = int(cy - length * math.cos(angle))       # ← 区别2：减号
    cv2.line(canvas, (cx, cy), (x, y), color, thickness, cv2.LINE_AA)

def draw_clock():
    canvas = image.copy()
    t = time.localtime()
    hour = t.tm_hour % 12
    minute = t.tm_min
    second = t.tm_sec

    # 时间→角度的换算完全不变（因为老规定的角度本来就是钟表角度）
    sec_angle  = second * 6
    min_angle  = minute * 6 + second * 0.1
    hour_angle = hour * 30 + minute * 0.5

    draw_hand(canvas, hour_angle, R - 90, 8, (0, 0, 0))
    draw_hand(canvas, min_angle,  R - 55, 5, (0, 0, 0))
    draw_hand(canvas, sec_angle,  R - 40, 2, (0, 0, 255))

    cv2.circle(canvas, (cx, cy), 8, (0, 0, 0), -1, cv2.LINE_AA)
    cv2.imshow('clock', canvas)

# ---------- 动态循环 ----------
while True:
    draw_clock()
    if cv2.waitKey(200) & 0xFF == 27:    # ESC 退出
        break

cv2.destroyAllWindows()
