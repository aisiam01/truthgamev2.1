import random
import time
import os
from colorama import init, Fore, Back, Style

init(autoreset=True)

class TextTruthGame:
    def __init__(self):
        self.friends = []
        self.truth_questions = [
            "What's your biggest fear?",
            "What's the most embarrassing thing you've ever done?",
            "If you could have any superpower, what would it be and why?",
            "What's your biggest regret?",
            "If you could swap lives with anyone for a day, who would it be?",
            "What's the weirdest dream you've ever had?",
            "What's your most prized possession?",
            "If you could travel anywhere in the world, where would you go?",
            "What's the best piece of advice you've ever received?",
            "What's your most unusual talent?"
        ]

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_header(self):
        self.clear_screen()
        print(Fore.CYAN + Style.BRIGHT + """
        ╔══════════════════════════════════════════════╗
        ║      Welcome to the Mystic Truth Revealer    ║
        ╚══════════════════════════════════════════════╝
        """)

    def print_menu(self):
        print(Fore.YELLOW + """
        📜 Main Menu 📜
        1. 🎭 Play a round of Truth
        2. 👥 Manage Friends
        3. ❓ Manage Truth Questions
        4. 🚪 Quit
        """)

    def manage_friends(self):
        while True:
            self.clear_screen()
            print(Fore.CYAN + "\n👥 Friend Management")
            print(Fore.YELLOW + """
            1. ➕ Add friend(s)
            2. ➖ Remove a friend
            3. 📋 Show all friends
            4. 🔙 Back to main menu
            """)
            choice = input(Fore.GREEN + "Enter your choice (1-4): ").strip()

            if choice == '1':
                self.add_friend()
            elif choice == '2':
                self.remove_friend()
            elif choice == '3':
                self.show_friends()
            elif choice == '4':
                print(Fore.CYAN + "🔙 Returning to main menu...")
                break
            else:
                print(Fore.RED + "❌ Invalid choice. Please try again.")

            input(Fore.YELLOW + "\nPress Enter to continue...")

    def add_friend(self):
        names = input(Fore.GREEN + "\n👥 Enter friend name(s) separated by commas (or press Enter to cancel): ").strip()
        if names:
            new_friends = [name.strip() for name in names.split(',') if name.strip()]
            if new_friends:
                self.friends.extend(new_friends)
                if len(new_friends) == 1:
                    print(Fore.CYAN + f"✅ {new_friends[0]} has joined the circle of truth!")
                else:
                    print(Fore.CYAN + f"✅ {len(new_friends)} friends have joined the circle of truth!")
                    for friend in new_friends:
                        print(Fore.YELLOW + f"  • {friend}")
            else:
                print(Fore.RED + "❌ No valid names entered.")
        else:
            print(Fore.CYAN + "🔙 Friend addition canceled.")

    def remove_friend(self):
        if not self.friends:
            print(Fore.RED + "\n❌ The circle is empty. There are no friends to remove.")
            return

        self.show_friends()
        while True:
            choice = input(Fore.YELLOW + "\n🔢 Enter the number of the friend to remove (or press Enter to cancel): ").strip()
            if not choice:
                print(Fore.CYAN + "🔙 Friend removal canceled.")
                return
            try:
                index = int(choice) - 1
                if 0 <= index < len(self.friends):
                    removed_friend = self.friends.pop(index)
                    print(Fore.RED + f"🚫 {removed_friend} has been removed from the circle of truth.")
                    return
                else:
                    print(Fore.RED + "❌ Invalid number. Please try again.")
            except ValueError:
                print(Fore.RED + "❌ Please enter a valid number.")

    def show_friends(self):
        if self.friends:
            print(Fore.CYAN + "\n👥 Friends in the circle of truth:")
            for i, friend in enumerate(self.friends, 1):
                print(Fore.YELLOW + f"  {i}. {friend}")
        else:
            print(Fore.RED + "\n👥 The circle awaits its first truth-seeker.")

    def manage_questions(self):
        while True:
            self.clear_screen()
            print(Fore.CYAN + "\n❓ Truth Question Management")
            print(Fore.YELLOW + """
            1. ➕ Add a truth question
            2. ➖ Remove a truth question
            3. 📋 Show all truth questions
            4. 🔙 Back to main menu
            """)
            choice = input(Fore.GREEN + "Enter your choice (1-4): ").strip()

            if choice == '1':
                self.add_truth_question()
            elif choice == '2':
                self.remove_truth_question()
            elif choice == '3':
                self.show_truth_questions()
            elif choice == '4':
                print(Fore.CYAN + "🔙 Returning to main menu...")
                break
            else:
                print(Fore.RED + "❌ Invalid choice. Please try again.")

            input(Fore.YELLOW + "\nPress Enter to continue...")

    def add_truth_question(self):
        question = input(Fore.GREEN + "\n❓ Enter a new truth question (or press Enter to cancel): ").strip()
        if question:
            self.truth_questions.append(question)
            print(Fore.CYAN + f"✅ New truth question added: {question}")
        else:
            print(Fore.CYAN + "🔙 Question addition canceled.")

    def remove_truth_question(self):
        if not self.truth_questions:
            print(Fore.RED + "\n❌ There are no truth questions to remove.")
            return

        self.show_truth_questions()
        while True:
            choice = input(Fore.YELLOW + "\n🔢 Enter the number of the question to remove (or press Enter to cancel): ").strip()
            if not choice:
                print(Fore.CYAN + "🔙 Question removal canceled.")
                return
            try:
                index = int(choice) - 1
                if 0 <= index < len(self.truth_questions):
                    removed_question = self.truth_questions.pop(index)
                    print(Fore.RED + f"🚫 Removed question: {removed_question}")
                    return
                else:
                    print(Fore.RED + "❌ Invalid number. Please try again.")
            except ValueError:
                print(Fore.RED + "❌ Please enter a valid number.")

    def show_truth_questions(self):
        if self.truth_questions:
            print(Fore.CYAN + "\n📋 Current Truth Questions:")
            for i, question in enumerate(self.truth_questions, 1):
                print(Fore.YELLOW + f"  {i}. {question}")
        else:
            print(Fore.RED + "\n❓ There are no truth questions. Add some to start playing!")

    def play_round(self):
        if not self.friends:
            print(Fore.RED + "\n❌ The circle is empty. Invite some friends first!")
            return
        if not self.truth_questions:
            print(Fore.RED + "\n❌ There are no truth questions. Add some questions first!")
            return

        print(Fore.CYAN + "\n🎲 The wheel of fate is spinning...")
        self.spinning_animation()
        selected_friend = random.choice(self.friends)
        question = random.choice(self.truth_questions)

        print(Fore.MAGENTA + f"\n🌟 {selected_friend}, the spirits have chosen you!")
        time.sleep(1)
        print(Fore.YELLOW + Style.BRIGHT + f"\n❓ Your truth question is: {question}")

        input(Fore.GREEN + "\nPress Enter when the truth has been revealed...")

    def spinning_animation(self):
        spinner = "|/-\\"
        for _ in range(10):
            for char in spinner:
                print(Fore.CYAN + f"\r{char} Spinning...", end="", flush=True)
                time.sleep(0.1)
        print()

    def play_game(self):
        while True:
            self.print_header()
            self.print_menu()

            choice = input(Fore.GREEN + "\n🔢 Enter your choice (1-4): ")

            if choice == '1':
                self.play_round()
            elif choice == '2':
                self.manage_friends()
            elif choice == '3':
                self.manage_questions()
            elif choice == '4':
                print(Fore.MAGENTA + "\n🙏 Thank you for seeking the truth. Until we meet again!")
                break
            else:
                print(Fore.RED + "\n❌ Invalid choice. The spirits are confused. Try again.")

            input(Fore.YELLOW + "\nPress Enter to continue...")

if __name__ == "__main__":
    game = TextTruthGame()
    game.play_game()