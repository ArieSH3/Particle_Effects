'''			Particle System				'''

import pygame
import sys
import time
import random
from perlin_noise import PerlinNoise



#----- Set Colours --------------------------------------------------------#

WHITE = (255,255,255)
BLACK = (0  ,0  ,0  )
RED   = (150,0  ,0  )
GREEN = (0  ,150,0  )
BLUE  = (0  ,0  ,150)
YELLOW= (230,150,0  )


#----- Set Parameters -----------------------------------------------------#

FPS = 60
	# Aspect ratio 4:3
WIN_W = 800
WIN_H = 600



#----- Init pygame and dependencies ---------------------------------------#

pygame.init()
screen = pygame.display.set_mode((WIN_W, WIN_H), 0, 32)
pygame.display.set_caption('Particle Effect')
my_font = pygame.font.SysFont('impact', 30)
clock = pygame.time.Clock()

#----- Init variables -----------------------------------------------------#

	# [pos, vel, timer, size, colour]
particles = []
pnoise = PerlinNoise(octaves = 10, seed = 1)
mb_pressed = False


#----- MAIN LOOP ----------------------------------------------------------#

while True:
	
	# -- Set screen colour
	screen.fill(WHITE)

	# -- Set particle colour
	pt_colour = BLACK
	
	# -- Set FPS
	clock.tick(FPS)

	# -- Particle variables:
	
		# -- Mouse pos
	mouse_x, mouse_y = pygame.mouse.get_pos()

		# -- Velocity
	velocity_x = random.randint(0, 20) / 10 - 1
	velocity_y = 0

		# -- Timer
	timer = random.randint(4,6)

		# -- Particle size
	pt_size = random.randint(1,3)

	# Check of mb pressed and resize the particles for the duration of the click
	if mb_pressed:
		pt_size = random.randint(3,6)
		timer = random.randint(5,7)
		pt_colour = RED



	# -- Handle keys/input
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			mb_pressed = True

		if event.type == pygame.MOUSEBUTTONUP:
			mb_pressed = False


	
	# -- Add particles
	particles.append([[mouse_x, mouse_y], [velocity_x, velocity_y], timer, pt_size, pt_colour])

	# -- Particle functionality:
	for particle in particles:
		particle[0][0] += particle[1][0]
		particle[0][1] += particle[1][1]
		particle[2]    -= 0.1
		particle[1][1] -= 0.1
		particle[3]    -= 0.05

		# -- Draw particles															 #2
		pygame.draw.circle(screen, particle[4], (particle[0][0], particle[0][1]), particle[3])

		# -- Remove particles
		if particle[2] <= 0:
			particles.remove(particle)






	pygame.display.update()
