import pyray

def main():
    screen_width = 800
    screen_height = 450

    pyray.init_window(screen_width, screen_height, "Raylib Example Game")
    pyray.set_target_fps(60)

    while not pyray.window_should_close():
        pyray.begin_drawing()
        pyray.clear_background(pyray.RAYWHITE)
        pyray.draw_text("Hello, Raylib!", 280, 200, 20, pyray.DARKGRAY)
        pyray.end_drawing()

    pyray.close_window()


if __name__ == "__main__":
    main()
