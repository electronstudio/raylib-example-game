import sys
import platform
import pyray


class Game:
    def __init__(self, width: int = 800, height: int = 450, title: str = "Raylib Example Game"):
        self.screen_width = width
        self.screen_height = height
        self.title = title
        
        # Print Python version info
        python_impl = platform.python_implementation()
        python_version = sys.version.split()[0]
        print(f"Running on {python_impl} {python_version}")
        print(f"Full version: {sys.version}")
    
    def run(self):
        pyray.init_window(self.screen_width, self.screen_height, self.title)
        pyray.set_target_fps(60)

        while not pyray.window_should_close():
            self._update()
            self._draw()

        pyray.close_window()
    
    def _update(self):
        pass
    
    def _draw(self):
        pyray.begin_drawing()
        pyray.clear_background(pyray.RAYWHITE)
        pyray.draw_text("Hello, Raylib!", 280, 200, 20, pyray.DARKGRAY)
        pyray.end_drawing()