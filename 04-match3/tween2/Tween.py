class Tween:
    def __init__(self, obj, property_name, start_val, end_val, duration, easing_func):
        self.obj = obj
        self.property_name = property_name
        self.start_val = start_val
        self.end_val = end_val
        self.duration = duration
        self.easing_func = easing_func
        self.timer = 0
        self.active = True

    def update(self, dt):
        if not self.active:
            return
        self.timer += dt
        if self.timer > self.duration:
            self.timer = self.duration
            self.active = False

        progress = self.timer / self.duration
        current_val = self.easing_func(self.start_val, self.end_val, progress, 1)
        setattr(self.obj, self.property_name, current_val)
        #self.obj[self.property_name] = current_val
