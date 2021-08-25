"""
Cave: シンプルな横スクロールゲーム。スペースキーを押すと上方向に加速度が上がる
洞窟は徐々に狭くなっていく。
"""
import sys
from random import randint
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE

# 初期化
pygame.init()