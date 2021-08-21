
# window を表示する
import sys
import pygame
# MOUSEBUTTONDOWN: マウスクリック
from pygame.locals import QUIT, MOUSEBUTTONDOWN

# pygame モジュールの初期化
pygame.init()

# 400*300サイズのウィンドウを作成して定数SURFACEに格納
SURFACE = pygame.display.set_mode((400, 300))

# 実行時間の調整
FPSCLOCK = pygame.time.Clock()

def main():
    """ main routine """
    # logo画像の読み込みとサイズ取得
    logo_file = "YDN.png"
    logo = pygame.image.load(logo_file)
    logo_width = logo.get_width()
    logo_hight = logo.get_height()

    mousepos = []

    while True:

        # "event"とはマウスを動かしたりクリックしたりの動作
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mousepos.append(event.pos)

        # 画面をオレンジ色で塗りつぶす
        SURFACE.fill((255, 150, 0))

        # クリックしたところにロゴ表示
        # 左上が(i,j)の位置 [SURFACE.blit(logo, (x,y))]
        for i, j in mousepos:
            SURFACE.blit(logo, (i-logo_width/2,j-logo_hight/2))

        pygame.display.update()
        FPSCLOCK.tick(3)

        
if __name__ == '__main__':
    main()