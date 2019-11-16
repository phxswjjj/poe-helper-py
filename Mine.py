import random
from datetime import datetime, timedelta

from pynput import mouse
from pynput.keyboard import Controller

from Skill import SkillCtrl

keyboard = Controller()

role = '召喚'
role = '地雷'
if role == '地雷':
    key_d = SkillCtrl(keyboard, 'd', 300, 200)
    key_2 = SkillCtrl(keyboard, '2', 5300, 500)
    key_3 = SkillCtrl(keyboard, '3', 7000, 500)
    key_4 = SkillCtrl(keyboard, '4', 4000, 500)
    key_5 = SkillCtrl(keyboard, '5', 5000, 500)
    key_q = SkillCtrl(keyboard, 'q', 1100, 500)
    key_t = SkillCtrl(keyboard, 't', 1000, 500)
else:
    key_d = SkillCtrl(keyboard, 'd', 99999300, 200)
    key_2 = SkillCtrl(keyboard, '2', 3800, 500)
    key_3 = SkillCtrl(keyboard, '3', 3800, 500)
    key_4 = SkillCtrl(keyboard, '4', 5300, 500)
    key_5 = SkillCtrl(keyboard, '5', 6500, 500)
    key_q = SkillCtrl(keyboard, 'q', 10300, 500)
    key_t = SkillCtrl(keyboard, 't', 3000, 500)


def on_click(x, y, button, pressed):
    if button == mouse.Button.right:
        key_d.try_fire()
        key_2.try_fire()
        key_3.try_fire()
        key_4.try_fire()
        key_5.try_fire()
        key_q.try_fire()
        key_t.try_fire()


if __name__ == '__main__':
    with mouse.Listener(
        on_click=on_click
    ) as listener:
        listener.join()
