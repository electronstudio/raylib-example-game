from enum import IntEnum


class GameScreen(IntEnum):
    UNKNOWN = -1
    LOGO = 0
    TITLE = 1
    OPTIONS = 2
    GAMEPLAY = 3
    ENDING = 4


class BaseScreen:
    def __init__(self):
        self.frames_counter = 0
        self.finish_screen = 0
    
    def init(self):
        self.frames_counter = 0
        self.finish_screen = 0
    
    def update(self):
        pass
    
    def draw(self, width: int, height: int):
        pass
    
    def unload(self):
        pass
    
    def should_finish(self):
        return self.finish_screen