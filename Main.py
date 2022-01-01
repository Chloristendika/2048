'''
Author: Chloris
2048 Pygame Controllor
Last Updated: 2021-12-31
'''

import pygame
from pygame.locals import *
import MainScript as MC
import sys

# -- start --
# image loader
image_blank = pygame.image.load("resources/blank.png")
image_num_2 = pygame.image.load("resources/num_2.png")
image_num_4 = pygame.image.load("resources/num_4.png")
image_num_8 = pygame.image.load("resources/num_8.png")
image_num_16 = pygame.image.load("resources/num_16.png")
image_num_32 = pygame.image.load("resources/num_32.png")
image_num_64 = pygame.image.load("resources/num_64.png")

dic = { '0': image_blank,
        '2': image_num_2,
        '4': image_num_4,
        '8': image_num_8,
        '16': image_num_16, 
        '32': image_num_32,
        '64': image_num_64,
}
# -- end --

def BLITPIC():
	screen = pygame.display.set_mode((400, 400))

	for i in range(4):
		for j in range(4):

			screen.blit(dic[str(MC.Board[i][j].value)], (95 * j + 10, 95 * i + 10))

	return screen


def main():
	pygame.init()
	pygame.display.set_caption("2048Demo")
	MC.RandGenerate(); MC.UpdateHash()
	screen = BLITPIC()
	while True:
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == pygame.K_RIGHT:
					MC.Move('D')
					MC.RandGenerate(); MC.UpdateHash()
					screen = BLITPIC()
				if event.key == pygame.K_LEFT:
					MC.Move('A')
					MC.RandGenerate(); MC.UpdateHash()
					screen = BLITPIC()
				if event.key == pygame.K_DOWN:
					MC.Move('S')
					MC.RandGenerate(); MC.UpdateHash()
					screen = BLITPIC()
				if event.key == pygame.K_UP:
					MC.Move('W')
					MC.RandGenerate(); MC.UpdateHash()
					screen = BLITPIC()

		pygame.display.flip()


if __name__ == '__main__':
	main()