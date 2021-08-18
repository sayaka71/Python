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
pygame.display.set_caption('Just Window')

def main():
    """ main routine """
    while True:
        # オレンジ色で塗りつぶす
        SURFACE.fill((255, 150, 0))

        # "event"とはマウスを動かしたりクリックしたりの動作
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

if __name__ == '__main__':
    main()