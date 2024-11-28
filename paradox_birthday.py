import random

def has_duplicates(birthdays):
    return len(birthdays) != len(set(birthdays))

def generate_birthdays(num_people):
    return [random.randint(1, 365) for _ in range(num_people)]

def birthday_paradox_simulation(num_people, num_simulations):
    duplicate_count = 0
    for _ in range(num_simulations):
        birthdays = generate_birthdays(num_people)
        if has_duplicates(birthdays):
            duplicate_count += 1
    return duplicate_count / num_simulations

if __name__ == "__main__":
    num_people = 23
    num_simulations = 10000
    probability = birthday_paradox_simulation(num_people, num_simulations)
    print(f"Probability of at least two people sharing a birthday in a group of {num_people}: {probability:.2f}")