
from pynput import mouse
from Timer import RepeatingTimer


class MouseInfo:
    def __init__(self):
        self._right_press = False
        self._right_click_count = 0

    def rclick(self):
        self._right_press = False
        self._right_click_count += 1

    def right_down(self):
        self._right_press = True

    def right_up(self):
        self._right_press = False
        self._right_click_count += 1

    def reset(self):
        self._right_click_count = 0

    def runable(self):
        return self._right_press or self._right_click_count > 0


class Job:
    def __init__(self, skills, interval_sec=0.2):
        self._skills = skills
        self._mouse_info: MouseInfo = MouseInfo()
        self._interval_sec = interval_sec

    def run(self):
        mi = self._mouse_info
        skills = self._skills
        if mi.runable():
            for skill in skills:
                skill.try_fire()
            mi.reset()

    def start(self):
        t = RepeatingTimer(self._interval_sec, self.run)
        t.start()

        def on_mouse_click(x, y, button, pressed):
            mi = self._mouse_info
            if button == mouse.Button.right:
                if pressed:
                    mi.right_down()
                else:
                    mi.right_up()

        with mouse.Listener(
            on_click=on_mouse_click
        ) as listener:
            listener.join()
