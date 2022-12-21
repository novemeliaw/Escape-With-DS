import pygame
import tree as tr
from pygame import Rect
import os #for path

class Button:
    def __init__(self, x, y, text, font:pygame.font.Font, width = 160, height= 90, on_click = None):
       self.rect = pygame.Rect(0,0,width,height)
       self.rect.center = (x,y)

       self.text = font.render(text, 1, (0,0,0))
       self.text_rect = self.text.get_rect()
       self.text_rect.center = (x,y)
       #set rect size & center
       self.rect = self.text_rect.inflate(20,20)
       self.rect.center = self.text_rect.center

       #clicky stuff
       self.hover_clr =(224, 252, 164)
       self.clicked_clr = (188, 255, 71)
       self.is_clicked = False
       self.on_click = on_click

    def draw_btn(self, surf: pygame.Surface):
      if self.is_clicked == True :
        pygame.draw.rect(surf, self.clicked_clr, self.rect)
      else:
        pygame.draw.rect(surf, self.hover_clr, self.rect)
      surf.blit(self.text, self.text_rect)

    def click(self):
      self.is_clicked = not self.is_clicked
      self.on_click()

    def notClick(self):
      self.is_clicked = False

class Charas:
      def __init__(self, path):
         self.image = pygame.image.load(path)

      def draw_charas(self, surf: pygame.Surface, x:int, y:int):
          surf.blit(self.image, (x,y))

#main game
class Game:
  pygame.init()
  pygame.mixer.init()

  #set screen
  s_width = 1280
  s_height = 720
  center = (s_width // 2, s_height // 2)

  tree = tr.dialogueTree.root
  path = os.path.dirname(__file__)
  font = pygame.font.SysFont("monospace", 30)

  def __init__(self) :
     self.screen = pygame.display.set_mode((self.s_width, self.s_height))

     #Title & Icon
     pygame.display.set_caption("ESCAPE WITH DS")
     icon = pygame.image.load('ds-icon.png')
     pygame.display.set_icon(icon)

     self.counter = 0

     self.btns: list[Button] = []
     self.charas : list[Charas] = []
     self.load_dialog()

  def draw_text(self, text):
    text = self.font.render(text,1,(255, 255, 255))
    text_rect = text.get_rect()
    text_box = text.rect.inflate(70,70)
    text_box.center = self.s_width // 2
    text_box.bottom = self.s_height
    text_rect.center = text_box.center
    pygame.draw.rect(self.screen, pygame.Color(127, 127, 127), text_box)
    self.screen.blit(text, text_rect)

  def setBGM(self, audio):
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play(-1)

  def load_dialog(self):
    self.charas = []
    self.narasi = self.tree.text

    for path in self.tree.asset:
      #check if bg & set bg
      if "Background" in path :
        self.bg = pygame.image.load(path)
      else:
        #set as chara
        self.charas.append(Charas(path))

  #check clicked
  def click_down(self):
    if self.btns == True:
      pos = pygame.mouse.get_pos()
      if self.btns[0].rect.collidepoint(pos):
        self.btns[0].click()
        self.tree = self.tree.left
      if self.btns[1].rect.collidepoint(pos):
        self.btns[1].click()
        self.tree = self.tree.right

  def click_up(self):
    for i in self.btns:
      if i.is_clicked:
        i.notClick()
        self.load_dialog()
        self.counter = 0
        self.btns = []
        break
  
  #pygame event
  def event(self):
    for i in pygame.event.get():
      if i.type == pygame.QUIT:
        return False

      elif i.type == pygame.MOUSEBUTTONDOWN:
        self.click_down()
        if self.tree == None:
          return False

      elif i.type == pygame.MOUSEBUTTONUP:
        self.click_up()

    return True

  def choices_btn(self):
    if any(self.tree.choice):
      left = Button(self.s_width*1 // 4, self.s_height // 2, self.font, self.tree.choice[0])
      right = Button(self.s_width*3 // 4, self.s_height // 2, self.font, self.tree.choice[1])
      self.btns = [left,right]
    else:
      self.tree = None

  def render_scrn(self):
      self.screen.fill((0,0,0))
      self.screen.blit(self.bg, (0,0))

      for i, chara in enumerate(self.charas):
        chara.draw_charas(self.screen, self.s_width * i // len(self.charas), self.s_height // 3)
        if self.btns:
          [btn.draw(self.screen) for btn in self.btns]
        else:
          #narration
          self.draw_text(self.narasi[self.counter])
      pygame.display.update()

  #render screen etc
  def main(self):
    status = True
    while status:
      pygame.time.Clock().tick(60)

      self.render_scrn()
      status = self.event()

    #end game
    pygame.display.quit()
    pygame.quit()


Game().main()
