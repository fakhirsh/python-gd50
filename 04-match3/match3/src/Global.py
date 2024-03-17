
class Global:
    # Actual window dimensions
    WINDOW_WIDTH = 1280
    WINDOW_HEIGHT = 720
    # WINDOW_WIDTH = 800
    # WINDOW_HEIGHT = 450

    # Virtual resolution dimensions
    VIRTUAL_WIDTH = 512
    VIRTUAL_HEIGHT = 288

    # Desired framerate
    FPS = 60

    assets = {}

    # The virtual screen is a smaller screen that we draw everything on
    virtual_screen = None
    # The state manager is responsible for managing different game states
    stateManager = None

    # The speed at which the background texture will scroll
    BACKGROUND_SCROLL_SPEED = 80