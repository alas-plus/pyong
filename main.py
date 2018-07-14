from kivy.app import App
from kivy.uix.widget import Widget


class PyongGame(Widget):
    pass


class PyongApp(App):
    def build(self):
        return PyongGame()


if __name__ == '__main__':
    PyongApp().run()
