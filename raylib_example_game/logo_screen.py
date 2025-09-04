import pyray
from .screens import BaseScreen


class LogoScreen(BaseScreen):
    def __init__(self):
        super().__init__()
        self.logo_position_x = 0
        self.logo_position_y = 0
        self.letters_count = 0
        self.top_side_rec_width = 0
        self.left_side_rec_height = 0
        self.bottom_side_rec_width = 0
        self.right_side_rec_height = 0
        self.state = 0
        self.alpha = 1.0
    
    def init(self):
        super().init()
        self.letters_count = 0
        
        self.logo_position_x = pyray.get_screen_width() // 2 - 128
        self.logo_position_y = pyray.get_screen_height() // 2 - 128
        
        self.top_side_rec_width = 16
        self.left_side_rec_height = 16
        self.bottom_side_rec_width = 16
        self.right_side_rec_height = 16
        
        self.state = 0
        self.alpha = 1.0
    
    def update(self):
        if self.state == 0:  # Top-left square corner blink logic
            self.frames_counter += 1
            
            if self.frames_counter == 80:
                self.state = 1
                self.frames_counter = 0  # Reset counter... will be used later...
        
        elif self.state == 1:  # Bars animation logic: top and left
            self.top_side_rec_width += 8
            self.left_side_rec_height += 8
            
            if self.top_side_rec_width == 256:
                self.state = 2
        
        elif self.state == 2:  # Bars animation logic: bottom and right
            self.bottom_side_rec_width += 8
            self.right_side_rec_height += 8
            
            if self.bottom_side_rec_width == 256:
                self.state = 3
        
        elif self.state == 3:  # "raylib" text-write animation logic
            self.frames_counter += 1
            
            if self.letters_count < 10:
                if self.frames_counter // 12:  # Every 12 frames, one more letter!
                    self.letters_count += 1
                    self.frames_counter = 0
            else:  # When all letters have appeared, just fade out everything
                if self.frames_counter > 200:
                    self.alpha -= 0.02
                    
                    if self.alpha <= 0.0:
                        self.alpha = 0.0
                        self.finish_screen = 1  # Jump to next screen
    
    def draw(self, width: int, height: int):
        if self.state == 0:  # Draw blinking top-left square corner
            if (self.frames_counter // 10) % 2:
                pyray.draw_rectangle(self.logo_position_x, self.logo_position_y, 16, 16, pyray.BLACK)
        
        elif self.state == 1:  # Draw bars animation: top and left
            pyray.draw_rectangle(self.logo_position_x, self.logo_position_y, self.top_side_rec_width, 16, pyray.BLACK)
            pyray.draw_rectangle(self.logo_position_x, self.logo_position_y, 16, self.left_side_rec_height, pyray.BLACK)
        
        elif self.state == 2:  # Draw bars animation: bottom and right
            pyray.draw_rectangle(self.logo_position_x, self.logo_position_y, self.top_side_rec_width, 16, pyray.BLACK)
            pyray.draw_rectangle(self.logo_position_x, self.logo_position_y, 16, self.left_side_rec_height, pyray.BLACK)
            
            pyray.draw_rectangle(self.logo_position_x + 240, self.logo_position_y, 16, self.right_side_rec_height, pyray.BLACK)
            pyray.draw_rectangle(self.logo_position_x, self.logo_position_y + 240, self.bottom_side_rec_width, 16, pyray.BLACK)
        
        elif self.state == 3:  # Draw "raylib" text-write animation + "powered by"
            pyray.draw_rectangle(self.logo_position_x, self.logo_position_y, self.top_side_rec_width, 16, pyray.fade(pyray.BLACK, self.alpha))
            pyray.draw_rectangle(self.logo_position_x, self.logo_position_y + 16, 16, self.left_side_rec_height - 32, pyray.fade(pyray.BLACK, self.alpha))
            
            pyray.draw_rectangle(self.logo_position_x + 240, self.logo_position_y + 16, 16, self.right_side_rec_height - 32, pyray.fade(pyray.BLACK, self.alpha))
            pyray.draw_rectangle(self.logo_position_x, self.logo_position_y + 240, self.bottom_side_rec_width, 16, pyray.fade(pyray.BLACK, self.alpha))
            
            pyray.draw_rectangle(pyray.get_screen_width() // 2 - 112, pyray.get_screen_height() // 2 - 112, 224, 224, pyray.fade(pyray.RAYWHITE, self.alpha))
            
            # Draw partial text based on letters_count
            raylib_text = "raylib"
            partial_text = raylib_text[:self.letters_count]
            pyray.draw_text(partial_text, pyray.get_screen_width() // 2 - 44, pyray.get_screen_height() // 2 + 48, 50, pyray.fade(pyray.BLACK, self.alpha))
            
            if self.frames_counter > 20:
                pyray.draw_text("powered by", self.logo_position_x, self.logo_position_y - 27, 20, pyray.fade(pyray.DARKGRAY, self.alpha))