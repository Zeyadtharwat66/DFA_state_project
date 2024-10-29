states = input("Enter the finite set of states : ").split()
input_alphabet = input("Enter the input alphabets : ").split()
initial_state = input("Enter the initial state : ")
final_state = input("Enter the accepting states : ").split()
transition_table = {}
input_alphabet_dict = {}
for i in range(len(states)):
    ts = input("Enter values For each Row in 1 Line : ").split()
    for j in range(len(ts)):
        transition_table.setdefault(states[i], {})[f"{j}"] = ts[j]
while True:
    check_string = input("Enter The String You Want To Test : ")
    check = list(check_string)
    next_state = transition_table[initial_state][check[0]]
    for i in range(1, len(check)):
        next_state = transition_table[next_state][check[i]]
    if next_state in final_state:
        print("String is Accepted")
    else:
        print("String is not Accepted")