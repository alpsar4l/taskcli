import os
import json
import time
from colorama import Fore, Style, init, Back

init(autoreset=True)


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def tasks():
    clear_terminal()
    print(f"{Style.BRIGHT}{Fore.CYAN}Tasks:\n{Style.RESET_ALL}")

    if not task_list:
        print(Fore.YELLOW + "   You have no tasks.")
    else:
        for i, task in enumerate(task_list, start=1):
            status = (
                Back.GREEN + "Completed"
                if task["completed"]
                else Back.RED + "Not Completed"
            )
            print(
                f"   [{Fore.GREEN}{Style.BRIGHT}{i}{Style.RESET_ALL}]: {Style.RESET_ALL}{task['name']} - {status}"
            )

        choice = input(
            Fore.YELLOW
            + "\nEnter the number of the task to select (Enter '-' to return to the main menu): "
        )
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(task_list):
                toggle_task_status(index)


def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(task_list, file, indent=4)


def new_task():
    clear_terminal()

    task_name = input(f"{Fore.CYAN}{Style.BRIGHT}Add a new task:{Style.RESET_ALL} ")
    task_list.append({"name": task_name, "completed": False})

    save_tasks()
    tasks()


def toggle_task_status(index):
    clear_terminal()
    task = task_list[index]
    task["completed"] = not task["completed"]
    save_tasks()

    print(f"{Fore.CYAN}Task status updated to {Style.BRIGHT}{'Completed' if task['completed'] else 'Not Completed'}{Style.RESET_ALL}{Fore.CYAN}:\n")
    print(f"   {task['name']}")
    toggle_choice = input(f"\n{Fore.GREEN}Press {Style.RESET_ALL}{Style.BRIGHT}t{Style.RESET_ALL}{Fore.GREEN} to toggle the status again, press {Style.RESET_ALL}{Style.BRIGHT}Enter{Style.RESET_ALL}{Fore.GREEN} to exit: {Style.RESET_ALL}").strip().lower()

    if toggle_choice == "t":
        toggle_task_status(index)
    else:
        tasks()


task_list = load_tasks()


def main_menu():
    try:
        while True:
            clear_terminal()

            user_name = os.getlogin()

            print(f"{Fore.GREEN}Hello {Style.RESET_ALL}{Style.BRIGHT}{user_name}{Style.RESET_ALL}{Fore.GREEN}, you have {Style.RESET_ALL}{Style.BRIGHT}{len([t for t in task_list if not t['completed']])}{Style.RESET_ALL}{Fore.GREEN} tasks.\n")
            print(f"[{Fore.GREEN}0{Style.RESET_ALL}] List tasks \n[{Fore.GREEN}1{Style.RESET_ALL}] Add new \n[{Fore.GREEN}-{Style.RESET_ALL}] Return to menu \n[{Fore.GREEN}8{Style.RESET_ALL}] Exit program")

            choice = input("")

            if choice == "0":
                tasks()
            elif choice == "1":
                new_task()
            elif choice == "-":
                continue
            elif choice == "8":
                print(Fore.YELLOW + "Exiting program...")
                break
            else:
                print(Fore.YELLOW + "Invalid choice, please try again.")
                time.sleep(0.5)

    except KeyboardInterrupt:
        print(Fore.YELLOW + "\nExiting program...")


if __name__ == "__main__":
    main_menu()
