from prettytable import PrettyTable

states = input("Enter the finite set of states : ").split()
input_alphabet = input("Enter the input alphabets : ").split()
initial_state = input("Enter the initial state : ")
final_state = input("Enter the accepting states : ").split()
table1 = PrettyTable()
input_alphabet.insert(0, "  ")
table1.field_names = input_alphabet
for i in states:
    table1.add_row([i, "", ""])
print(table1)
transition_table = {}
input_alphabet_dict = {}
for i in range(len(states)):
    ts = input("Enter values For each Row in 1 Line : ").split()
    transition_table.setdefault(states[i], {})["0"] = ts[0]
    transition_table.setdefault(states[i], {})["1"] = ts[1]
table2 = PrettyTable()
table2.field_names = input_alphabet
for i in states:
    table2.add_row([i, transition_table[i]["0"], transition_table[i]["1"]])
print(table2)
while True:
    check_string = input("Enter The String You Want To Test : ")
    check = list(check_string)
    next_state = transition_table[initial_state][check[0]]
    for i in range(1, len(check)):
        next_state = transition_table[next_state][check[i]]
        print(next_state)
    if next_state in final_state:
        print("String is Accepted")
    else:
        print("String is not Accepted")
