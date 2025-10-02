import random

class Lottery:
    def __init__(self):
        self.winning_numbers = set(random.sample(range(1, 61), 6))

    def display_winning(self):
        return sorted(self.winning_numbers)


class Player:
    def __init__(self):
        self.numbers = set()

    def choose_numbers(self):
        print("Enter 6 numbers between 1–60:")
        while len(self.numbers) < 6:
            try:
                num = int(input(f"Number {len(self.numbers)+1}: "))
                if 1 <= num <= 60:
                    if num in self.numbers:
                        print("Duplicate! Try another.")
                    else:
                        self.numbers.add(num)
                else:
                    print("Invalid! Must be 1–60.")
            except ValueError:
                print("Enter a valid number.")

    def check_prize(self, lottery):
        matches = self.numbers & lottery.winning_numbers
        count = len(matches)
        prize = 1_000_000 if count == 6 else count * 1000
        return matches, count, prize


# ---- Main Program ----
def main():
    lotto = Lottery()
    player = Player()

    player.choose_numbers()
    matches, count, prize = player.check_prize(lotto)

    print("\n--- LOTTERY RESULTS ---")
    print("Winning Numbers:", lotto.display_winning())
    print("Your Numbers:", sorted(player.numbers))
    print("Matches:", sorted(matches) if matches else "None")
    print("Total Matches:", count)
    print(f"Prize: ₱{prize:,}")


if __name__ == "__main__":
    main()
