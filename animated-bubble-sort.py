from pickle import TRUE
import pygame
import random
#### PYGAME AND WINDOW INIT. ####
pygame.init()
pygame.font.init()
winWidth, WinHeight = 800, 500
win = pygame.display.set_mode((winWidth, WinHeight))
pygame.display.set_caption('Animated Bubble Sort')
clock = pygame.time.Clock()
#font = pygame.font.Font('assets/fonts/Market_Deco.ttf', 36)
#### PYGAME AND WINDOW INIT. ####
L = []
for i in range(500):
	L.append(random.randint(1, 1000))
L.reverse()
current_x = 0
spawned = False
sorted = False
k = 1
comparisons = 0
WHITE = (255, 255, 255)
while True:
	win.fill((0,0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
	for i in L: # (i/max(L))*WinHeight)
		pygame.draw.rect(win, WHITE, pygame.Rect(current_x, WinHeight - (i/max(L))*WinHeight, winWidth/len(L), (i/max(L))*WinHeight))
		current_x += winWidth/len(L)
	for j in range(0, len(L) - k):
		if L[j] > L[j + 1]:
			comparisons += 1
			L[j], L[j+1], = L[j+1], L[j]
	if all(L[i] <= L[i+1] for i in range(len(L) - 1)):
		WHITE = (0,255,0)
	if k <= len(L) + 1:
		k += 1
	current_x = 0

	print(f'Comparisons: {comparisons}')
	pygame.display.update()
	clock.tick(120)