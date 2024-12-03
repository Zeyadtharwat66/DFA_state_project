import sys
states = input("Enter the finite set of states: ").split()
input_alphabet = input("Enter the input alphabets: ").split()
for symbol in input_alphabet:
    if not (symbol.isdigit() or symbol == "empty"):
        print("Error: You must enter digits as input alphabet or 'empty'")
        sys.exit()
initial_state = input("Enter the initial state: ")
if initial_state not in states:
    print("Initial state is not recognized")
    sys.exit()
final_state = input("Enter the accepting states: ").split()
for state in final_state:
    if state not in states:
        print("Accepting state is not recognized")
        sys.exit()
transition_table = {}
for state in states:
    ts = input(f"Enter values for each row of state {state} : ").split()
    transition_table[state] = {}
    for j, transition in enumerate(ts):
        if transition.startswith("[") and transition.endswith("]"):
            transition_table[state][input_alphabet[j]] = transition[1:-1].split(",")
        elif transition != "fi":
            transition_table[state][input_alphabet[j]] = [transition]
        else:
            transition_table[state][input_alphabet[j]] = []
def epsilon_closure(states):
    closure = set(states)
    stack = list(states)
    while stack:
        current = stack.pop()
        for next_state in transition_table.get(current, {}).get("empty", []):
            if next_state not in closure:
                closure.add(next_state)
                stack.append(next_state)
    return closure
while True:
    check_string = input("Enter the string you want to test: ")
    check = list(check_string)
    if any(symbol not in input_alphabet for symbol in check):
        print("String contains invalid symbols")
        continue
    current_states = epsilon_closure([initial_state])
    print("The Trace:", end=" ")
    for symbol in check:
        next_states = set()
        for state in current_states:
            next_states.update(transition_table.get(state, {}).get(symbol, []))
        current_states = epsilon_closure(next_states)
        if not current_states:
            print("\nString is not Accepted")
            break
        print(f"{'->'.join(sorted(current_states))}", end="->")
    if any(state in final_state for state in current_states):
        print("\nString is Accepted")
    else:
        print("\nString is not Accepted")