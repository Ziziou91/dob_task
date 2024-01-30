"""Simple application to print out names and dates of birth from 'DOB.txt'."""
file_name = "./DOB.txt"

def app() -> None:
    """Reads DOB.txt file and organises the data before using it to call print_person."""
    name_dob_list = []
    with open(file_name, "r", encoding="UTF-8") as file:
        for line in file:
            person = line[:-1].split(" ", 2)
            new_line = [" ".join(person[:2])]+person[2:]
            name_dob_list.append(new_line)
                       
    print_person(name_dob_list, "Name")
    print("\n")
    print_person(name_dob_list, "Birthdate")



def print_person(input_list: list, input_type: str) -> None:
    """Loops through the given list and prints string depending on a given input_type string."""
    print(f"\033[1m{input_type}\033[0m")
    for val in input_list:
        if input_type == "Name":
            print(val[0])
        else:
            print(val[1])

print(f"{'*'*69}")
print(f"{'='*29}dob_task.py{'='*29}")
print(f"{'*'*69}\n")

app()

print(f"\n{'*'*69}")
print(f"{'='*27}dob_task.py END{'='*27}")
print(f"{'*'*69}\n")
