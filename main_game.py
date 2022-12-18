import pygame

# Initialize the pygame
pygame.init()

#Create the screen
screen = pygame.display.set_mode((1080, 720))
pygame.display.update()

#Title and Icon Title
pygame.display.set_caption("ESCAPE WITH DS")
icon = pygame.image.load('xxx.png')
pygame.display.set_icon(icon)

#Load Image
tryImg = pygame.image.load('xxx.png').convert()

# Using blit to copy content from one surface to other
screen.blit(tryImg, (0, 0))
 
# paint screen one time
pygame.display.flip()
# status = True
while (True):
 
  # iterate over the list of Event objects
  # that was returned by pygame.event.get() method.
    for i in pygame.event.get():
 
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if i.type == pygame.QUIT:
            status = False
 
# deactivates the pygame library
pygame.display.quit()
pygame.quit()