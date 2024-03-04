'''
    Python port of the Harward's GD50 course
    https://cs50.harvard.edu/games/2018/

    Ported by:  Fakhir Shaheen
    Website:    https://fakhirshaheen.com/
    github:     https://github.com/fakhirsh
    linkedin:   https://www.linkedin.com/in/fakhirshaheen/
'''

# StateManager - a state machine manager
#
# Usage:
#
#   States are only created as need, to save memory, reduce clean-up bugs and increase speed
#   due to garbage collection taking longer with more data in memory.
# 
#   States are added with a string identifier and an intialisation function.
#   It is expect the init function, when called, will return a dictionary with
#   'render', 'update', 'enter', and 'exit' methods.
#
# stateMachine = StateMachine({
#     'MainMenu': lambda: MainMenu(),
#     'InnerGame': lambda: InnerGame(),
#     'GameOver': lambda: GameOver()
# })
# stateMachine.change('MainGame')
#
# Arguments passed into the change function after the state name
# will be forwarded to the enter function of the state being changed too.
#
# State identifiers should have the same name as the state dictionary, unless there's a good
# reason not to. i.e. MainMenu creates a state using the MainMenu dictionary. This keeps things
# straight forward.
#
# =Doing Transitions=
#

# Define the StateMachine class to manage different game states
class StateManager:
    def __init__(self):
        # Initializes the StateManager with an empty list of states and an empty default state
        self.states = []            # List to store the states
        #self.current_state = None   # Set the initial state to an empty placeholder

    def changeState(self, newState):
        '''
        Changes the current state to a new state
        @param newState: The fully initialized object of the new state to switch to...       
        '''
        if self.states:
            self.states[-1].free()
            self.states[-1].unload()
            self.states.pop()
        
        self.states.append(newState)
        self.states[-1].load()
        self.states[-1].init()

    def update(self, dt):
        '''
        Updates the current state
        @param dt: The delta time since the last frame
        '''
        if self.states:
            self.states[-1].update(dt)

    def render(self, virtual_screen, dt=0.0):
        '''
        Renders the current state
        @param virtual_screen: The Pygame screen surface to draw on
        @param dt: The delta time since the last frame
        '''
        if self.states:
            self.states[-1].render(virtual_screen, dt)

