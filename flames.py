class FlamesGame:
    def __init__(self, name1, name2):
        self.name1 = name1.lower().replace(" ", "")
        self.name2 = name2.lower().replace(" ", "")
        self.flames = ["Friendship", "Love", "Affection", "Marriage", "Enemy", "Sibling"]

    def common_letters(self):
        n1, n2 = list(self.name1), list(self.name2)
        
        # Removing common characters from both names
        for ch in self.name1:
            if ch in n2:
                n1.remove(ch)
                n2.remove(ch)

        remaining1 = "".join(n1)
        remaining2 = "".join(n2)
        count = len(n1) + len(n2)

        return count, remaining1, remaining2

    def compute_result(self):
        count, remaining1, remaining2 = self.common_letters()

        # Show the remaining characters and their count
        print(f"\nRemaining characters after removal:")
        print(f"Name 1 remaining: {remaining1} (Count: {len(remaining1)})")
        print(f"Name 2 remaining: {remaining2} (Count: {len(remaining2)})")
        print(f"Total remaining characters: {count}")

        # Special case: all letters removed
        if count == 0:
            return "Not compatible! Single forever </3"

        index = 0
        while len(self.flames) > 1:
            index = (index + count - 1) % len(self.flames)
            self.flames.pop(index)

        return self.flames[0]


# ---- Main Program ----
def main():
    print(" Welcome to the Mating Game (FLAMES) ")
    name1 = input("Enter your name: ")
    name2 = input("Enter partner's name: ")

    game = FlamesGame(name1, name2)
    result = game.compute_result()

    print("\n--- RESULT ---")
    print(f"Relationship between you and your crush is: {result}")


if __name__ == "__main__":
    main()
