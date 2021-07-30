# Includes
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.clock import Clock
from time import strftime, localtime
from kivy.properties import StringProperty
import random


class MyWidget(Widget):
    # Get local time
    random = random.random()
    time = StringProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.loop, 1)

    def loop(self, dt=None):
        self.hour = strftime("%H", localtime())
        if int(self.hour) > 12:
            self.time = strftime(f"{int(self.hour)-12}:%M:%S", localtime())
        else:
            self.time = strftime("%H:%M:%S", localtime())
        print(f"Current time is: {self.time}")
    
    def on_touch_down(self, touch):
        # Draw randomly colored circles at touch position
        with self.canvas:
            Color(random.random(), random.random(), random.random(), 1)
            d = 30
            Rectangle(pos=(touch.x-d/2, touch.y-d/2), size=(d,d))


class MyClockApp(App):

    def build(self):
        return MyWidget()



if __name__ == '__main__':
    MyClockApp().run()
