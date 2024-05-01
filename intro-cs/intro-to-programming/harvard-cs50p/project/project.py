def add_account(info, bank):
    ids = sorted(map(lambda account: account["id"], bank["accounts"]))
    new_id = ids[-1] + 1
    new_account = {"id": new_id, "name": info["name"], "balance": 0, "status": "active"}
    bank["accounts"].append(new_account)
    return new_account


def get_account():
    pass


def freeze_account():
    pass


def change_account_name():
    pass


def deposit():
    pass


def withdraw():
    pass


def init(bank_name):
    bank = {
        name: bank_name.strip(),
        accounts: [],
    }
    account = add_account({name: "Boss"})
    deposit(account("id"), amount=80_000_000_000)
    return bank


def main():
    pass


if __name__ == "__main__":
    main()
