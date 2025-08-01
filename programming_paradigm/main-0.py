# main-0.py

import sys
from bank_account import BankAccount

def main():
    # Tu peux changer le solde initial ici pour tester d'autres scénarios
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command_part = sys.argv[1]
    if ':' in command_part:
        command, amount_str = command_part.split(':', 1)
    else:
        command = command_part
        amount_str = None

    command = command.lower()

    if command == "deposit" and amount_str is not None:
        account.deposit(amount_str)
        print(f"Deposited: ${amount_str}")
    elif command == "withdraw" and amount_str is not None:
        success = account.withdraw(amount_str)
        if success:
            print(f"Withdrew: ${amount_str}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command. Usage examples:")
        print("  python main-0.py deposit:50")
        print("  python main-0.py withdraw:20")
        print("  python main-0.py display")

if __name__ == "__main__":
    main()
