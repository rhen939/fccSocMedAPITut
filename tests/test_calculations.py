from app.calculations import add, subtract, multiply, divide, BankAccount, InsufficientFunds
import pytest


@pytest.fixture
def zero_bank_account():
    return BankAccount()


@pytest.fixture
def fifty_bank_account():
    return BankAccount(50)


@pytest.mark.parametrize("num1, num2, expected", [
    (3,2,5),
    (7,1,8),
    (12,4,16)
])
def test_add(num1, num2, expected):
    print ("test")
    assert add(num1, num2) == expected


def test_subtract():
    print("subtract test")
    assert subtract(9, 4) == 5


def test_multiply():
    print("multiply test")
    assert multiply(3, 2) == 6


def test_divide():
    print("divide test")
    assert divide(9, 3) == 3


def test_bank_account_set_initial_amount(fifty_bank_account):
    assert fifty_bank_account.balance == 50


def test_bank_account_default_amount(zero_bank_account):
    assert zero_bank_account.balance == 0


def test_withdraw(fifty_bank_account):
    fifty_bank_account.withdraw(20)
    assert fifty_bank_account.balance == 30


def test_deposit(fifty_bank_account):
    fifty_bank_account.deposit(20)
    assert fifty_bank_account.balance == 70


def test_interest(fifty_bank_account):
    fifty_bank_account.collect_interest()
    assert round(fifty_bank_account.balance, 6) == 55


@pytest.mark.parametrize("deposited, withdrew, expected", [
    (3,2,1),
    (7,1,6),
    (12,4,8),
])
def test_bank_transaction(zero_bank_account, deposited, withdrew, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected


def test_nsf(fifty_bank_account):
    with pytest.raises(InsufficientFunds):
        fifty_bank_account.withdraw(100)


