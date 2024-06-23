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

class DFABuilder:
    def from_config(config):
        dfa = DFA(config["input_alphabet"])
        DFABuilder._add_states(dfa, config["states"])
        DFABuilder._add_transitions(dfa, config["transitions"])
        DFABuilder._add_trap_state(dfa)
        dfa.set_initial_state(config["initial_state"])
        DFABuilder._set_accepting_states(dfa, config["accepting_states"])
        return dfa

    def _add_states(dfa, states):
        for state in states:
            dfa.add_state(state)
    
    def _add_transitions(dfa, transitions):
        for state, state_transitions in transitions.items():
            for symbol, next_state in state_transitions.items():
                dfa.add_transition(state, symbol, next_state)

    def _add_trap_state(dfa):
        trap_state = dfa.add_state("trap")
        for state in dfa.states.values():
            for symbol in dfa.input_alphabet:
                if symbol not in state.transitions:
                    state.add_transition(symbol, trap_state)

    def _set_accepting_states(dfa, accepting_states):
        for state in accepting_states:
            dfa.set_accepting_state(state)