
# window を表示する
import sys
import pygame
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

            elif event.type == MOUSEBUTTONDOWN:
                mousedwon = True
                mousepos.append((event.pos))
                print('down')

            elif event.type == MOUSEMOTION:
                if mousedown:
                    mousepos.append((event.pos))
                    print('motion')

            elif event.type == MOUSEBUTTONUP:
                mousedown = False
                # mousepos.clear()
                mousepos.append((event.pos))
                print('up')

        # 画面をオレンジ色で塗りつぶす
        SURFACE.fill((255, 150, 0))

        if len(mousepos) > 1:
            pygame.draw.lines(SURFACE, (0,0,255), False, mousepos)

        pygame.display.update()
        FPSCLOCK.tick(10)

        
if __name__ == '__main__':
    main()