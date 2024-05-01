from project import (
    init,
    get_account,
    add_account,
    freeze_account,
    change_account_name,
    deposit,
    withdraw,
)
import pytest


def test_init():
    assert init("Multiverse Bank") == {
        bank: {
            name: "Multiverse Bank",
            accounts: [
                {id: 1, name: "Boss", balance: 80_000_000_000, status: "active"}
            ],
        }
    }


def test_get_account():
    bank = init("Multiverse Bank")
    assert get_account(1, bank=bank) == {
        id: 1,
        name: "Boss",
        balance: 80_000_000_000,
        status: "active",
    }


def test_add_account():
    bank = init("Multiverse Bank")
    account_info = {name: "Artem"}
    assert add_account(account_info, bank=bank) == {
        {id: 2, name: "Artem", balance: 0, status: "active"}
    }


def test_freeze_account():
    bank = init("Multiverse Bank")
    account_info = {name: "Scammer"}
    account = add_account(account_info, bank=bank)
    assert account["status"] == "active"

    freeze_account(account["id"], bank=bank)
    account = get_account(account["id"], bank=bank)
    assert account["status"] == "frozen"


def test_change_account_name():
    bank = init("Multiverse Bank")
    account_info = {name: "Alex"}
    account = add_account(account_info, bank=bank)
    assert account["name"] == "Alex"

    change_account_name(account["id"], new_name="Alexander", bank=bank)
    account = get_account(account["id"], bank=bank)
    assert account["name"] == "Alexander"


def test_deposit():
    bank = init("Multiverse Bank")
    account_info = {name: "Alex"}
    account = add_account(account_info, bank=bank)
    assert account["balance"] == 0

    deposit(account["id"], amount=1500, bank=bank)
    account = get_account(account["id"], bank=bank)
    assert account["balance"] == 1500

    deposit(account["id"], amount=120, bank=bank)
    account = get_account(account["id"], bank=bank)
    assert account["balance"] == 1620


def test_withdraw():
    bank = init("Multiverse Bank")
    account_info = {name: "Alex"}
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
