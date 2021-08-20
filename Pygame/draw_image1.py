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

def main(logo_file="YDN.png"):
    """ main routine """
    logo = pygame.image.load(logo_file)

    while True:

        # "event"とはマウスを動かしたりクリックしたりの動作
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 画面をオレンジ色で塗りつぶす
        SURFACE.fill((255, 150, 0))

        # 左上が(x,y)の位置にロゴを描画
        x,y = 20,50
        SURFACE.blit(logo, (x,y))

        pygame.display.update()
        FPSCLOCK.tick(3)

        
if __name__ == '__main__':
    main()