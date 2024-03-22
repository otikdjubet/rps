MAX_LINES =3
MAX_BET = 100
MIN_BET = 1

def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number")
    return amount

def get_lines():
    while True:
        lines = input("How many lines would you like to bet on (From 1 - " + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number")
    return lines

def get_bet():
    while True:
        bet = input(f"How much would you like to bet (From ${MIN_BET} - ${MAX_BET}? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print("Enter a valid bet.")
        else:
            print("Please enter a number")
    return bet

def main():
    balance = deposit()
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You dont have enough balance. Your current balance is ${balance}")
        else:
            break
    new_bal = balance - total_bet
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}. Remaining balance is ${new_bal}" )


main()