'''						Recreating the flickers/fireflies that appear for me when im looking at the sky'''
import pygame
import random
import time
import sys



# ----- Set parameters ------------------------ #
screen_size = (800, 600)


# ----- Pygame Init --------------------------- #
pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Sky Fireflies')
display = pygame.Surface(screen_size)

# ----- Import sky image ---------------------- #
sky_img = pygame.image.load('Sky_Gradient.png')

# ----- Variables ----------------------------- #
	# [pos, vel, scale, timer]
fireflies = []


# ----- CODE LOOP --------------------------------------------------------- #
while True:

	# --Reset screen to black each frame
	display.fill((0,0,0))

	# --Display sky image
	display.blit(sky_img, (0, 0))


	# --Handle events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit() 


	# --Fireflies parameteres
		# Position
	pos_x, pos_y = (random.randint(0, screen_size[0]), random.randint(0, screen_size[1]))
		# Velocity
	velocity_x = random.randint(0, 20) / 10 - 1
	velocity_y = random.randint(0, 20) / 10 - 1
		# Scale
	scale = 1
		# Timer
	timer = random.randint(4,6)

	# --Add fireflies/particles
	if len(fireflies) < 70:
		fireflies.append([[pos_x, pos_y], [velocity_x / 2, velocity_y / 2], scale, timer])

	# --Fireflies functionality
	for firefly in fireflies:
		firefly[0][0] += firefly[1][0]
		firefly[0][1] += firefly[1][1]
		firefly[3]    -= 0.03


		# --Draw firefly
		pygame.draw.circle(display, (255,255,255), (firefly[0][0], firefly[0][1]), (firefly[2]) )

		if firefly[3] < 0:
			fireflies.remove(firefly)






	# Blit images to the display and update screen
	screen.blit(display, (0,0))
	pygame.display.update()

