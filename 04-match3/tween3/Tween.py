import math

class Tween:
    def __init__(self, obj, property_name, start_val, end_val, duration, easing_name, on_complete=None):
        self.obj = obj
        self.property_name = property_name
        self.start_val = start_val
        self.end_val = end_val
        self.duration = duration
        self.easing_func = Tween.getEasingFunction(easing_name)
        self.timer = 0
        self.active = True
        self.on_complete = on_complete

    def update(self, dt):
        if not self.active:
            return
        self.timer += dt
        if self.timer > self.duration:
            self.timer = self.duration
            self.active = False
            if self.on_complete:
                self.on_complete()


        progress = self.timer / self.duration
        current_val = self.easing_func(self.start_val, self.end_val, progress, 1)
        setattr(self.obj, self.property_name, current_val)
        #self.obj[self.property_name] = current_val

#---------------------------------------------------------
    def getEasingFunction(easing_name):
        if easing_name == "linear":
            return Tween.linear
        elif easing_name == "ease_in_quad":
            return Tween.ease_in_quad
        elif easing_name == "ease_out_quad":
            return Tween.ease_out_quad
        elif easing_name == "easeOutElastic":
            return Tween.easeOutElastic
        else:
            raise ValueError("Invalid easing function name")

    def linear(start_val, end_val, t, duration):
        if duration <= 0:
            raise ValueError("duration must be greater than 0")
        # Clamp t to be within the range [0, DURATION]
        t = max(0, min(t, duration))
        return start_val + (end_val - start_val) * t / duration

    def ease_in_quad(start_val, end_val, t, duration):
        t = max(0, min(t, duration)) / duration  # Normalize t to [0, 1]
        return start_val + (end_val - start_val) * (t**2)

    def ease_out_quad(start_val, end_val, t, duration):
        t = max(0, min(t, duration)) / duration  # Normalize t to [0, 1]
        return start_val - (end_val - start_val) * (t * (t - 2))

    def easeOutElastic(start_val, end_val, t, duration):
        if t == 0:
            return start_val
        t /= duration
        if t == 1:
            return end_val
        # Adjusting the period to control the frequency of bounces
        p = duration * 0.3  # This period might result in around 3-4 bounces
        # Adjusted amplitude to a fixed proportion of the movement range
        a = (end_val - start_val) * 0.25
        s = p / 4
        return a * math.pow(2, -10 * t) * math.sin((t * duration - s) * (2 * math.pi) / p) + end_val