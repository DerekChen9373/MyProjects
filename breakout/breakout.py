
from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120
NUM_LIVES = 3

def main():

    graphics = BreakoutGraphics()
    n=NUM_LIVES
    while True:
        pause(FRAME_RATE)
        if graphics.get_started:
            vx=graphics.get_dx()
            vy=graphics.get_dy()
            graphics.ball.move(vx,vy)
            graphics.rebounce_wall()
            object=graphics.detect_object()
            graphics.remove(object)
            if graphics.still_bricks():
                graphics.reset()
                break
            graphics.out_of_court()
            if graphics.count>0 and n+graphics.count!=NUM_LIVES:
                n-=1
            if n==0 :
                break

if __name__ == '__main__':
    main()
