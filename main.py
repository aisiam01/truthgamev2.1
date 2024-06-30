import random
import time
import os

class TruthRevealerGame:
        def __init__(self):
            self.friends = []
            self.truth_questions = [
                "What's your biggest fear?",
                "What's your most embarrassing moment?",
                "What's a secret you've never told anyone?",
                "What's the biggest mistake you've ever made?",
                "What's your biggest regret in life?",
            ]

        def print_ascii_header(self):
            header = """
════════════════════════════════════════════
   Welcome to the Mystic Truth Revealer ════════════════════════════════════════════
🔮✨ Unveiling Truths, Deepening Connections ✨🔮
            """
            print(header)

        def print_header(self):
            os.system('cls' if os.name == 'nt' else 'clear')
            self.print_ascii_header()
            print("🤫 Uncover secrets, 🤝 forge connections, 🌟 and embrace the truth!\n")

        def print_menu(self):
            print("📜 Main Menu:")
            print("1️⃣ 🎭 Play a round")
            print("2️⃣ 👥 Manage friends")
            print("3️⃣ ❓ Manage questions")
            print("4️⃣ 🚪 Exit game")

        def add_friend(self):
            name = input("\n👤 Enter friend's name (or press Enter to cancel): ").strip()
            if name:
                self.friends.append(name)
                print(f"✅ {name} has been added to your circle of truth-seekers! 🎉")
            else:
                print("🔙 Friend addition canceled.")

        def remove_friend(self):
            if not self.friends:
                print("\n❌ You have no friends to remove. How lonely! 😢")
                return

            print("\n👥 Your current friends:")
            for i, friend in enumerate(self.friends, 1):
                print(f"{i}. 😊 {friend}")

            choice = input("\n🔢 Enter the number of the friend to remove (or press Enter to cancel): ").strip()
            if choice:
                try:
                    index = int(choice) - 1
                    if 0 <= index < len(self.friends):
                        removed_friend = self.friends.pop(index)
                        print(f"🚫 {removed_friend} has been removed from your circle. 👋")
                    else:
                        print("❌ Invalid friend number. 🤔")
                except ValueError:
                    print("❌ Please enter a valid number. 🧮")
            else:
                print("🔙 Friend removal canceled.")

        def manage_friends(self):
            while True:
                print("\n👥 Friend Management:")
                print("1️⃣ ➕ Add a friend")
                print("2️⃣ ➖ Remove a friend")
                print("3️⃣ 📋 View friends")
                print("4️⃣ 🔙 Back to main menu")

                choice = input("\n🔢 Enter your choice (1-4): ")

                if choice == '1':
                    self.add_friend()
                elif choice == '2':
                    self.remove_friend()
                elif choice == '3':
                    self.show_friends()
                elif choice == '4':
                    break
                else:
                    print("\n❌ Invalid choice. Please try again. 🤔")

        def show_friends(self):
            if not self.friends:
                print("\n❌ You have no friends. Time to socialize! 🎭")
            else:
                print("\n👥 Your circle of truth-seekers:")
                for i, friend in enumerate(self.friends, 1):
                    print(f"{i}. 😊 {friend}")

        def add_truth_question(self):
            questions = input("\n❓ Enter new truth question(s) separated by commas (or press Enter to cancel): ").strip()
            if questions:
                new_questions = [q.strip() for q in questions.split(',') if q.strip()]
                if new_questions:
                    self.truth_questions.extend(new_questions)
                    if len(new_questions) == 1:
                        print(f"✅ New truth question added: 💡 {new_questions[0]}")
                    else:
                        print(f"✅ {len(new_questions)} new truth questions added:")
                        for question in new_questions:
                            print(f"  • 💡 {question}")
                else:
                    print("❌ No valid questions entered. 🤔")
            else:
                print("🔙 Question addition canceled.")

        def remove_truth_question(self):
            if not self.truth_questions:
                print("\n❌ There are no truth questions to remove. 😮")
                return
            self.show_truth_questions()
            numbers = input("\n🔢 Enter the number(s) of the question(s) to remove, separated by commas (or press Enter to cancel): ").strip()
            if numbers:
                try:
                    indices = [int(num.strip()) - 1 for num in numbers.split(',') if num.strip()]
                    indices.sort(reverse=True)  # Sort in reverse order to remove from the end first
                    removed_questions = []
                    for index in indices:
                        if 0 <= index < len(self.truth_questions):
                            removed_questions.append(self.truth_questions.pop(index))
                        else:
                            print(f"❌ Invalid number: {index + 1}. Skipping. 🤔")

                    if removed_questions:
                        if len(removed_questions) == 1:
                            print(f"🚫 Removed question: 💡 {removed_questions[0]}")
                        else:
                            print(f"🚫 Removed {len(removed_questions)} questions:")
                            for question in removed_questions:
                                print(f"  • 💡 {question}")
                    else:
                        print("❌ No valid questions were removed. 😕")
                except ValueError:
                    print("❌ Please enter valid numbers separated by commas. 🧮")
            else:
                print("🔙 Question removal canceled.")

        def show_truth_questions(self):
            if not self.truth_questions:
                print("\n❌ There are no truth questions. Add some to spice up the game! 🌶️")
            else:
                print("\n❓ Current truth questions:")
                for i, question in enumerate(self.truth_questions, 1):
                    print(f"{i}. 💡 {question}")

        def manage_questions(self):
            while True:
                print("\n❓ Question Management:")
                print("1️⃣ ➕ Add a question")
                print("2️⃣ ➖ Remove a question")
                print("3️⃣ 📋 View questions")
                print("4️⃣ 🔙 Back to main menu")

                choice = input("\n🔢 Enter your choice (1-4): ")

                if choice == '1':
                    self.add_truth_question()
                elif choice == '2':
                    self.remove_truth_question()
                elif choice == '3':
                    self.show_truth_questions()
                elif choice == '4':
                    break
                else:
                    print("\n❌ Invalid choice. Please try again. 🤔")

        def play_round(self):
            if not self.friends:
                print("\n❌ You need friends to play! Add some friends first. 👥")
                return

            if not self.truth_questions:
                print("\n❌ You need truth questions to play! Add some questions first. ❓")
                return

            print("\n🎭 Let the truth be unveiled! 🌟")
            time.sleep(1)

            friend = random.choice(self.friends)
            question = random.choice(self.truth_questions)

            print(f"\n🎯 {friend}, prepare to face the truth! 😮")
            time.sleep(1)
            print(f"\n❓ {question}")

            input("\n⏳ Press Enter when the truth has been spoken...")
            print("\n✨ The truth has been revealed, and bonds have deepened! 🤝")

        def play_game(self):
            while True:
                self.print_header()
                self.print_menu()

                choice = input("\n🔢 Enter your choice (1-4): ")

                if choice == '1':
                    self.play_round()
                elif choice == '2':
                    self.manage_friends()
                elif choice == '3':
                    self.manage_questions()
                elif choice == '4':
                    print("\n🙏 Thank you for seeking the truth. Until we meet again! 👋✨")
                    break
                else:
                    print("\n❌ Invalid choice. The spirits are confused. Try again. 🤔")

                input("\n⏳ Press Enter to continue...")

if __name__ == "__main__":
        game = TruthRevealerGame()
        game.play_game()
