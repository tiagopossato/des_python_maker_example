from .. import Events, State, Supervisor

# Create states
q0_state = State("q0", True)
q2_state = State("q2", False)
q3_state = State("q3", False)
q4_state = State("q4", False)


# Create transitions
q0_state.add_transition(Events['s2'], q2_state)
q0_state.add_transition(Events['ppg_on'], q3_state)
q2_state.add_transition(Events['s2'], q2_state)
q2_state.add_transition(Events['ppg_on'], q4_state)
q3_state.add_transition(Events['s2'], q4_state)
q4_state.add_transition(Events['ppg_off'], q0_state)
q4_state.add_transition(Events['s2'], q4_state)


# create state list
state_list = []
state_list.append(q0_state)
state_list.append(q2_state)
state_list.append(q3_state)
state_list.append(q4_state)


# create event list
alphabet = []
alphabet.append(Events['s2'])
alphabet.append(Events['ppg_on'])
alphabet.append(Events['ppg_off'])


# create supervisor
se04_solta_peca = Supervisor("se04_solta_peca", state_list, alphabet)