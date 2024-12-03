import sys
states = input("Enter the finite set of states : ").split()
input_alphabet = input("Enter the input alphabets : ").split()
initial_state = input("Enter the initial state : ")
if not initial_state in states:
    print("Initial state is not recognized")
    sys.exit()
final_state = input("Enter the accepting states : ").split()
for i in range(len(final_state)):    
    if not final_state[i] in states:
        print("Accepting state is not recognized")
        sys.exit()
transition_table = {}
for i in range(len(states)):
    ts = input("Enter values For each Row in 1 Line : ").split()
    if not len(ts) == len(input_alphabet):
        print("Number of states is not correct")
        sys.exit()
    for j in range(len(ts)):
        if not ts[j] in states:
            print("Some states are not recognized")
            sys.exit()
        transition_table.setdefault(states[i], {})[f"{input_alphabet[j]}"] = ts[j]
while True:
    check_string = input("Enter The String You Want To Test : ")
    flag=False
    for i in range(len(check_string)):
        if not check_string[i] in input_alphabet:
            print("Error You must enter digits as input alphabet and digits from input alphabet")
            flag =True
            break
    if flag==True:
        continue
    check = list(check_string)
    next_state = transition_table[initial_state][check[0]]
    print(f"The Trace : {next_state}",end='->')
    for i in range(1, len(check)):
        next_state = transition_table[next_state][check[i]]
        print(next_state,end='->')
    if next_state in final_state:
        print("\nString is Accepted")
    else:
        print("\nString is not Accepted")