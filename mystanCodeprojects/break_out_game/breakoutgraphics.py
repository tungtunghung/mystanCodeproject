"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Draw bricks
        for x in range(brick_cols):
            for y in range(brick_rows):
                self._brick = GRect(brick_width, brick_height)
                self._brick.filled = True
                if 0 <= y < brick_rows / (brick_rows / 2) * 1:
                    self._brick.fill_color = 'salmon'
                    self._brick.color = 'salmon'
                elif brick_rows / (brick_rows / 2) <= y < brick_rows / (brick_rows / 2) * 2:
                    self._brick.fill_color = 'orange'
                    self._brick.color = 'orange'
                elif brick_rows / (brick_rows / 2) <= y < brick_rows / (brick_rows / 2) * 3:
                    self._brick.fill_color = 'skyblue'
                    self._brick.color = 'skyblue'
                elif brick_rows / (brick_rows / 2) <= y < brick_rows / (brick_rows / 2) * 4:
                    self._brick.fill_color = 'greenyellow'
                    self._brick.color = 'greenyellow'
                elif brick_rows / (brick_rows / 2) <= y < brick_rows / (brick_rows / 2) * 5:
                    self._brick.fill_color = 'limegreen'
                    self._brick.color = 'limegreen'
                else:
                    self._brick.fill_color = 'lightsage'
                    self._brick.color = 'lightsage'
                self.window.add(self._brick, 0 + x * (brick_width + brick_spacing),
                                brick_offset + y * (brick_height + brick_spacing))
        # Create a paddle
        self._paddle = GRect(paddle_width, paddle_height)
        self._paddle.filled = True
        self._paddle.fill_color = 'black'
        self.window.add(self._paddle, (self.window.width-paddle_width)/2, self.window.height-paddle_offset-paddle_height)
        # Center a filled ball in the graphical window
        self._ball = GOval(ball_radius*2, ball_radius*2)
        self._ball.filled = True
        self._ball.fill_color = 'black'
        self.window.add(self._ball, (self.window.width-self._ball.width)/2, (self.window.height-self._ball.height)/2)
        # Default initial velocity for the ball
        self.__dx = random.randrange(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        # Initialize our mouse listeners
        self._ball_move = False
        onmouseclicked(self.ball_start)
        onmousemoved(self.change_paddle_position)
        self._score = 0
        self._touch_paddle = False

    def ball_start(self, m):
        self._ball_move = True

    def brick_collision_happened(self):
        ball_upper_left = self.window.get_object_at(self._ball.x, self._ball.y)
        ball_upper_right = self.window.get_object_at(self._ball.x + BALL_RADIUS * 2, self._ball.y)
        ball_bottom_left = self.window.get_object_at(self._ball.x, self._ball.y + BALL_RADIUS * 2)
        ball_bottom_right = self.window.get_object_at(self._ball.x + BALL_RADIUS * 2, self._ball.y + BALL_RADIUS * 2)
        if ball_bottom_left is not self._paddle and ball_bottom_right is not self._paddle and ball_upper_left is not self._paddle and ball_upper_right is not self._paddle:
            self._touch_paddle = False
            if ball_upper_left is None and ball_upper_right is None and ball_bottom_left is None and ball_bottom_right is None:
                return False
            elif ball_bottom_left is None and ball_bottom_right is None and ball_upper_right is None:
                # When the ball's upper left corner collide with the brick, the brick will be remove
                self.window.remove(ball_upper_left)
                self._score += 1
                return True
            elif ball_bottom_left is None and ball_bottom_right is None and ball_upper_left is None:
                self.window.remove(ball_upper_right)
                self._score += 1
                return True
            elif ball_upper_right is None and ball_upper_left is None and ball_bottom_right is None:
                self.window.remove(ball_bottom_left)
                self._score += 1
                return True
            elif ball_upper_right is None and ball_upper_left is None and ball_bottom_left is None:
                self.window.remove(ball_bottom_right)
                self._score += 1
                return True
            elif ball_bottom_left is None and ball_bottom_right is None:
                self.window.remove(ball_upper_right)
                self._score += 1
                return True
            elif ball_upper_left is None and ball_upper_right is None:
                self.window.remove(ball_bottom_right)
                self._score += 1
                return True
            elif ball_upper_left is None and ball_bottom_left is None:
                self.window.remove(ball_upper_right)
                self._score += 1
                return True
        self._touch_paddle = True
        return False

    def no_brick_left(self):
        for x in range(0, BRICK_COLS * (BRICK_WIDTH + BRICK_SPACING) - BRICK_SPACING, BRICK_WIDTH + BRICK_SPACING):
            for y in range(BRICK_OFFSET, BRICK_OFFSET + (BRICK_ROWS * (BRICK_HEIGHT + BRICK_SPACING) - BRICK_SPACING), BRICK_HEIGHT + BRICK_SPACING):
                # Check whether there is any brick in the window
                maybe_brick = self.window.get_object_at(x, y)
                if maybe_brick is not None and maybe_brick is not self._ball and maybe_brick is not self._paddle:
                    return False
        return True

    def lose_a_life(self):
        if self._ball.y >= self.window.height - self._ball.height:
            # Add a new ball at the center of the window and the ball won't move until the mouse clicks
            self.window.add(self._ball, (self.window.width-self._ball.width)/2, (self.window.height-self._ball.height)/2)
            self._ball_move = False
            return True

    def hit_the_ceiling(self):
        if self._ball.y <= 0:
            return True

    def hit_the_walls(self):
        if self._ball.x <= 0 or self._ball.x >= self.window.width - self._ball.width:
            return True

    def change_paddle_position(self, m):
        if m.x-self._paddle.width/2 <= 0:
            self.window.add(self._paddle, 0, self._paddle.y)
        elif m.x-self._paddle.width/2 >= self.window.width-self._paddle.width:
            self.window.add(self._paddle, self.window.width-self._paddle.width, self._paddle.y)
        else:
            self.window.add(self._paddle, m.x - self._paddle.width / 2, self._paddle.y)

    # getter
    def get_dx(self):
        if random.random() > 0.5:
            self.__dx = -self.__dx
        return self.__dx

    # getter
    def get_dy(self):
        return self.__dy

    @property
    def ball(self):
        return self._ball

    @property
    def ball_move(self):
        return self._ball_move

    @property
    def score(self):
        return self._score

    @property
    def touch_paddle(self):
        return self._touch_paddle


