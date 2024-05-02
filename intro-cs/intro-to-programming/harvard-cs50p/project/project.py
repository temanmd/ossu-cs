import re
import sys
from errors import AccountIsFrozenError, AccountNotFoundError, OutOfMoneyError
from terminal_colors import TColors
from data_functions import (
    get_accounts,
    get_account,
    add_account,
    freeze_account,
    unfreeze_account,
    change_account_name,
    deposit,
    withdraw,
    init,
)


GOODBYE_TEXT = "Good bye!"


def welcome_info(bank_name):
    return (
        f'Welcome to "{bank_name}" bank!\n\n'
        "You can manage your bank with commands:\n\n"
        f"    {TColors.BOLD}show all{TColors.ENDC} (show all accounts)\n"
        f"    {TColors.BOLD}show{TColors.ENDC} 1 (show individual account by id)\n"
        f'    {TColors.BOLD}add{TColors.ENDC} "Name" (add new account with name)\n'
        f'    {TColors.BOLD}change{TColors.ENDC} 1 "New Name" (change account\'s name by id)\n'
        f"    {TColors.BOLD}freeze{TColors.ENDC} 1 (freeze an account by id)\n"
        f"    {TColors.BOLD}unfreeze{TColors.ENDC} 1 (unfreeze an account by id)\n"
        f"    {TColors.BOLD}deposit{TColors.ENDC} 1 12_000 (deposit account's balance by id)\n"
        f"    {TColors.BOLD}withdraw{TColors.ENDC} 1 5_000 (withdraw account's balance by id)\n"
        f"    {TColors.BOLD}help{TColors.ENDC} (show this message again)\n"
        f"    {TColors.BOLD}exit{TColors.ENDC} (exit the program)"
    )


def validate_command(command):
    regex = (
        r"^(show all|"
        r"show \d+|"
        r"add \"([a-zA-Z]|\s)+\"|"
        r"change \d+ \"([a-zA-Z]|\s)+\"|"
        r"freeze \d+|"
        r"unfreeze \d+|"
        r"deposit \d+ (\d|_)+|"
        r"withdraw \d+ (\d|_)+|"
        r"help|exit)$"
    )

    if not re.search(regex, command):
        print(
            f'\n{TColors.FAIL}Invalid command using, to show valid using format, type "help"{TColors.ENDC}'
        )
        return False

    return True


def process_show_action(params, bank):
    if params[0] == "all":
        print(get_accounts(bank=bank))
    else:
        print(get_account(int(params[0]), bank=bank))


def process_add_action(params, bank):
    name_parts = []
    for part in params:
        name_parts.append(part.strip('"'))
    name = " ".join(name_parts)
    account = add_account({"name": name}, bank=bank)
    print(account)


def process_change_action(params, bank):
    id = int(params[0])
    name_parts = []
    for part in params[1:]:
        name_parts.append(part.strip('"'))
    name = " ".join(name_parts)
    account = change_account_name(id, new_name=name, bank=bank)
    print(account)


def process_freeze_action(params, bank):
    id = int(params[0])
    account = freeze_account(id, bank=bank)
    print(account)


def process_unfreeze_action(params, bank):
    id = int(params[0])
    account = unfreeze_account(id, bank=bank)
    print(account)


def process_deposit_action(params, bank):
    id = int(params[0])
    amount = int(params[1])
    print(deposit(id, amount=amount, bank=bank))


def process_withdraw_action(params, bank):
    id = int(params[0])
    amount = int(params[1])
    print(withdraw(id, amount=amount, bank=bank))


def process_bank_with_command(command, bank):
    print()
    parts = command.split()
    action = parts[0]
    params = parts[1:]

    try:
        match action:
            case "show":
                process_show_action(params, bank)
            case "add":
                process_add_action(params, bank)
            case "change":
                process_change_action(params, bank)
            case "freeze":
                process_freeze_action(params, bank)
            case "unfreeze":
                process_unfreeze_action(params, bank)
            case "deposit":
                process_deposit_action(params, bank)
            case "withdraw":
                process_withdraw_action(params, bank)
            case "help":
                print(welcome_info(bank["name"]))
            case "exit":
                sys.exit(GOODBYE_TEXT)
            case _:
                print(f"{TColors.FAIL}Very odd error{TColors.ENDC}")
                return
    except AccountNotFoundError as error:
        print(f"{TColors.WARNING}Account with id={error} not found{TColors.ENDC}")
    except AccountIsFrozenError as error:
        print(f"{TColors.WARNING}Account with id={error} is frozen{TColors.ENDC}")
    except OutOfMoneyError as error:
        print(
            f"{TColors.WARNING}Account with id={error.args[0]} has insufficient funds\n"
            f"Balance: {error.args[1]}{TColors.ENDC}"
        )


def main():
    try:
        bank_name = input("Input bank name: ").strip()
    except (KeyboardInterrupt, EOFError):
        sys.exit(f"\n\n{GOODBYE_TEXT}")
    print()
    bank = init(bank_name)
    print(welcome_info(bank_name))

    while True:
        try:
            command = input(
                f"\n{TColors.UNDERLINE}Input command:{TColors.ENDC} "
            ).strip()
            if validate_command(command):
                process_bank_with_command(command, bank=bank)
        except (KeyboardInterrupt, EOFError):
            sys.exit(f"\n\n{GOODBYE_TEXT}")


if __name__ == "__main__":
    main()
