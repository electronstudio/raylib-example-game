import pyray
from .screens import BaseScreen


class EndingScreen(BaseScreen):
    def __init__(self, font, fx_coin):
        super().__init__()
        self.font = font
        self.fx_coin = fx_coin
    
    def update(self):
        # Press enter or tap to return to TITLE screen
        if pyray.is_key_pressed(pyray.KEY_ENTER) or pyray.is_gesture_detected(pyray.GESTURE_TAP):
            pyray.toggle_borderless_windowed()
            self.finish_screen = 1
            pyray.play_sound(self.fx_coin)
    
    def draw(self, width: int, height: int):
        pyray.draw_rectangle(0, 0, width, height, pyray.BLUE)
        
        pos = pyray.Vector2(20, 10)
        pyray.draw_text_ex(self.font, "ENDING SCREEN", pos, self.font.baseSize * 3.0, 4, pyray.DARKBLUE)
        pyray.draw_text("PRESS ENTER or TAP to RETURN to TITLE SCREEN", 120, 220, 20, pyray.DARKBLUE)