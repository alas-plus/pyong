from random import randint

from kivy.app import App
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector

from res.widgets.pyongball import PyongBall


class PyongGame(Widget):
    pyong_ball = ObjectProperty(None)

    def serve_ball(self):
        self.pyong_ball.center = self.center
        self.pyong_ball.velocity = Vector(4, 0).rotate(randint(0, 360))

    def update(self, dt):
        self.pyong_ball.move()

        # bounce off top and bottom
        if (self.pyong_ball.y < 0) or (self.pyong_ball.top > self.height):
            self.pyong_ball.velocity_y *= -1

        # bounce off left and right
        if (self.pyong_ball.x < 0) or (self.pyong_ball.right > self.width):
            self.pyong_ball.velocity_x *= -1


class PyongApp(App):
    def build(self):
        pyong_game = PyongGame()
        pyong_game.serve_ball()
        Clock.schedule_interval(pyong_game.update, 1.0 / 60.0)
        return pyong_game


if __name__ == '__main__':
    PyongApp().run()
