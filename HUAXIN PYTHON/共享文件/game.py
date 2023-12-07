import pygame
import sys
import threading
import time
# 初始化Pygame
pygame.init()

# 设置窗口大小
width, height = 800, 600
size = (width, height)
长 = 50
宽 = 50
x = width/2
y = height/2
# 创建窗口
screen = pygame.display.set_mode(size)
pygame.display.set_caption("游戏()")
font = pygame.font.Font(None, 36)
# 设置颜色
white = (255, 255, 255)
blue = (0, 0, 255)
s = 1
t = 0
def 后台进程():
    pygame.event.pump()
    global x,y,t
    # 画一个蓝色的矩形
    while True:

        pass



后台进程_ = threading.Thread(target=后台进程)
后台进程_.start()
# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if x <= 0:
        x += 10
    if y <= 0:
        y += 10
    if y >= 550:
        y -= 10
    if x >= 750:
        x -= 10
    if keys[pygame.K_w]:
        s = 1
        y -= s
        if x <= 0:
            x += 10
        if y <= 0:
            y += 10
        if y >= 550:
            y -= 10
        if x >= 750:
            x -= 10

    if keys[pygame.K_s]:
        s = 1
        y += s
        if x <= 0:
            x += 10
        if y <= 0:
            y += 10
        if y >= 550:
            y -= 10
        if x >= 750:
            x -= 10

    if keys[pygame.K_a]:
        s = 1
        x -= s
        if x <= 0:
            x += 10
        if y <= 0:
            y += 10
        if y >= 550:
            y -= 10
        if x >= 750:
            x -= 10

    if keys[pygame.K_d]:
        s = 1
        x += s
        if x <= 0:
            x += 10
        if y <= 0:
            y += 10
        if y >= 550:
            y -= 10
        if x >= 750:
            x -= 10

    if keys[pygame.K_w] and keys[pygame.K_LCTRL]:
        s = 10
        y -= s
        if x <= 0:
            x += 10
        if y <= 0:
            y += 10
        if y >= 550:
            y -= 10
        if x >= 750:
            x -= 10

    if keys[pygame.K_s] and keys[pygame.K_LCTRL]:
        s = 10
        y += s
        if x <= 0:
            x += 10
        if y <= 0:
            y += 10
        if y >= 550:
            y -= 10
        if x >= 750:
            x -= 10
    if keys[pygame.K_a] and keys[pygame.K_LCTRL]:
        s = 10
        x -= s
        if x <= 0:
            x += 10
        if y <= 0:
            y += 10
        if y >= 550:
            y -= 10
        if x >= 750:
            x -= 10
    if keys[pygame.K_d] and keys[pygame.K_LCTRL]:
        s = 10
        x += s
        if x <= 0:
            x += 10
        if y <= 0:
            y += 10
        if y >= 550:
            y -= 10
        if x >= 750:
            x -= 10
    text = font.render(f"{t}", True, (255, 255, 255))
    text_rect = text.get_rect(center=(width // 2, height // 2))
    screen.blit(text, text_rect)

    # 填充背景色
    screen.fill(white)






    print(f'x = {x},y = {y}')
    pygame.draw.rect(screen, blue, (x, y, 长, 宽))
    # 刷新屏幕
    pygame.display.flip()

    # 控制帧率
    pygame.time.Clock().tick(60)


