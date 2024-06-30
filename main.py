import random
import time
import os
from colorama import init, Fore, Back, Style

init(autoreset=True)

class TextTruthGame:
    # ... (previous methods remain the same)

    def add_truth_question(self):
        questions = input(Fore.GREEN + "\n❓ Enter new truth question(s) separated by commas (or press Enter to cancel): ").strip()
        if questions:
            new_questions = [q.strip() for q in questions.split(',') if q.strip()]
            if new_questions:
                self.truth_questions.extend(new_questions)
                if len(new_questions) == 1:
                    print(Fore.CYAN + f"✅ New truth question added: {new_questions[0]}")
                else:
                    print(Fore.CYAN + f"✅ {len(new_questions)} new truth questions added:")
                    for question in new_questions:
                        print(Fore.YELLOW + f"  • {question}")
            else:
                print(Fore.RED + "❌ No valid questions entered.")
        else:
            print(Fore.CYAN + "🔙 Question addition canceled.")

    def remove_truth_question(self):
        if not self.truth_questions:
            print(Fore.RED + "\n❌ There are no truth questions to remove.")
            return

        self.show_truth_questions()
        numbers = input(Fore.YELLOW + "\n🔢 Enter the number(s) of the question(s) to remove, separated by commas (or press Enter to cancel): ").strip()
        if numbers:
            try:
                indices = [int(num.strip()) - 1 for num in numbers.split(',') if num.strip()]
                indices.sort(reverse=True)  # Sort in reverse order to remove from the end first
                removed_questions = []
                for index in indices:
                    if 0 <= index < len(self.truth_questions):
                        removed_questions.append(self.truth_questions.pop(index))
                    else:
                        print(Fore.RED + f"❌ Invalid number: {index + 1}. Skipping.")
                
                if removed_questions:
                    if len(removed_questions) == 1:
                        print(Fore.RED + f"🚫 Removed question: {removed_questions[0]}")
                    else:
                        print(Fore.RED + f"🚫 Removed {len(removed_questions)} questions:")
                        for question in removed_questions:
                            print(Fore.YELLOW + f"  • {question}")
                else:
                    print(Fore.RED + "❌ No valid questions were removed.")
            except ValueError:
                print(Fore.RED + "❌ Please enter valid numbers separated by commas.")
        else:
            print(Fore.CYAN + "🔙 Question removal canceled.")

    # ... (other methods remain the same)

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
