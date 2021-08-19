"""
justwindow.py:
    window を表示するスクリプト
    色を変えたりイベントを学ぶ
"""
# window を表示する
import sys
import pygame
from pygame.locals import QUIT

# pygame モジュールの初期化
pygame.init()

# 400*300サイズのウィンドウを作成して定数SURFACEに格納
SURFACE = pygame.display.set_mode((400, 300))
# 実行時間の調整
FPSCLOCK = pygame.time.Clock()

def main():
    """ main routine """

    while True:

        # "event"とはマウスを動かしたりクリックしたりの動作
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 画面をオレンジ色で塗りつぶす
        SURFACE.fill((255, 150, 0))

        # 格子を作る
        # 黒：縦線
        for x_position in range(0,400,25):
            pygame.draw.line(SURFACE, (0,0,0),
                (x_position, 0), (x_position, 300))
        # 黒：横線
        for y_position in range(0,300,25):
            pygame.draw.line(SURFACE, (0,0,0),
                (0, y_position), (400, y_position))

        pygame.display.update()
        FPSCLOCK.tick(3)

        
if __name__ == '__main__':
    main()