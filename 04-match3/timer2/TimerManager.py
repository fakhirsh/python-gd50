'''
    Python port of the Harward's GD50 course
    https://cs50.harvard.edu/games/2018/

    Ported by:  Fakhir Shaheen
    Website:    https://fakhirshaheen.com/
    github:     https://github.com/fakhirsh
    linkedin:   https://www.linkedin.com/in/fakhirshaheen/
'''

from Timer import Timer

class TimerManager:
    timers = []

    @staticmethod
    def add_timer(interval, action, repeat=-1):
        TimerManager.timers.append(Timer(interval, action, repeat))

    @staticmethod
    def update(dt):
        TimerManager.timers = [timer for timer in TimerManager.timers if timer.update(dt)]

    @staticmethod
    def clear():
        TimerManager.timers.clear()