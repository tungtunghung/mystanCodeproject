"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 2000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    graphics = BreakoutGraphics()
    dx = graphics.get_dx()
    dy = graphics.get_dy()
    # Add animation loop here!
    num_lives = NUM_LIVES
    while True:
        if num_lives <= 0 or graphics.no_brick_left():
            break
        if graphics.ball_move:  # The ball will start to move after mouse clicked
            # update
            graphics.ball.move(dx, dy)
            # check
            if graphics.hit_the_walls():
                dx = -dx
            if graphics.hit_the_ceiling():
                dy = -dy
            if graphics.touch_paddle and dy > 0:  # To avoid the ball bouncing repeatedly on the paddle
                dx = graphics.get_dx()  # To change the dx every collision happened
                dy = -dy
            if graphics.brick_collision_happened():
                dx = graphics.get_dx()  # To change the dx every collision happened
                dy = -dy
            if graphics.lose_a_life():
                num_lives -= 1
        # pause
        pause(FRAME_RATE)




if __name__ == '__main__':
    main()
