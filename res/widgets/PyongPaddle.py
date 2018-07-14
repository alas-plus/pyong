from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector


class PyongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            speedup = 1.1
            offset = 0.02 * Vector(ball.center_x - self.center_x, ball.center_y - self.center_y)
            ball.velocity = speedup * (offset - ball.velocity)
