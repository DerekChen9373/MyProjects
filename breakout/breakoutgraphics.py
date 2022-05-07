
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5
BRICK_WIDTH = 40
BRICK_HEIGHT = 15
BRICK_ROWS = 10
BRICK_COLS = 10
BRICK_OFFSET = 50
BALL_RADIUS = 10
PADDLE_WIDTH = 75
PADDLE_HEIGHT = 15
PADDLE_OFFSET = 50
INITIAL_Y_SPEED = 7.0
MAX_X_SPEED = 5

class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.paddle=GRect(PADDLE_WIDTH,PADDLE_HEIGHT,x=self.window.width/2-PADDLE_WIDTH/2,y=self.window.height-PADDLE_OFFSET)
        self.window.add(self.paddle)
        self.paddle.Filled=True
        self.paddle.fill_color="black"
        self.ball=GOval(2*BALL_RADIUS,2*BALL_RADIUS,x=self.window.width/2-BALL_RADIUS,y=self.window.height/2-BALL_RADIUS)
        self.window.add(self.ball)
        self.ball.Filled=True
        self.ball.fill_color="BLACK"
        self.__dy=INITIAL_Y_SPEED
        self.__dx=random.randint(1,MAX_X_SPEED)
        if (random.random() > 0.5):
            self.__dx = -self.__dx
        self.get_started=False
        self.count=0
        onmouseclicked(self.start)
        onmousemoved(self.paddle_move)
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                self.brick=GRect(BRICK_WIDTH,BRICK_HEIGHT,x=j * BRICK_WIDTH+j * BRICK_SPACING,y=BRICK_OFFSET+i * BRICK_HEIGHT+i * BRICK_SPACING)
                self.window.add(self.brick)
                if i == 0 or  i == 1:
                    self.brick.filled=True
                    self.brick.fill_color="red"
                elif i == 2 or  i == 3:
                    self.brick.filled=True
                    self.brick.fill_color="orange"
                elif i == 4 or  i == 5:
                    self.brick.filled=True
                    self.brick.fill_color="yellow"
                elif i == 6 or  i == 7:
                    self.brick.filled=True
                    self.brick.fill_color="green"
                else:
                    self.brick.filled=True
                    self.brick.fill_color="blue"

    def start(self,event):

        self.get_started=True

    def paddle_move(self, event):

        if event.x-PADDLE_WIDTH/2 >0 and event.x+PADDLE_WIDTH/2<self.window.width:
            self.paddle.x=event.x-PADDLE_WIDTH/2
        elif event.x-PADDLE_WIDTH/2<0:
            self.paddle.x=0
        elif event.x+PADDLE_WIDTH/2>self.window.width:
            self.paddle.x=self.window.width-PADDLE_WIDTH

    def get_dx(self):

        return self.__dx

    def get_dy(self):

        return self.__dy

    def rebounce_wall(self):

        if self.ball.x <= 0 or self.ball.x +BALL_RADIUS*2>=self.window.width:
            self.__dx=-self.__dx
        elif self.ball.y <= 0:
            self.__dy=-self.__dy

    def detect_object(self):

        object = self.window.get_object_at(self.ball.x,self.ball.y)
        if object is None:
            object=self.window.get_object_at(self.ball.x+2 * BALL_RADIUS,self.ball.y)
            if object is None:
                object=self.window.get_object_at(self.ball.x,self.ball.y+2 * BALL_RADIUS)
                if object is None:
                    object=self.window.get_object_at(self.ball.x+2 * BALL_RADIUS,self.ball.y+2 * BALL_RADIUS)
                    return None
                return object
            return object
        return object

    def remove(self,object):

        if object==self.paddle:
            if self.__dy>= 0:
                self.__dy=-self.__dy
        if object is not None and object is not self.paddle:
            self.window.remove(object)
            self.__dy=-self.__dy

    def out_of_court(self):
        if self.ball.y+BALL_RADIUS>self.window.height:
            self.ball.x=self.window.width/2-BALL_RADIUS
            self.ball.y=self.window.height/2-BALL_RADIUS
            self.get_started=False
            self.count+=1

    def reset(self):

        self.ball.x = self.window.width / 2 - BALL_RADIUS
        self.ball.y = self.window.height / 2 - BALL_RADIUS

    def still_bricks(self):

        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                brick=self.window.get_object_at(x=j * BRICK_WIDTH + j * BRICK_SPACING, y=BRICK_OFFSET+i * BRICK_HEIGHT+i * BRICK_SPACING)
                if brick is not None:
                    return False
        return True







