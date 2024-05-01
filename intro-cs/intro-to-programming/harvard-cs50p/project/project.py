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


def main():
    bank_name = input("Input bank name: ").strip()
    print()
    bank = init(bank_name)
    welcome_info = (
        f'Welcome to "{bank_name}" bank!\n\n'
        "You can manage your bank with commands:\n\n"
        "1) show all (show all accounts)\n"
        "2) show 1 (show individual account by id)\n"
        '3) add "Name" (add new account with name)\n'
        '4) change 1 "New Name" (change account\'s name by id)\n'
        "5) freeze 1 (freeze an account by id)\n"
        "6) unfreeze 1 (unfreeze an account by id)\n"
        "7) deposit 1 12_000 (deposit account's balance by id)\n"
        "8) withdraw 1 5_000 (withdraw account's balance by id)\n"
    )
    print(welcome_info)
    print(bank)


if __name__ == "__main__":
    main()
