import random

def roll_dice(num_dice):
    results = [random.randint(1, 6) for _ in range(num_dice)]
    return results


def main():
    while True:
        try:
            num_dice = int(input("How many dice do you want to roll? "))
            if num_dice <= 0:
                print("Please enter a positive number of dice to roll.")
                continue
            
            dice_results = roll_dice(num_dice)
            
            print(f"Results of rolling {num_dice} dice:")
            for i, result in enumerate(dice_results, start=1):
                print(f"Die {i}: {result}")
        
            replay = input("Do you want to roll the dice again? (yes/no): ").lower()
            if replay != 'yes':
                print("THANK YOU FOR PLAYING")
                exit
                break
        
        except ValueError:
            print("Invalid input. Please enter a valid number of dice to roll.")


main()
