print("To Do App")


print("Do you wish to add a task?")
option = input("if yes input y, if no input n:")
if option == "y":
    task_1 = input("Input Task 1: ")
    print(task_1)
    task_2 = input("Input Task 2: ")
    print(task_2)

    to_do_list = {task_1, task_2}
    print(to_do_list)
    print("This is your to do list:")
    print(task_1)
    print(task_2)
else:
    print("Thank you,this is your to do list for the day.")