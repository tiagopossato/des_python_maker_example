from .. import Events, State, Supervisor

# Create states
q0_state = State("q0", True)
q1_state = State("q1", False)
q10_state = State("q10", False)
q11_state = State("q11", False)
q12_state = State("q12", False)
q13_state = State("q13", False)
q14_state = State("q14", False)
q15_state = State("q15", False)
q16_state = State("q16", False)
q17_state = State("q17", False)
q18_state = State("q18", False)
q19_state = State("q19", False)
q20_state = State("q20", False)
q21_state = State("q21", False)
q22_state = State("q22", False)
q23_state = State("q23", False)
q24_state = State("q24", False)
q25_state = State("q25", False)
q26_state = State("q26", False)
q27_state = State("q27", False)
q28_state = State("q28", False)
q29_state = State("q29", False)
q3_state = State("q3", False)
q30_state = State("q30", False)
q31_state = State("q31", False)
q32_state = State("q32", False)
q33_state = State("q33", False)
q34_state = State("q34", False)
q35_state = State("q35", False)
q36_state = State("q36", False)
q37_state = State("q37", False)
q38_state = State("q38", False)
q39_state = State("q39", False)
q4_state = State("q4", False)
q40_state = State("q40", False)
q5_state = State("q5", False)
q6_state = State("q6", False)
q7_state = State("q7", False)
q8_state = State("q8", False)
q9_state = State("q9", False)


