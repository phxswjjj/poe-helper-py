import random
from datetime import datetime, timedelta

from pynput.keyboard import Controller
import time


class SkillCtrl:
    def __init__(self, kb: Controller, kc: str, delay_ms: float = 0, delay_ms_bonus: float = 0, wait_ms: float = 0):
        if not kb or not isinstance(kb, Controller):
            raise 'kb is not pynput.keyboard.Controller'
        else:
            self._kb = kb

        if not isinstance(kc, str):
            raise 'kc is not string'
        else:
            self._kc = kc

        self._delay_ms: float = delay_ms
        self._delay_ms_bonus: float = delay_ms_bonus
        self._wait_ms: float = wait_ms
        self._next_fire_time: datetime = datetime.now()
        self._next_fire()

    def try_fire(self) -> bool:
        if datetime.now() >= self._next_fire_time:
            if self._wait_ms:
                time.sleep(self._wait_ms / 1000)
            self._kb.type(self._kc)
            self._next_fire()
            return True
        else:
            return False

    def immediate_fire(self):
        self._kb.type(self._kc)
        self._next_fire()

    def _next_fire(self) -> datetime:
        bonus_ms: float = 0
        if self._delay_ms_bonus:
            bonus_rate = random.random()
            bonus_ms = self._delay_ms_bonus * bonus_rate
        delay_ms: float = 0
        if self._delay_ms or bonus_ms:
            delay_ms = self._delay_ms + bonus_ms
        if delay_ms:
            self._next_fire_time = datetime.now() + timedelta(0, 0, 0, delay_ms)
        return self._next_fire_time


if __name__ == '__main__':
    keyboard = Controller()
    s1 = SkillCtrl(keyboard, 'c', 0, 1000)
    print(s1.try_fire())
