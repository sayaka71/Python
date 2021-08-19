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

        # 赤：四角（塗りつぶし），始点（10, 20），(width, height) = (100, 50)
        pygame.draw.rect(SURFACE, (255,0,0),
            (10, 20, 100,50))

        # 黒：四角（太さ3）
        pygame.draw.rect(SURFACE, (0,0,0),
            (150,20, 100,30), 3)

        # 白矢印作成
        # 白：三角（塗りつぶし）
        pygame.draw.polygon(SURFACE, (255,255,255),
            points=[(150,100), (200,60), (250,100)])
        # 白：四角（塗りつぶし）
        pygame.draw.rect(SURFACE, (255,255,255),
            (170,100, 60,100))

        pygame.display.update()
        FPSCLOCK.tick(3)

if __name__ == '__main__':
    main()