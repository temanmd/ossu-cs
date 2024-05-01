class AccountIsFrozenError(Exception):
    pass


class AccountNotFoundError(Exception):
    pass


def get_ids(bank):
    return sorted(map(lambda account: account["id"], bank["accounts"]))


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
    if account["status"] == "frozen":
        pass
    else:
        index = bank["accounts"].index(account)
        account["status"] = "frozen"
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
    if account["status"] == "active":
        index = bank["accounts"].index(account)
        account["balance"] += amount
        bank["accounts"][index] = account
        return account
    else:
        raise AccountIsFrozenError()


def withdraw():
    pass


def init(bank_name):
    bank = {
        "name": bank_name.strip(),
        "accounts": [],
    }
    account = add_account({"name": "Boss"}, bank=bank)
    deposit(account["id"], amount=80_000_000_000, bank=bank)
    return bank


def main():
    pass


if __name__ == "__main__":
    main()
