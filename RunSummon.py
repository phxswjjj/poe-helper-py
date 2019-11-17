
from pynput.keyboard import Controller

import Helper
from Skill import SkillCtrl

keyboard = Controller()

skills = {
    SkillCtrl(keyboard, '2', 3800, 500),
    SkillCtrl(keyboard, '3', 3800, 500),
    SkillCtrl(keyboard, '4', 5300, 500),
    SkillCtrl(keyboard, '5', 6500, 500),
    SkillCtrl(keyboard, 'q', 10300, 500),
    SkillCtrl(keyboard, 't', 3000, 500)
}

if __name__ == '__main__':
    j = Helper.Job(skills)
    j.start()
