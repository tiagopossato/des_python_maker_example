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
q0_state.add_transition(Events['t2'], q2_state)
q0_state.add_transition(Events['s5'], q7_state)
q10_state.add_transition(Events['t2'], q11_state)
q10_state.add_transition(Events['f5'], q4_state)
q10_state.add_transition(Events['f2'], q7_state)
q11_state.add_transition(Events['t2'], q11_state)
q11_state.add_transition(Events['f5'], q6_state)
q11_state.add_transition(Events['f2'], q8_state)
q12_state.add_transition(Events['t2'], q12_state)
q12_state.add_transition(Events['f5'], q6_state)
q12_state.add_transition(Events['f2'], q9_state)
q2_state.add_transition(Events['t2'], q2_state)
q2_state.add_transition(Events['s5'], q8_state)
q3_state.add_transition(Events['t2'], q3_state)
q3_state.add_transition(Events['s2'], q4_state)
q3_state.add_transition(Events['s5'], q9_state)
q4_state.add_transition(Events['f2'], q0_state)
q4_state.add_transition(Events['s5'], q10_state)
q4_state.add_transition(Events['t2'], q5_state)
q5_state.add_transition(Events['s5'], q11_state)
q5_state.add_transition(Events['f2'], q2_state)
q5_state.add_transition(Events['t2'], q5_state)
q6_state.add_transition(Events['s5'], q12_state)
q6_state.add_transition(Events['f2'], q3_state)
q6_state.add_transition(Events['t2'], q6_state)
q7_state.add_transition(Events['f5'], q0_state)
q7_state.add_transition(Events['t2'], q8_state)
q8_state.add_transition(Events['f5'], q3_state)
q8_state.add_transition(Events['t2'], q8_state)
q9_state.add_transition(Events['s2'], q10_state)
q9_state.add_transition(Events['f5'], q3_state)
q9_state.add_transition(Events['t2'], q9_state)


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
alphabet.append(Events['t2'])
alphabet.append(Events['s5'])
alphabet.append(Events['f5'])
alphabet.append(Events['f2'])
alphabet.append(Events['s2'])


# create supervisor
supE10_liga_cv2 = Supervisor("supE10_liga_cv2", state_list, alphabet)