# Create transitions
q0_state.add_transition(Events['s4'], q14_state)
q0_state.add_transition(Events['t1'], q3_state)
q0_state.add_transition(Events['m7'], q7_state)
q1_state.add_transition(Events['t1'], q0_state)
q1_state.add_transition(Events['s4'], q11_state)
q1_state.add_transition(Events['m7'], q6_state)
q10_state.add_transition(Events['t1'], q10_state)
q10_state.add_transition(Events['s4'], q20_state)
q10_state.add_transition(Events['s3'], q26_state)
q10_state.add_transition(Events['p7'], q5_state)
q11_state.add_transition(Events['f4'], q1_state)
q11_state.add_transition(Events['t1'], q12_state)
q11_state.add_transition(Events['m7'], q16_state)
q12_state.add_transition(Events['f4'], q0_state)
q12_state.add_transition(Events['t1'], q13_state)
q12_state.add_transition(Events['m7'], q17_state)
q13_state.add_transition(Events['t1'], q13_state)
q13_state.add_transition(Events['m7'], q18_state)
q13_state.add_transition(Events['f4'], q3_state)
q13_state.add_transition(Events['s3'], q32_state)
q14_state.add_transition(Events['t1'], q14_state)
q14_state.add_transition(Events['m7'], q19_state)
q14_state.add_transition(Events['f4'], q4_state)
q15_state.add_transition(Events['t1'], q15_state)
q15_state.add_transition(Events['m7'], q20_state)
q15_state.add_transition(Events['s3'], q31_state)
q15_state.add_transition(Events['f4'], q5_state)
q16_state.add_transition(Events['p7'], q12_state)
q16_state.add_transition(Events['t1'], q17_state)
q16_state.add_transition(Events['f4'], q6_state)
q17_state.add_transition(Events['p7'], q13_state)
q17_state.add_transition(Events['t1'], q18_state)
q17_state.add_transition(Events['f4'], q7_state)
q18_state.add_transition(Events['p7'], q13_state)
q18_state.add_transition(Events['t1'], q18_state)
q18_state.add_transition(Events['s3'], q37_state)
q18_state.add_transition(Events['f4'], q8_state)
q19_state.add_transition(Events['p7'], q15_state)
q19_state.add_transition(Events['t1'], q19_state)
q19_state.add_transition(Events['f4'], q9_state)
q20_state.add_transition(Events['f4'], q10_state)
q20_state.add_transition(Events['p7'], q15_state)
q20_state.add_transition(Events['t1'], q20_state)
q20_state.add_transition(Events['s3'], q36_state)
q21_state.add_transition(Events['f3'], q1_state)
q21_state.add_transition(Events['t1'], q22_state)
q21_state.add_transition(Events['m7'], q26_state)
q21_state.add_transition(Events['s4'], q31_state)
q22_state.add_transition(Events['f3'], q0_state)
q22_state.add_transition(Events['t1'], q23_state)
q22_state.add_transition(Events['m7'], q27_state)
q22_state.add_transition(Events['s4'], q34_state)
q23_state.add_transition(Events['t1'], q23_state)
q23_state.add_transition(Events['m7'], q28_state)
q23_state.add_transition(Events['f3'], q3_state)
q23_state.add_transition(Events['s4'], q33_state)
q24_state.add_transition(Events['t1'], q24_state)
q24_state.add_transition(Events['m7'], q29_state)
q24_state.add_transition(Events['s4'], q34_state)
q24_state.add_transition(Events['f3'], q4_state)
q25_state.add_transition(Events['t1'], q25_state)
q25_state.add_transition(Events['m7'], q30_state)
q25_state.add_transition(Events['s4'], q35_state)
q25_state.add_transition(Events['f3'], q5_state)
q26_state.add_transition(Events['p7'], q22_state)
q26_state.add_transition(Events['t1'], q27_state)
q26_state.add_transition(Events['s4'], q36_state)
q26_state.add_transition(Events['f3'], q6_state)
q27_state.add_transition(Events['p7'], q23_state)
q27_state.add_transition(Events['t1'], q28_state)
q27_state.add_transition(Events['s4'], q39_state)
q27_state.add_transition(Events['f3'], q7_state)
q28_state.add_transition(Events['p7'], q23_state)
q28_state.add_transition(Events['t1'], q28_state)
q28_state.add_transition(Events['s4'], q38_state)
q28_state.add_transition(Events['f3'], q8_state)
q29_state.add_transition(Events['p7'], q25_state)
q29_state.add_transition(Events['t1'], q29_state)
q29_state.add_transition(Events['s4'], q39_state)
q29_state.add_transition(Events['f3'], q9_state)
q3_state.add_transition(Events['s4'], q13_state)
q3_state.add_transition(Events['s3'], q22_state)
q3_state.add_transition(Events['t1'], q3_state)
q3_state.add_transition(Events['m7'], q8_state)
q30_state.add_transition(Events['f3'], q10_state)
q30_state.add_transition(Events['p7'], q25_state)
q30_state.add_transition(Events['t1'], q30_state)
q30_state.add_transition(Events['s4'], q40_state)
q31_state.add_transition(Events['f3'], q11_state)
q31_state.add_transition(Events['f4'], q21_state)
q31_state.add_transition(Events['t1'], q32_state)
q31_state.add_transition(Events['m7'], q36_state)
q32_state.add_transition(Events['f3'], q12_state)
q32_state.add_transition(Events['f4'], q22_state)
q32_state.add_transition(Events['t1'], q33_state)
q32_state.add_transition(Events['m7'], q37_state)
q33_state.add_transition(Events['f3'], q13_state)
q33_state.add_transition(Events['f4'], q23_state)
q33_state.add_transition(Events['t1'], q33_state)
q33_state.add_transition(Events['m7'], q38_state)
q34_state.add_transition(Events['f3'], q14_state)
q34_state.add_transition(Events['f4'], q24_state)
q34_state.add_transition(Events['t1'], q34_state)
q34_state.add_transition(Events['m7'], q39_state)
q35_state.add_transition(Events['f3'], q15_state)
q35_state.add_transition(Events['f4'], q25_state)
q35_state.add_transition(Events['t1'], q35_state)
q35_state.add_transition(Events['m7'], q40_state)
q36_state.add_transition(Events['f3'], q16_state)
q36_state.add_transition(Events['f4'], q26_state)
q36_state.add_transition(Events['p7'], q32_state)
q36_state.add_transition(Events['t1'], q37_state)
q37_state.add_transition(Events['f3'], q17_state)
q37_state.add_transition(Events['f4'], q27_state)
q37_state.add_transition(Events['p7'], q33_state)
q37_state.add_transition(Events['t1'], q38_state)
q38_state.add_transition(Events['f3'], q18_state)
q38_state.add_transition(Events['f4'], q28_state)
q38_state.add_transition(Events['p7'], q33_state)
q38_state.add_transition(Events['t1'], q38_state)
q39_state.add_transition(Events['f3'], q19_state)
q39_state.add_transition(Events['f4'], q29_state)
q39_state.add_transition(Events['p7'], q35_state)
q39_state.add_transition(Events['t1'], q39_state)
q4_state.add_transition(Events['s4'], q14_state)
q4_state.add_transition(Events['t1'], q4_state)
q4_state.add_transition(Events['m7'], q9_state)
q40_state.add_transition(Events['f3'], q20_state)
q40_state.add_transition(Events['f4'], q30_state)
q40_state.add_transition(Events['p7'], q35_state)
q40_state.add_transition(Events['t1'], q40_state)
q5_state.add_transition(Events['m7'], q10_state)
q5_state.add_transition(Events['s4'], q15_state)
q5_state.add_transition(Events['s3'], q21_state)
q5_state.add_transition(Events['t1'], q5_state)
q6_state.add_transition(Events['p7'], q0_state)
q6_state.add_transition(Events['s4'], q16_state)
q6_state.add_transition(Events['t1'], q7_state)
q7_state.add_transition(Events['s4'], q19_state)
q7_state.add_transition(Events['p7'], q3_state)
q7_state.add_transition(Events['t1'], q8_state)
q8_state.add_transition(Events['s4'], q18_state)
q8_state.add_transition(Events['s3'], q27_state)
q8_state.add_transition(Events['p7'], q3_state)
q8_state.add_transition(Events['t1'], q8_state)
q9_state.add_transition(Events['s4'], q19_state)
q9_state.add_transition(Events['p7'], q5_state)
q9_state.add_transition(Events['t1'], q9_state)


