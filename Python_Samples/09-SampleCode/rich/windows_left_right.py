from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
import os

console = Console()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')



def main():
    
    1
    clear_console()
    
    left_text = "[bold magenta]Left Window[/bold magenta]\nThis is the left window."
    right_text = "[bold cyan]Right Window[/bold cyan]\nThis is the right window."

    while True:
        
        left_text_panel = Panel(left_text, title="Left")
        right_text_panel = Panel(right_text, title="Right")
        console.print(Columns([left_text_panel, right_text_panel]))
        choice = input("Enter your choice (1/2/3): ")


        if choice == "1":
            left_text = "[bold magenta]Left Window[/bold magenta]\n......................You selected Option 1"
            left_text =left_text + "\nYou selected Option 1"
        elif choice == "2":
            right_text = "[bold cyan]Right Window[/bold cyan]\n.....................You selected Option 2"
        elif choice == "3":
            print("Exiting the application")
            break
        else:
            print("Invalid choice. Please try again.")
1

if __name__ == "__main__":
    main()