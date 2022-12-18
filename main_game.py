import pygame

# Initialize the pygame
pygame.init()

#Create the screen
s_width = 1080
s_height = 720
screen = pygame.display.set_mode((1080, 720))
pygame.display.update()

#Title and Icon Title
pygame.display.set_caption("ESCAPE WITH DS")
icon = pygame.image.load('ds scratch 2.png')
pygame.display.set_icon(icon)

# #Load Image
# tryImg = pygame.image.load('xxx.png').convert()

# Font
textfont = pygame.font.SysFont  ("monospace", 50)
class textBox:
  def draw_text(self, text):
    text_show = textfont.render(text, 1, (255,255,255))
    text_rect = text_show.get_rect()
    text_rect.center = (s_width / 2, s_height / 2)

    #show text
    screen.blit(text_show, text_rect)
 
class setBG:
  def __init__(self, background) :
      bg = pygame.image.load(background)
      screen.blit(bg,(0,0))

pygame.mixer.init()
class setBGM:
  def __init__(self, audio) :
     #load
     pygame.mixer.music.load(audio)
     #set repeat
     pygame.mixer.music.play(-1)


# class Button:



bg = pygame.image.load("creepy-river.png")
load_bg = pygame.transform.scale(bg,(509,339))


# paint screen one time
pygame.display.flip()
status = True

while (status):
  # iterate over the list of Event objects
  # that was returned by pygame.event.get() method.
    for i in pygame.event.get():
        # if event object type is QUIT
        screen.fill((0,0,0))
        screen.blit(load_bg, (s_width / 2, s_height / 2 ))
        # then quitting the pygame
        # and program both.
        if i.type == pygame.QUIT:
            status = False

    text = textfont.render("Is this working?", 1, (255,255,255))
    screen.blit(text, (300,300))
    pygame.display.update()

 
# deactivates the pygame library
pygame.display.quit()
pygame.quit()