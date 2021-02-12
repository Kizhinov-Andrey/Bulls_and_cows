from itertools import permutations
from random import sample

# Here we will store all responses to the user
# in the format (past number, the number entered by the user, bulls, cows).
RESPONSE = []


def best_n(user_n):  # A function that will calculate the best number for a given situation.
    if RESPONSE:
        # Create all possible variations of numbers.
        options = [el for el in permutations(RESPONSE[-1][0], 4) if el[0] != 0]
        # There will be numbers that fit our story.
        approach = []
        for n in options:  # For all numbers in options.
            for task in RESPONSE:
                # If some test returns incorrect results, then we end the loop.
                if score(n, task[1]) != (task[2], task[3]):
                    break
            else:
                # If the loop ran smoothly,
                # then we add our number to the options along with the bulls and cows for it.
                bull, cow = score(n, user_n)
                approach.append((list(n), bull, cow))
        # Return the best number.
        return sorted(approach, key=lambda pair: (pair[1], pair[2]))[0]
    else:  # If it is the first number, then we can find such n that all numbers will be different.
        n = create_new_n()
        while score(n, user_n) != (0, 0):
            n = create_new_n()
        return n, 0, 0


def score(n, user_n):  # Returns the number of bulls and cows for the given number.
    bull = 0
    cow = 0
    for i in range(4):
        if n[i] == user_n[i]:
            bull += 1
        elif user_n[i] in n:
            cow += 1
    return bull, cow


def create_new_n():  # A function that returns a new number without leading zeros.
    data = range(10)
    n = sample(data, 4)
    while n[0] == 0:
        n = sample(data, 4)
    return n


def main():
    user_n = list(map(int, input()))
    n, bull, cow = best_n(user_n)
    print(f'Bulls {bull}, cows {cow}.')
    while bull != 4:
        RESPONSE.append((n, user_n, bull, cow))
        user_n = list(map(int, input()))
        n, bull, cow = best_n(user_n)
        print(f'Bulls {bull}, cows {cow}.')
    print('You win')


if __name__ == '__main__':
    main()
