
# window を表示する
import sys
import pygame
from math import sin, cos, radians
# MOUSEBUTTONDOWN: マウスクリック
from pygame.locals import QUIT,MOUSEBUTTONDOWN,MOUSEMOTION, MOUSEBUTTONUP

# pygame モジュールの初期化
pygame.init()

# 400*300サイズのウィンドウを作成して定数SURFACEに格納
SURFACE = pygame.display.set_mode((400, 300))

# 実行時間の調整
FPSCLOCK = pygame.time.Clock()

def main():
    """ main routine """
    mousepos = []
    mousedown = False

    while True:

        # "event"とはマウスを動かしたりクリックしたりの動作
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 画面をオレンジ色で塗りつぶす
        SURFACE.fill((255, 150, 0))

        pointlist0, pointlist1 = [], []

        # 星を描く。144度ずつまわすと星になる。
        for theta in range(0, 720, 144):
            rad = radians(theta)
            pointlist0.append((cos(rad)*100 + 100,sin(rad)*100 + 150))
            pointlist1.append((cos(rad)*100 + 300,sin(rad)*100 + 150))

        pygame.draw.lines(SURFACE, (255,255,255), True, pointlist0, 5)
        pygame.draw.aalines(SURFACE, (255,255,255), True, pointlist1)
            


        pygame.display.update()
        FPSCLOCK.tick(10)

        
if __name__ == '__main__':
    main()