from tabulate import tabulate


HEADERS = ["ID", "Name", "Balance", "Status"]


def render_account(account):
    table = decorate_account(account.values())
    print(tabulate([table], headers=HEADERS))


def render_accounts(accounts):
    table = list(map(lambda account: decorate_account(account.values()), accounts))
    print(tabulate(table, headers=HEADERS))


def decorate_account(account):
    id, name, balance, status = account
    decorated_balance = f"{balance:_}"
    return [id, name, decorated_balance, status]