# create state list
state_list = []
state_list.append(q0_state)
state_list.append(q1_state)
state_list.append(q10_state)
state_list.append(q11_state)
state_list.append(q12_state)
state_list.append(q13_state)
state_list.append(q14_state)
state_list.append(q15_state)
state_list.append(q16_state)
state_list.append(q17_state)
state_list.append(q18_state)
state_list.append(q19_state)
state_list.append(q20_state)
state_list.append(q21_state)
state_list.append(q22_state)
state_list.append(q23_state)
state_list.append(q24_state)
state_list.append(q25_state)
state_list.append(q26_state)
state_list.append(q27_state)
state_list.append(q28_state)
state_list.append(q29_state)
state_list.append(q3_state)
state_list.append(q30_state)
state_list.append(q31_state)
state_list.append(q32_state)
state_list.append(q33_state)
state_list.append(q34_state)
state_list.append(q35_state)
state_list.append(q36_state)
state_list.append(q37_state)
state_list.append(q38_state)
state_list.append(q39_state)
state_list.append(q4_state)
state_list.append(q40_state)
state_list.append(q5_state)
state_list.append(q6_state)
state_list.append(q7_state)
state_list.append(q8_state)
state_list.append(q9_state)


# create event list
alphabet = []
alphabet.append(Events['s4'])
alphabet.append(Events['t1'])
alphabet.append(Events['m7'])
alphabet.append(Events['s3'])
alphabet.append(Events['p7'])
alphabet.append(Events['f4'])
alphabet.append(Events['f3'])


# create supervisor
supE04_desce_braco = Supervisor("supE04_desce_braco", state_list, alphabet)