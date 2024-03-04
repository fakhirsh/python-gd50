'''
    Python port of the Harward's GD50 course
    https://cs50.harvard.edu/games/2018/

    Ported by:  Fakhir Shaheen
    Website:    https://fakhirshaheen.com/
    github:     https://github.com/fakhirsh
    linkedin:   https://www.linkedin.com/in/fakhirshaheen/
'''

class State:
    """
    The State class serves as an abstract base class for game states or application states.
    It defines a common interface for all states, including lifecycle methods for loading,
    initializing, pausing, resuming, updating, and rendering. Subclasses must implement
    these methods according to their specific needs.
    
    Attributes:
        isPaused (bool): Indicates whether the state is currently paused.
    """

#--------------------------------------------------------------------------------------------------
    
    def __init__(self):
        """
        Initializes the State instance, setting the initial paused status to False.
        """
        self.isPaused = False
        self.stateManager = None

#--------------------------------------------------------------------------------------------------

    def load(self):
        """
        Placeholder for a method to load resources or data necessary for the state.
        This method should be overridden in subclasses to perform state-specific loading operations.
        
        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        raise NotImplementedError

#--------------------------------------------------------------------------------------------------
    
    def unload(self):
        """
        Placeholder for a method to unload resources or data when the state is no longer needed.
        This method should be overridden in subclasses to perform state-specific unloading operations.
        
        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        raise NotImplementedError

#--------------------------------------------------------------------------------------------------
    
    def init(self):
        """
        Placeholder for a method to initialize the state. This method is intended to set up
        any necessary state-specific data structures or variables after loading resources.
        
        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        raise NotImplementedError
    
#--------------------------------------------------------------------------------------------------
    
    def free(self):
        """
        Placeholder for a method to free up resources and perform clean-up activities for the state.
        This method is called when the state is definitively done and can be used to ensure a clean exit.
        
        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        raise NotImplementedError
    
#--------------------------------------------------------------------------------------------------
    
    def pause(self):
        """
        Placeholder for a method to pause the state, such as when the application loses focus or
        when transitioning to another state that does not unload the current state.
        
        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        raise NotImplementedError
    
#--------------------------------------------------------------------------------------------------
    
    def resume(self):
        """
        Placeholder for a method to resume the state from a paused state, restoring
        activity and possibly re-initializing resources that were freed on pause.
        
        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        raise NotImplementedError
    
#--------------------------------------------------------------------------------------------------
    
    def update(self, dt):
        """
        Placeholder for the update method, which is called regularly to update the state of the game
        or application. This method should contain the logic for updating the state's data.
        
        Args:
            dt (float): The delta time, or time elapsed since the last update call, in seconds.
        
        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        raise NotImplementedError
    
#--------------------------------------------------------------------------------------------------
    
    def render(self, virtual_screen, dt=0.0):
        """
        Placeholder for the render method, which is called regularly to draw the state's visual elements.
        This method should contain all the drawing logic.
        
        Args:
            dt (float): Optional. The delta time, or time elapsed since the last render call, in seconds.
                        Defaults to 0.0 if not provided.
        
        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        raise NotImplementedError

#--------------------------------------------------------------------------------------------------
    
    def handle_event(self, event):
        """
        Placeholder for the method to handle events, such as user input or system events.
        This method should contain the logic for handling events.

        Args:
            event (pygame.event.Event): The event to handle.

        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        raise NotImplementedError

#--------------------------------------------------------------------------------------------------
    
    def is_paused(self):
        """
        Checks if the state is currently paused.
        
        Returns:
            bool: True if the state is paused, False otherwise.
        """
        return self.isPaused

#--------------------------------------------------------------------------------------------------