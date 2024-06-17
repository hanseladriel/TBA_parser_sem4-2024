class State:
    def __init__(self, name):
        self.name = name
        self.transitions = {}
        self.accepting = False

    def add_transition(self, symbol, next_state):
        self.transitions[symbol] = next_state

    def set_accepting(self):
        self.accepting = True

class DFA:
    def __init__(self, input_alphabet):
        self.states = {}
        self.input_alphabet = input_alphabet
        self.initial_state = None

    def add_state(self, state_name):
        state = State(state_name)
        self.states[state_name] = state
        return state

    def add_transition(self, state_name, symbol, next_state_name):
        state = self.states[state_name]
        next_state = self.states[next_state_name]
        state.add_transition(symbol, next_state)

    def set_initial_state(self, state_name):
        self.initial_state = self.states[state_name]

    def set_accepting_state(self, state_name):
        self.states[state_name].set_accepting()

    def simulate(self, input_string):
        current_state = self.initial_state
        for symbol in input_string:
            if symbol not in self.input_alphabet:
                return False
            if symbol not in current_state.transitions:
                return False
            current_state = current_state.transitions[symbol]
        return current_state.accepting