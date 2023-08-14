from .. import Events, State, Supervisor

# Create states
q0_state = State("q0", True)
q2_state = State("q2", False)
q3_state = State("q3", False)
q4_state = State("q4", False)
q5_state = State("q5", False)
q6_state = State("q6", False)
q7_state = State("q7", False)
q8_state = State("q8", False)


# Create transitions
q0_state.add_transition(Events['s5'], q4_state)
q0_state.add_transition(Events['s3'], q5_state)
q2_state.add_transition(Events['s5'], q4_state)
q2_state.add_transition(Events['s3'], q6_state)
q3_state.add_transition(Events['f5'], q2_state)
q3_state.add_transition(Events['s3'], q7_state)
q4_state.add_transition(Events['f5'], q2_state)
q4_state.add_transition(Events['s3'], q8_state)
q5_state.add_transition(Events['s5'], q8_state)
q6_state.add_transition(Events['f3'], q0_state)
q6_state.add_transition(Events['s5'], q8_state)
q7_state.add_transition(Events['f5'], q6_state)
q8_state.add_transition(Events['f3'], q3_state)
q8_state.add_transition(Events['f5'], q6_state)


# create state list
state_list = []
state_list.append(q0_state)
state_list.append(q2_state)
state_list.append(q3_state)
state_list.append(q4_state)
state_list.append(q5_state)
state_list.append(q6_state)
state_list.append(q7_state)
state_list.append(q8_state)


# create event list
alphabet = []
alphabet.append(Events['s5'])
alphabet.append(Events['s3'])
alphabet.append(Events['f5'])
alphabet.append(Events['f3'])


# create supervisor
supE05_sobre_braco = Supervisor("supE05_sobre_braco", state_list, alphabet)