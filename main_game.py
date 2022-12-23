import pygame
import tree
import os

class Button:
    # Button class
    def __init__(self, x, y, font: pygame.font.Font, text, width=160, height=90, on_click=lambda: None):
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = (x, y)
        
        self.text = font.render(text, 1, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (x, y)
        self.rect = self.text_rect.inflate(20, 20)
        self.rect.center = self.text_rect.center
        
        self.idle_color = (255, 255, 255)
        self.clicked_color = (127, 127, 127)
        self.is_clicked = False
        self.on_click = on_click
    
    def draw_btn(self, surface: pygame.Surface):
        if self.is_clicked:
            pygame.draw.rect(surface, self.clicked_color, self.rect)
        else:
            pygame.draw.rect(surface, self.idle_color, self.rect)
        surface.blit(self.text, self.text_rect)

    def click(self):
        self.is_clicked = not self.is_clicked
        self.on_click()
    
    def unclick(self):
        self.is_clicked = False

class Charas:
    def __init__(self, path):
        self.image = pygame.image.load(path)
    
    def draw(self, surface: pygame.Surface, x: int, y: int):
        surface.blit(self.image, (x, y))

class Game:
    pygame.init()
    pygame.mixer.init()
    width = 1280
    height = 720
    center = (width // 2, height // 2)
    dialog = tree.dialogueTree.root
    path = os.path.dirname(__file__)
    font = pygame.font.SysFont("monospace", 30)
    

    def __init__(self):
        self.screen = pygame.display.set_mode((self.width, self.height))

        #set icon & caption app
        pygame.display.set_caption("ESCAPE WITH DS")
        icon = pygame.image.load("ds-icon.png")
        pygame.display.set_icon(icon)
        
        self.counter = 0
        # self.setBGM(self.path + "/Audio Asset/Eerie_BGM.mp3")
        self.buttons: list[Button] = []
        self.sprites: list[Charas] = []
        self.load_dialog()
    
    def draw_text(self, text, color=(255, 255, 255)):
        text = self.font.render(text, 1, color)
        text_rect = text.get_rect()
        text_box = text_rect.inflate(70, 70)
        text_box.centerx = self.width // 2
        text_box.bottom = self.height
        text_rect.center = text_box.center
        pygame.draw.rect(self.screen, pygame.Color(127, 127, 127), text_box)
        self.screen.blit(text, text_rect)
    
    def setBGM(self, audio):
        pygame.mixer.music.load(audio)
        pygame.mixer.music.play(-1)
    
    def load_dialog(self):
        self.charas = []
        self.narasi = self.dialog.text
        for path in self.dialog.asset:
            if "Background" in path:
                self.background = pygame.image.load(path)
            else:
                self.charas.append(Charas(path))

    def click_down(self):
        # self.click_sound.play()
        if self.buttons:
            pos = pygame.mouse.get_pos()
            if self.buttons[0].rect.collidepoint(pos):
                self.buttons[0].click()
                self.dialog = self.dialog.left
            if self.buttons[1].rect.collidepoint(pos):
                self.buttons[1].click()
                self.dialog = self.dialog.right
        else:
            self.counter += 1
            if self.counter >= len(self.narasi):
                self.create_choices()
    
    def click_up(self):
        for button in self.buttons:
            if button.is_clicked:
                button.unclick()
                self.load_dialog()
                self.counter = 0
                self.buttons = []
                break

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.click_down()
                if self.dialog == None:
                    return False
            elif event.type == pygame.MOUSEBUTTONUP:
                self.click_up()
        return True
    
    def create_choices(self):
        if any(self.dialog.choice):
            left = Button(self.width * 1 // 4, self.height // 2, self.font, self.dialog.choice[0])
            right = Button(self.width * 3 // 4, self.height // 2, self.font, self.dialog.choice[1])
            self.buttons = [left, right]
        else:
            self.dialog = None

    def main(self):
        status = True
        while status:
            pygame.time.Clock().tick(60)

            self.screen.fill((0, 0, 0)) # clear screen
            self.screen.blit(self.background, (0, 0))   # renders background
            for i, chara in enumerate(self.charas):
                chara.draw(self.screen, self.width * i // len(self.charas), self.height // 3)
            if self.buttons:
            # renders buttons if on a choice screen
                [button.draw_btn(self.screen) for button in self.buttons]
            else:
            # renders narration
                self.draw_text(self.narasi[self.counter])
            pygame.display.update()
            status = self.event()
        pygame.display.quit()
        pygame.quit()

Game().main()
