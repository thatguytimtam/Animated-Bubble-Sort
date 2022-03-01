from pickle import TRUE
import pygame
import time
#### PYGAME AND WINDOW INIT. ####
pygame.init()
pygame.font.init()
winWidth, WinHeight = 800, 500

win = pygame.display.set_mode((winWidth, WinHeight))
pygame.display.set_caption('Animated Bubble Sort')
clock = pygame.time.Clock()
#font = pygame.font.Font('assets/fonts/Market_Deco.ttf', 36)
#### PYGAME AND WINDOW INIT. ####

L = [82, 74, 56, 35, 34, 9, 20, 291, 31, 200, 400, 210, 220, 135, 123, 315, 242, 351, 100]

'''
print(L)
for i in range(len(L) - 1):
	for j in range(0, len(L) - i - 1):
		if L[j] > L[j + 1]:
			L[j], L[j+1], = L[j+1], L[j]

'''

current_x = 30
spawned = False
sorted = False

k = 1
a = 1

WHITE = (255, 255, 255)

while True:
	win.fill((0,0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

	for i in L:
		
		pygame.draw.rect(win, WHITE, pygame.Rect(current_x, WinHeight - i, winWidth/len(L), i*10))
		current_x += winWidth/len(L)
	
	#for i in range(len(L) - 1):
	for j in range(0, len(L) - k):
		if L[j] > L[j + 1]:
			L[j], L[j+1], = L[j+1], L[j]
		
	
	if all(L[i] <= L[i+1] for i in range(len(L) - 1)):
		WHITE = (0,255,0)

	if k <= len(L) + 1:
		k += 1


	current_x = 0

	
	pygame.display.update()
	clock.tick(4)