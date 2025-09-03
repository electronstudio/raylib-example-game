import pyray
from .screens import BaseScreen


class GameplayScreen(BaseScreen):
    def __init__(self, font, fx_coin):
        super().__init__()
        self.font = font
        self.fx_coin = fx_coin
    
    def update(self):
        # Press enter or tap to change to ENDING screen
        if pyray.is_key_pressed(pyray.KEY_ENTER) or pyray.is_gesture_detected(pyray.GESTURE_TAP):
            self.finish_screen = 1
            pyray.play_sound(self.fx_coin)
    
    def draw(self):
        pyray.draw_rectangle(0, 0, pyray.get_screen_width(), pyray.get_screen_height(), pyray.PURPLE)
        pos = pyray.Vector2(20, 10)
        pyray.draw_text_ex(self.font, "GAMEPLAY SCREEN", pos, self.font.baseSize * 3.0, 4, pyray.MAROON)
        pyray.draw_text("PRESS ENTER or TAP to JUMP to ENDING SCREEN", 130, 220, 20, pyray.MAROON)