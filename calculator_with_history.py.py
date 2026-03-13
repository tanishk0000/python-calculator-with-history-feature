history = "HISTORY_FILE.txt"

def show_history():
    lines = open(history, "r").readlines()

    if len(lines) == 0:
        print("Sorry! there is no history present")
    else:
        for line in reversed(lines):
            print(line.strip())

def clear_history():
    open(history, "w").close()
    print("Calculator history deleted")

def write_history(equation, result):
    files = open(history, "a")
    files.write(equation + "=" + str(result) + "\n")
    files.close()

def calculate(user_input):
    parts = user_input.split()

    if len(parts) != 3:
        print("Invalid format please use example: (8 + 8)")
        return

    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero")
            return
        else:
            result = num1 / num2

    print(result)
    write_history(user_input, result)

def main():
    user_Calc = input("Please enter calculation like (2 + 2)\n")
    calculate(user_Calc)

    user_choice = input("Press 'c' to clear history or 'w' to watch history: ")

    if user_choice == "c":
        clear_history()
    elif user_choice == "w":
        show_history()

main()