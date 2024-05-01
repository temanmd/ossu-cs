class TColors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class AccountIsFrozenError(Exception):
    pass


class AccountNotFoundError(Exception):
    pass


class OutOfMoneyError(Exception):
    pass


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
        raise AccountNotFoundError()


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
        raise AccountIsFrozenError()
    index = bank["accounts"].index(account)
    account["balance"] += amount
    bank["accounts"][index] = account
    return account


def withdraw(id, amount, bank):
    account = get_account(id, bank=bank)
    if account["balance"] < amount:
        raise OutOfMoneyError()
    if account["status"] == "frozen":
        raise AccountIsFrozenError()
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
        f"1) {TColors.BOLD}show all{TColors.ENDC} (show all accounts)\n"
        f"2) {TColors.BOLD}show{TColors.ENDC} 1 (show individual account by id)\n"
        f'3) {TColors.BOLD}add{TColors.ENDC} "Name" (add new account with name)\n'
        f'4) {TColors.BOLD}change{TColors.ENDC} 1 "New Name" (change account\'s name by id)\n'
        f"5) {TColors.BOLD}freeze{TColors.ENDC} 1 (freeze an account by id)\n"
        f"6) {TColors.BOLD}unfreeze{TColors.ENDC} 1 (unfreeze an account by id)\n"
        f"7) {TColors.BOLD}deposit{TColors.ENDC} 1 12_000 (deposit account's balance by id)\n"
        f"8) {TColors.BOLD}withdraw{TColors.ENDC} 1 5_000 (withdraw account's balance by id)\n"
        f"9) {TColors.BOLD}help{TColors.ENDC} (show this message again)\n"
    )


def main():
    bank_name = input("Input bank name: ").strip()
    print()
    bank = init(bank_name)
    print(welcome_info(bank_name))


if __name__ == "__main__":
    main()
