
from Tween import Tween

class TweenManager:
    tweens = []
    # def __init__(self):
    #     self.tweens = []

    def create_tween(obj, property_name, start_val, end_val, duration, easing_func):
        """Create and add a tween to the manager."""
        tween = Tween(obj, property_name, start_val, end_val, duration, easing_func)
        TweenManager.tweens.append(tween)

    def update(dt):
        """Update all active tweens and remove completed ones."""
        for tween in TweenManager.tweens[:]:
            tween.update(dt)
            if not tween.active:
                TweenManager.tweens.remove(tween)
