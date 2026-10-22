import math
import time
import numpy as np
import cv2

cx, cy, R = 280, 300, 220

# 1. 先画好"表盘模板"：表盘、刻度、数字只画一次，指针每帧在上面重画
def draw_face():
    img = np.zeros((560, 560, 3), np.uint8)
    img[:] = (245, 245, 245)
    cv2.circle(img, (cx, cy), R, (0, 0, 0), 6, cv2.LINE_AA)
    cv2.circle(img, (cx, cy), R - 8, (200, 200, 200), -1, cv2.LINE_AA)

    for i in range(60):
        ang = math.radians(i * 6)
        if i % 5 == 0:
            r1, r2, w = R - 30, R - 8, 2
        else:
            r1, r2, w = R - 18, R - 8, 1
        p1 = (int(cx + r1 * math.sin(ang)), int(cy - r1 * math.cos(ang)))
        p2 = (int(cx + r2 * math.sin(ang)), int(cy - r2 * math.cos(ang)))
        cv2.line(img, p1, p2, (0, 0, 0), w, cv2.LINE_AA)

    for i in range(1, 13):
        ang = math.radians(i * 30)
        tx = int(cx + (R - 55) * math.sin(ang))
        ty = int(cy - (R - 55) * math.cos(ang))
        cv2.putText(img, str(i), (tx - 12, ty + 12),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(img, "OPENCV CLOCK", (120, 60),
                cv2.FONT_HERSHEY_DUPLEX, 1.3, (0, 0, 255), 2, cv2.LINE_AA)
    return img

face = draw_face()   # 生成一次表盘模板

def draw_hand(img, angle_deg, length, color, thick):
    a = math.radians(angle_deg)
    p = (int(cx + length * math.sin(a)), int(cy - length * math.cos(a)))
    cv2.line(img, (cx, cy), p, color, thick, cv2.LINE_AA)

# 2. 主循环：取时间 → 画指针 → 刷新
while True:
    img = face.copy()               # 复制模板做底，指针就不会"残留"
    t = time.localtime()            # 获取当前时间
    h, m, s = t.tm_hour, t.tm_min, t.tm_sec

    hour_ang = (h % 12) * 30 + m * 0.5   # 时针：时×30 + 分×0.5
    min_ang  = m * 6 + s * 0.1           # 分针：分×6 + 秒×0.1（带平滑）
    sec_ang  = s * 6                     # 秒针：秒×6

    draw_hand(img, hour_ang, 120, (0, 0, 0), 8)
    draw_hand(img, min_ang, 170, (0, 0, 0), 5)
    draw_hand(img, sec_ang, 185, (0, 0, 255), 2)

    cv2.circle(img, (cx, cy), 10, (0, 0, 0), -1)
    cv2.circle(img, (cx, cy), 4, (255, 255, 255), -1)

    cv2.imshow("clock", img)
    if cv2.waitKey(100) == 27:      # 100ms 一帧（约10帧/秒），按 ESC 退出
        break

cv2.destroyAllWindows()