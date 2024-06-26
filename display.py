import sdl2
import sdl2.ext

class Display():
    def __init__(self, W, H):
        sdl2.ext.init()
        self.W, self.H = W, H
        self.window = sdl2.ext.Window("SLAM", size = (W,H))
        self.window.show()
    
    def paint(self, img):
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                exit(0)
        # draw
        surf = sdl2.ext.pixels3d(self.window.get_surface(), transpose=False)
        surf[:, :, 0:3] = img
        # blit
        self.window.refresh()
