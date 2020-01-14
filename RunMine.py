
from pynput.keyboard import Controller

import Helper
from Skill import SkillCtrl

keyboard = Controller()

skills = [
    SkillCtrl(keyboard, 'd', 300, 200),
    SkillCtrl(keyboard, '2', 4500, 100),
    SkillCtrl(keyboard, '3', 4900, 100),
    SkillCtrl(keyboard, '4', 3800, 100),
    SkillCtrl(keyboard, '5', 5300, 100),
    SkillCtrl(keyboard, 'q', 5500, 100),
    SkillCtrl(keyboard, 'r', 1200, 100),
    SkillCtrl(keyboard, 't', 1000, 100)
]
skills_sp = [
    SkillCtrl(keyboard, 'd', 300, 200, 1500),
    SkillCtrl(keyboard, 'd', 300, 200, 1500),
    SkillCtrl(keyboard, 'd', 300, 200, 1500)
]

if __name__ == '__main__':
    j = Helper.Job([skills, skills_sp])
    j.start()
