"""
justwindow.py:
    window を表示するスクリプト
    色を変えたりイベントをいじったり
"""
# window を表示する
import sys
import pygame
from pygame.locals import QUIT

# pygame モジュールの初期化
pygame.init()

# 400*300サイズのウィンドウを作成して定数SURFACEに格納
SURFACE = pygame.display.set_mode((400, 300))
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption('Count Loop')

def main():
    """ main routine """
    sysfont = pygame.font.SysFont(None, 36)
    counter = 0

    while True:
        # オレンジ色で塗りつぶす
        SURFACE.fill((255, 150, 0))

        # "event"とはマウスを動かしたりクリックしたりの動作
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        counter += 1
        count_image = sysfont.render(
            "count is {}".format(counter), True, (255, 255, 255))
        SURFACE.blit(count_image, (50, 50))
        pygame.display.update()

        # 1秒間に10回実行するように休憩時間を調整してくれる
        FPSCLOCK.tick(10)

if __name__ == '__main__':
    main()