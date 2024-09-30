from functions import get_todos, write_todos
import time


now = time.strftime("%b %d, %y %H:%M:%S")
print("It is", now)

while True:
    action = input("Type add, show, edit, sort, complete or exit: ")
    action = action.strip()

    #match action:
    if 'add' in action:
        try:
           todo = input("What is your ToDo: ") + "\n"

           todos = get_todos("todos.txt")

           todos.append(todo)
           write_todos("todos.txt",todos)
        except ValueError:
            print("Wrong comand")
    elif 'show' in action:
        try:
            todos = get_todos("todos.txt")

            if todos == []:
                print("no todos")
            else:
                for index,item in enumerate(todos):
                    item = item.strip('\n')
                    row = f"{index + 1}-{item.capitalize()}"
                    print(row)
                #x = 1
                #for item in todos:
                   #print(str(x) + ": " + item.capitalize())
                   #x = x + 1
        except ValueError:
            print("Wrong comand")
    elif 'edit' in action:
        try:
            number = int(input("To do Number? "))
            number = number - 1
            todos = get_todos("todos.txt")

            new_todo = input("enter to do")
            todos[number] = new_todo + '\n'
            write_todos("todos.txt", todos)
        except ValueError:
            print("Wrong comand")


    elif 'complete' in action:
        try:
            todos = get_todos("todos.txt")  # Load the list of todos
            if not todos:  # If the todos list is empty
                print("Please first add a ToDo")
            else:
                number_C = int(input("To do Number? "))

                if number_C == 0:  # Check if the user entered 0
                    print("Invalid number: To-do numbers start from 1.")
                elif number_C > len(todos) or number_C < 1:
                    print(f"Invalid number: Please enter a number between 1 and {len(todos)}.")
                else:
                    number_C -= 1  # Adjust for 0-based indexing
                    todos.pop(number_C)
                    write_todos("todos.txt", todos)
                    print("List Updated")
                    for idx, item in enumerate(todos, start=1):
                        print(f"{idx}: {item.capitalize()}")

        except ValueError:

            print("Invalid input: Please enter a valid number.")
        except IndexError:
            print("wrong command")


    elif 'sort' in action:
        try:
            sort = input("Sort by alphabetical or reverse")
            if True:
                match sort:
                    case 'alphabetical':
                        todos.sort()
                        if todos == []:
                            print("no todos")

                        else:
                            x = 1
                            print("List Updated")
                            for item in todos:
                                print(str(x) + ": " + item.capitalize())
                                x = x + 1


                    case 'reverse':
                        todos.sort(reverse=True)
                        if todos == []:
                            print("no todos")

                        else:
                            x = 1
                            print("List Updated")
                            for item in todos:
                                print(str(x) + ": " + item.capitalize())
                                x = x + 1


                    #case  _:
                        #print("enter valid comand")
        except ValueError:
            print("Wrong comand")

    elif 'exit' in action:
        print("Bye")
        exit()

    else:
        print("type somthing correct")




