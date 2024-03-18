'''
    Python port of the Harward's GD50 course
    https://cs50.harvard.edu/games/2018/

    Ported by:  Fakhir Shaheen
    Website:    https://fakhirshaheen.com/
    github:     https://github.com/fakhirsh
    linkedin:   https://www.linkedin.com/in/fakhirshaheen/
'''


class Timer:
    def __init__(self, interval, action, repeat=-1):
        """
        Initializes a Timer object.

        Parameters:
        - interval (float): The time interval in seconds between each action.
        - action (function): The function to be executed at each interval.
        - repeat (int, optional): The number of times the timer should repeat. 
          Default is -1 for infinite repetitions.
        """
        self.interval = interval
        self.action = action
        self.repeat = repeat  # -1 for infinite, positive for specific repetitions
        self.elapsed = 0

    def update(self, dt):
        """
        Updates the timer based on the elapsed time.

        Parameters:
        - dt (float): The elapsed time since the last update in seconds.

        Returns:
        - bool: True if the timer should continue, False if it should be removed.
        """
        self.elapsed += dt
        if self.elapsed >= self.interval:
            self.action()
            self.elapsed -= self.interval  # Reset elapsed time
            if self.repeat > 0:
                self.repeat -= 1  # Decrement if not infinite
            if self.repeat == 0:
                return False  # Timer should be removed if repeat reaches 0
        return True  # Timer continues