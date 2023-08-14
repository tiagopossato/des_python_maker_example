from .. import Events, State, Supervisor

# Create states
q0_state = State("q0", True)
q2_state = State("q2", False)
q3_state = State("q3", False)
q4_state = State("q4", False)


# Create transitions
q0_state.add_transition(Events['t5'], q2_state)
q2_state.add_transition(Events['t5'], q2_state)
q2_state.add_transition(Events['s5'], q3_state)
q3_state.add_transition(Events['f5'], q0_state)
q3_state.add_transition(Events['t5'], q4_state)
q4_state.add_transition(Events['f5'], q2_state)
q4_state.add_transition(Events['t5'], q4_state)


# create state list
state_list = []
state_list.append(q0_state)
state_list.append(q2_state)
state_list.append(q3_state)
state_list.append(q4_state)


# create event list
alphabet = []
alphabet.append(Events['t5'])
alphabet.append(Events['s5'])
alphabet.append(Events['f5'])


# create supervisor
supE08_pega_peca = Supervisor("supE08_pega_peca", state_list, alphabet)