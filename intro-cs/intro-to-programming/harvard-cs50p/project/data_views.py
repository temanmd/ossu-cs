from tabulate import tabulate


HEADERS = ["ID", "Name", "Balance", "Status"]


def render_account(account):
    table = decorate_account(account.values())
    render_table([table])


def render_accounts(accounts):
    table = list(map(lambda account: decorate_account(account.values()), accounts))
    render_table(table)


def render_table(accounts):
    print(tabulate(accounts, headers=HEADERS, tablefmt="github"))


def decorate_account(account):
    id, name, balance, status = account
    decorated_balance = f"{balance:_}"
    return [id, name, decorated_balance, status]
