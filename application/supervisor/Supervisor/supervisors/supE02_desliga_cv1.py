from .. import Events, State, Supervisor

# Create states
q0_state = State("q0", True)
q2_state = State("q2", False)
q3_state = State("q3", False)
q4_state = State("q4", False)


# Create transitions
q0_state.add_transition(Events['t1'], q2_state)
q0_state.add_transition(Events['s1'], q3_state)
q2_state.add_transition(Events['t1'], q2_state)
q2_state.add_transition(Events['s1'], q4_state)
q3_state.add_transition(Events['t1'], q4_state)
q4_state.add_transition(Events['f1'], q0_state)
q4_state.add_transition(Events['t1'], q4_state)


# create state list
state_list = []
state_list.append(q0_state)
state_list.append(q2_state)
state_list.append(q3_state)
state_list.append(q4_state)


# create event list
alphabet = []
alphabet.append(Events['t1'])
alphabet.append(Events['s1'])
alphabet.append(Events['f1'])


# create supervisor
supE02_desliga_cv1 = Supervisor("supE02_desliga_cv1", state_list, alphabet)