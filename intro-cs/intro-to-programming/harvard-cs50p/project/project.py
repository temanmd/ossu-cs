import re
import sys
from errors import AccountIsFrozenError, AccountNotFoundError, OutOfMoneyError
from terminal_colors import TColors


GOODBYE_TEXT = "Good bye!"


def get_ids(bank):
    return sorted(map(lambda account: account["id"], bank["accounts"]))


def get_accounts(bank):
    return bank["accounts"]


def add_account(info, bank):
    ids = get_ids(bank)
    new_id = ids[-1] + 1 if ids else 1
    new_account = {"id": new_id, "name": info["name"], "balance": 0, "status": "active"}
    bank["accounts"].append(new_account)
    return new_account


def get_account(id, bank):
    ids = get_ids(bank)
    if id in ids:
        return list(filter(lambda account: account["id"] == id, bank["accounts"]))[0]
    else:
        raise AccountNotFoundError(id)


def freeze_account(id, bank):
    account = get_account(id, bank=bank)
    if account["status"] != "frozen":
        index = bank["accounts"].index(account)
        account["status"] = "frozen"
        bank["accounts"][index] = account
    return account


def unfreeze_account(id, bank):
    account = get_account(id, bank=bank)
    if account["status"] == "frozen":
        index = bank["accounts"].index(account)
        account["status"] = "active"
        bank["accounts"][index] = account
    return account


def change_account_name(id, new_name, bank):
    account = get_account(id, bank=bank)
    index = bank["accounts"].index(account)
    account["name"] = new_name
    bank["accounts"][index] = account
    return account


def deposit(id, amount, bank):
    account = get_account(id, bank=bank)
    if account["status"] == "frozen":
        raise AccountIsFrozenError(id)
    index = bank["accounts"].index(account)
    account["balance"] += amount
    bank["accounts"][index] = account
    return account


def withdraw(id, amount, bank):
    account = get_account(id, bank=bank)
    if account["balance"] < amount:
        raise OutOfMoneyError(id, account["balance"])
    if account["status"] == "frozen":
        raise AccountIsFrozenError(1)
    index = bank["accounts"].index(account)
    account["balance"] -= amount
    bank["accounts"][index] = account
    return account


def init(bank_name):
    bank = {
        "name": bank_name.strip(),
        "accounts": [],
    }
    account = add_account({"name": "Boss"}, bank=bank)
    deposit(account["id"], amount=80_000_000_000, bank=bank)
    return bank


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


def render_accounts(accounts):
    print(accounts)


def render_account(id, bank):
    print(get_account(id, bank=bank))


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
        render_accounts(bank["accounts"])
    else:
        render_account(int(params[0]), bank)


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
