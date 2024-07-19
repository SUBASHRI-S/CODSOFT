import random

class RPSGame:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.user_score = 0
        self.computer_score = 0
        self.total_games = 0
        self.total_wins = 0
        self.total_losses = 0
        self.total_ties = 0

    def get_user_choice(self):
        while True:
            print("\nChoose one: Rock, Paper, or Scissors")
            user_choice = input("Your choice: ").strip().lower()
            if user_choice in self.choices:
                return user_choice
            else:
                print("Invalid choice! Please choose Rock, Paper, or Scissors.")

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            self.user_score += 1
            self.total_wins += 1
            return "You win!"
        else:
            self.computer_score += 1
            self.total_losses += 1
            return "Computer wins!"

    def play_game(self):
        while True:
            print("\nLet's play Rock-Paper-Scissors!")
            
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            
            print(f"\nYou chose: {user_choice}")
            print(f"Computer chose: {computer_choice}")
            
            result = self.determine_winner(user_choice, computer_choice)
            print(result)
            
            self.total_games += 1
            
            print(f"\nScores - You: {self.user_score}  Computer: {self.computer_score}")
            
            play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
            if play_again != 'yes':
                print("\nGame Statistics:")
                print(f"Total games played: {self.total_games}")
                print(f"Total wins: {self.total_wins}")
                print(f"Total losses: {self.total_losses}")
                print(f"Total ties: {self.total_ties}")
                print("\nThanks for playing!")
                break

if __name__ == "__main__":
    game = RPSGame()
    game.play_game()
