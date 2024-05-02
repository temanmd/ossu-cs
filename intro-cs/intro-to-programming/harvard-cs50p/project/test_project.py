from data_functions import (
    AccountIsFrozenError,
    AccountNotFoundError,
    OutOfMoneyError,
    init,
    get_account,
    get_accounts,
    add_account,
    freeze_account,
    unfreeze_account,
    change_account_name,
    deposit,
    withdraw,
    get_ids,
)
import pytest


def test_init():
    assert init("Multiverse Bank") == {
        "name": "Multiverse Bank",
        "accounts": [
            {"id": 1, "name": "Boss", "balance": 80_000_000_000, "status": "active"}
        ],
    }


def test_get_accounts():
    bank = init("Multiverse Bank")
    assert get_accounts(bank) == [
        {"id": 1, "name": "Boss", "balance": 80_000_000_000, "status": "active"}
    ]

    alex = add_account({"name": "Alex"}, bank=bank)
    nick = add_account({"name": "Nick"}, bank=bank)
    deposit(alex["id"], amount=1200, bank=bank)
    deposit(nick["id"], amount=50_000, bank=bank)
    withdraw(nick["id"], amount=12_500, bank=bank)
    freeze_account(alex["id"], bank=bank)
    assert get_accounts(bank) == [
        {"id": 1, "name": "Boss", "balance": 80_000_000_000, "status": "active"},
        {"id": 2, "name": "Alex", "balance": 1200, "status": "frozen"},
        {"id": 3, "name": "Nick", "balance": 37_500, "status": "active"},
    ]


def test_get_ids():
    bank = init("Multiverse Bank")
    assert get_ids(bank) == [1]
    add_account({"name": "Alex"}, bank=bank)
    assert get_ids(bank) == [1, 2]


def test_get_account():
    bank = init("Multiverse Bank")
    assert get_account(1, bank=bank) == {
        "id": 1,
        "name": "Boss",
        "balance": 80_000_000_000,
        "status": "active",
    }
    with pytest.raises(AccountNotFoundError):
        get_account(123, bank=bank)


def test_add_account():
    bank = init("Multiverse Bank")
    account_info = {"name": "Artem"}
    assert add_account(account_info, bank=bank) == {
        "id": 2,
        "name": "Artem",
        "balance": 0,
        "status": "active",
    }


def test_freeze_account():
    bank = init("Multiverse Bank")
    account_info = {"name": "Scammer"}
    account = add_account(account_info, bank=bank)
    assert account["status"] == "active"

    freeze_account(account["id"], bank=bank)
    account = get_account(account["id"], bank=bank)
    assert account["status"] == "frozen"


def test_unfreeze_account():
    bank = init("Multiverse Bank")
    account_info = {"name": "Suspicious Nick"}
    account = add_account(account_info, bank=bank)
    freeze_account(account["id"], bank=bank)
    unfreeze_account(account["id"], bank=bank)
    account = add_account(account_info, bank=bank)
    assert account["status"] == "active"


def test_change_account_name():
    bank = init("Multiverse Bank")
    account_info = {"name": "Alex"}
    account = add_account(account_info, bank=bank)
    assert account["name"] == "Alex"

    change_account_name(account["id"], new_name="Alexander", bank=bank)
    account = get_account(account["id"], bank=bank)
    assert account["name"] == "Alexander"


def test_deposit():
    bank = init("Multiverse Bank")
    account_info = {"name": "Alex"}
    account = add_account(account_info, bank=bank)
    assert account["balance"] == 0

    deposit(account["id"], amount=1500, bank=bank)
    account = get_account(account["id"], bank=bank)
    assert account["balance"] == 1500

    deposit(account["id"], amount=120, bank=bank)
    account = get_account(account["id"], bank=bank)
    assert account["balance"] == 1620

    freeze_account(account["id"], bank=bank)

    with pytest.raises(AccountIsFrozenError):
        deposit(account["id"], amount=100, bank=bank)


def test_withdraw():
    bank = init("Multiverse Bank")
    account_info = {"name": "Alex"}
    account = add_account(account_info, bank=bank)
    deposit(account["id"], amount=5000, bank=bank)

    withdraw(account["id"], amount=1500, bank=bank)
    account = get_account(account["id"], bank=bank)
    assert account["balance"] == 3500

    with pytest.raises(OutOfMoneyError):
        withdraw(account["id"], amount=5000, bank=bank)

    freeze_account(account["id"], bank=bank)

    with pytest.raises(AccountIsFrozenError):
        withdraw(account["id"], amount=100, bank=bank)
