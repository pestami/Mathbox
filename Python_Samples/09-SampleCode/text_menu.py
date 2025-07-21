#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SESA237770
#
# Created:     15.07.2025
# Copyright:   (c) SESA237770 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


class ConsoleApp:
    def __init__(self):
        self.menu_options = {
            "1": {"name": "Option 1", "action": self.option1},
            "2": {"name": "Option 2", "action": self.option2},
            "3": {"name": "Exit", "action": self.exit_app}
        }

    def display_menu(self):
        print("\n--- Menu ---")
        for key, value in self.menu_options.items():
            print(f"{key}. {value['name']}")

    def option1(self):
        print("You selected Option 1")

    def option2(self):
        print("You selected Option 2")

    def exit_app(self):
        print("Exiting the application")
        exit()

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice in self.menu_options:
                self.menu_options[choice]["action"]()
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = ConsoleApp()
    app.run()
