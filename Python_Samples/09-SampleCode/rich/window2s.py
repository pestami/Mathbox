from rich.console import Console
from rich.text import Text
from rich.panel import Panel
import os

console = Console()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    text = Text("This is a long text that can be scrolled.\n" * 20)
    while True:
        clear_console()
        console.print(Panel(text, title="Scrollable Window"))
        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            text = Text("You selected Option 1.\n" * 20)
        elif choice == "2":
            text = Text("You selected Option 2.\n" * 20)
        elif choice == "3":
            print("Exiting the application")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    main()