from .. import Events, State, Supervisor

# Create states
q0_state = State("q0", True)
q10_state = State("q10", False)
q11_state = State("q11", False)
q12_state = State("q12", False)
q2_state = State("q2", False)
q3_state = State("q3", False)
q4_state = State("q4", False)
q5_state = State("q5", False)
q6_state = State("q6", False)
q7_state = State("q7", False)
q8_state = State("q8", False)
q9_state = State("q9", False)


# Create transitions
q0_state.add_transition(Events['m7'], q3_state)
q0_state.add_transition(Events['s4'], q5_state)
q0_state.add_transition(Events['s3'], q7_state)
q10_state.add_transition(Events['m7'], q12_state)
q10_state.add_transition(Events['f3'], q4_state)
q10_state.add_transition(Events['f4'], q8_state)
q11_state.add_transition(Events['m7'], q12_state)
q11_state.add_transition(Events['f3'], q5_state)
q11_state.add_transition(Events['f4'], q8_state)
q12_state.add_transition(Events['p7'], q10_state)
q12_state.add_transition(Events['f3'], q6_state)
q12_state.add_transition(Events['f4'], q9_state)
q2_state.add_transition(Events['m7'], q3_state)
q2_state.add_transition(Events['s4'], q5_state)
q3_state.add_transition(Events['p7'], q0_state)
q3_state.add_transition(Events['s4'], q6_state)
q4_state.add_transition(Events['s3'], q10_state)
q4_state.add_transition(Events['f4'], q2_state)
q4_state.add_transition(Events['m7'], q6_state)
q5_state.add_transition(Events['f4'], q2_state)
q5_state.add_transition(Events['m7'], q6_state)
q6_state.add_transition(Events['f4'], q3_state)
q6_state.add_transition(Events['p7'], q4_state)
q7_state.add_transition(Events['f3'], q0_state)
q7_state.add_transition(Events['s4'], q11_state)
q7_state.add_transition(Events['m7'], q9_state)
q8_state.add_transition(Events['s4'], q11_state)
q8_state.add_transition(Events['f3'], q2_state)
q8_state.add_transition(Events['m7'], q9_state)
q9_state.add_transition(Events['s4'], q12_state)
q9_state.add_transition(Events['f3'], q3_state)
q9_state.add_transition(Events['p7'], q7_state)


# create state list
state_list = []
state_list.append(q0_state)
state_list.append(q10_state)
state_list.append(q11_state)
state_list.append(q12_state)
state_list.append(q2_state)
state_list.append(q3_state)
state_list.append(q4_state)
state_list.append(q5_state)
state_list.append(q6_state)
state_list.append(q7_state)
state_list.append(q8_state)
state_list.append(q9_state)


# create event list
alphabet = []
alphabet.append(Events['m7'])
alphabet.append(Events['s4'])
alphabet.append(Events['s3'])
alphabet.append(Events['f3'])
alphabet.append(Events['f4'])
alphabet.append(Events['p7'])


# create supervisor
supE03_bloqueia_braco = Supervisor("supE03_bloqueia_braco", state_list, alphabet)