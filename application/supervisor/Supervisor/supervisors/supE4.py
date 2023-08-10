from .. import Events, State, Supervisor

# Create states
g5S0_S0_S0_state = State("g5S0_S0_S0", True)
g5S0_S0_S1_state = State("g5S0_S0_S1", False)
g5S0_S1_S0_state = State("g5S0_S1_S0", False)
g5S0_S1_S1_state = State("g5S0_S1_S1", False)
g5S1_S0_S0_state = State("g5S1_S0_S0", False)
g5S1_S0_S1_state = State("g5S1_S0_S1", False)
g5S1_S1_S0_state = State("g5S1_S1_S0", False)
g5S1_S1_S1_state = State("g5S1_S1_S1", False)


# Create transitions
g5S0_S0_S0_state.add_transition(Events['s2'], g5S0_S0_S1_state)
g5S0_S0_S0_state.add_transition(Events['ppg_item'], g5S0_S1_S0_state)
g5S0_S0_S1_state.add_transition(Events['s2'], g5S0_S0_S1_state)
g5S0_S0_S1_state.add_transition(Events['ppg_item'], g5S0_S1_S1_state)
g5S0_S1_S0_state.add_transition(Events['ppg_item'], g5S0_S1_S0_state)
g5S0_S1_S0_state.add_transition(Events['s2'], g5S0_S1_S1_state)
g5S0_S1_S0_state.add_transition(Events['ppg_on'], g5S1_S0_S0_state)
g5S0_S1_S1_state.add_transition(Events['ppg_item'], g5S0_S1_S1_state)
g5S0_S1_S1_state.add_transition(Events['s2'], g5S0_S1_S1_state)
g5S0_S1_S1_state.add_transition(Events['ppg_on'], g5S1_S0_S1_state)
g5S1_S0_S0_state.add_transition(Events['s2'], g5S1_S0_S1_state)
g5S1_S0_S0_state.add_transition(Events['ppg_item'], g5S1_S1_S0_state)
g5S1_S0_S1_state.add_transition(Events['ppg_off'], g5S0_S0_S0_state)
g5S1_S0_S1_state.add_transition(Events['s2'], g5S1_S0_S1_state)
g5S1_S0_S1_state.add_transition(Events['ppg_item'], g5S1_S1_S1_state)
g5S1_S1_S0_state.add_transition(Events['ppg_item'], g5S1_S1_S0_state)
g5S1_S1_S0_state.add_transition(Events['s2'], g5S1_S1_S1_state)
g5S1_S1_S1_state.add_transition(Events['ppg_off'], g5S0_S1_S0_state)
g5S1_S1_S1_state.add_transition(Events['ppg_item'], g5S1_S1_S1_state)
g5S1_S1_S1_state.add_transition(Events['s2'], g5S1_S1_S1_state)


# create state list
state_list = []
state_list.append(g5S0_S0_S0_state)
state_list.append(g5S0_S0_S1_state)
state_list.append(g5S0_S1_S0_state)
state_list.append(g5S0_S1_S1_state)
state_list.append(g5S1_S0_S0_state)
state_list.append(g5S1_S0_S1_state)
state_list.append(g5S1_S1_S0_state)
state_list.append(g5S1_S1_S1_state)


# create event list
alphabet = []
alphabet.append(Events['s2'])
alphabet.append(Events['ppg_item'])
alphabet.append(Events['ppg_on'])
alphabet.append(Events['ppg_off'])


# create supervisor
supE4 = Supervisor("supE4", state_list, alphabet)