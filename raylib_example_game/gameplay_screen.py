import random
import pyray
from .screens import BaseScreen

MAX_BUNNIES      =  500000

class Bunny:
    def __init__(self):
        self.position_x = 0.0
        self.position_y = 0.0
        self.speed_x = 0.0
        self.speed_y = 0.0
        self.color_r = 0
        self.color_g = 0
        self.color_b = 0
        self.color_a = 0


class GameplayScreen(BaseScreen):
    def __init__(self, font, fx_coin, wabbit_texture):
        super().__init__()
        self.font = font
        self.fx_coin = fx_coin

        self.texBunny = wabbit_texture
        self.bunnies = []
        for i in range(0, MAX_BUNNIES):
            self.bunnies.append(Bunny())
            self.bunniesCount = 0


    def update(self):
        # Press enter or tap to change to ENDING screen
        if pyray.is_key_pressed(pyray.KEY_ENTER) or pyray.is_gesture_detected(pyray.GESTURE_TAP):
            self.finish_screen = 1
            pyray.play_sound(self.fx_coin)

        for i in range(100):
            if self.bunniesCount < MAX_BUNNIES:
                self.bunnies[self.bunniesCount].position_x = self.width/2
                self.bunnies[self.bunniesCount].position_y = self.height/2
                self.bunnies[self.bunniesCount].speed_x = random.randint(-250, 250)/60.0
                self.bunnies[self.bunniesCount].speed_y = random.randint(-250, 250)/60.0
                self.bunnies[self.bunniesCount].color_r = random.randint(50,240)
                self.bunnies[self.bunniesCount].color_g = random.randint(80, 240)
                self.bunnies[self.bunniesCount].color_b = random.randint(100, 240)
                self.bunnies[self.bunniesCount].color_a = 255
                self.bunniesCount+=1

        for i in range(0, self.bunniesCount):
            self.bunnies[i].position_x += self.bunnies[i].speed_x
            self.bunnies[i].position_y += self.bunnies[i].speed_y

            if ((self.bunnies[i].position_x + self.texBunny.width/2) > self.width) or ((self.bunnies[i].position_x + self.texBunny.width/2) < 0):
                self.bunnies[i].speed_x *= -1
            if ((self.bunnies[i].position_y + self.texBunny.height/2) > self.height) or ((self.bunnies[i].position_y + self.texBunny.height/2 - 40) < 0):
                self.bunnies[i].speed_y *= -1



    def draw(self, width: int, height: int):
        self.width = width
        self.height = height
        pyray.draw_rectangle(0, 0, width, height, pyray.PURPLE)

        for i in range(0, self.bunniesCount):
            pyray.draw_texture(self.texBunny, int(self.bunnies[i].position_x), int(self.bunnies[i].position_y), (self.bunnies[i].color_r,self.bunnies[i].color_g,self.bunnies[i].color_b,self.bunnies[i].color_a))

        pyray.draw_rectangle(0, 0, width, 40, pyray.BLACK)
        pyray.draw_text(f"bunnies {self.bunniesCount}", 120, 10, 20, pyray.GREEN)

        pos = pyray.Vector2(20, 40)
        pyray.draw_text_ex(self.font, f"GAMEPLAY SCREEN {width} {height}", pos, self.font.baseSize * 3.0, 4, pyray.MAROON)
        pyray.draw_text("PRESS ENTER or TAP to JUMP to ENDING SCREEN", 130, 220, 20, pyray.MAROON)