
from pynput.keyboard import Controller

import Helper
from Skill import SkillCtrl

keyboard = Controller()

skills = {
    SkillCtrl(keyboard, 'd', 300, 200),
    SkillCtrl(keyboard, '2', 5300, 500),
    SkillCtrl(keyboard, '3', 7000, 500),
    SkillCtrl(keyboard, '4', 4000, 500),
    SkillCtrl(keyboard, '5', 5000, 500),
    SkillCtrl(keyboard, 'q', 1100, 500),
    SkillCtrl(keyboard, 't', 1000, 500)
}

if __name__ == '__main__':
    j = Helper.Job(skills)
    j.start()
