import pygame
from pygame import Rect

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

class dialogBox:
  width = 600
  height = 400

  def __init__(self, x, y, text):
    self.x= x
    self.y = y
    self.text = text

  def draw_dialog(self):
    box = Rect(self.x, self.y, self.width, self.height)
    # insert text
    text_btn = textfont.render(self.text, 1, (0, 0, 0))
    text_len = text_btn.get_width()
    screen.blit(text_btn, ((self.x + int(self.width/2) - int(text_len / 2), self.y + 5)))

     
     

class Button:
    click_btn = (188, 255, 71)
    hover_btn = (224, 252, 164)
    btn = (255,255,255)
    width = 280
    height = 40

    def __init__(self, x, y, text):
       self.x = x 
       self.y = y
       self.text = text

    def draw_btn(self):
      global is_clicked
      action = False

      pos = pygame.mouse.get_pos()

      btn_rect = Rect(self.x, self.y, self.width, self.height)

      if btn_rect.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1:
          is_clicked = True
          pygame.draw.rect(screen, self.click_btn, btn_rect)
        else : 
          is_clicked = False
          pygame.draw.rect(screen, self.hover_btn, btn_rect)
      else : 
        pygame.draw.rect(screen, self.btn, btn_rect)

      # insert text
      text_btn = textfont.render(self.text, 1, (0, 0, 0))
      text_len = text_btn.get_width()
      screen.blit(text_btn, ((self.x + int(self.width/2) - int(text_len / 2), self.y + 5)))
      return action


load_bg = pygame.image.load("creepy-river.png")
# load_bg = pygame.transform.scale(bg,(509,339))


# paint screen one time
pygame.display.flip()
status = True

start = True
toChoose = False


while (status):
   screen.fill((0,0,0))
        #bgm here

    #starting position
   if start == True:
    #load narasi awal

        screen.blit(load_bg, (300, 300))
   for i in pygame.event.get():
        if i.type == pygame.QUIT:
          status = False

        if i.type == pygame.MOUSEBUTTONDOWN:
            is_clicked = True
            #load sfx click
            pygame.mixer.music.load("click.wav")
            pygame.mixer.music.play()
            #check 


   if toChoose == True:
        if 
        # check if node = none (end)

        # else load text

       
        # then quitting the pygame
        # and program both.

        text = textfont.render("Is this working?", 1, (255,255,255))
        screen.blit(text, (300,300))
        pygame.display.update()

 
# deactivates the pygame library
pygame.display.quit()
pygame.quit()