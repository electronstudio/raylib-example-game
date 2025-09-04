import pyray

from .screens import BaseScreen


class TitleScreen(BaseScreen):
    def __init__(self, font, fx_coin):
        super().__init__()
        self.font = font
        self.fx_coin = fx_coin
    
    def update(self):
        # Press enter or tap to change to GAMEPLAY screen
        if pyray.is_key_pressed(pyray.KEY_ENTER) or pyray.is_gesture_detected(pyray.GESTURE_TAP):
            pyray.toggle_borderless_windowed()
            # finishScreen = 1   # OPTIONS
            self.finish_screen = 2  # GAMEPLAY
            pyray.play_sound(self.fx_coin)
    
    def draw(self, width: int, height: int):
        pyray.draw_rectangle(0, 0, width, height, pyray.GREEN)
        pos = pyray.Vector2(20, 10)
        pyray.draw_text_ex(self.font, "TITLE SCREEN", pos, self.font.baseSize * 3.0, 4, pyray.DARKGREEN)
        pyray.draw_text("PRESS ENTER or TAP to JUMP to GAMEPLAY SCREEN", 120, 220, 20, pyray.DARKGREEN)