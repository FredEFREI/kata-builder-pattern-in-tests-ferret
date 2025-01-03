from shop import Shop, User
import UserBuilder


def test_happy_path(fsf_address):
    user = User(
        name="bob",
        email="bob@domain.tld",
        age=25,
        address=fsf_address,
        verified=True,
    )

    assert Shop.can_order(user)
    assert not Shop.must_pay_foreign_fee(user)


def test_minors_cannot_order_from_the_shop(fsf_address):
    user = User(
        name="bob",
        email="bob@domain.tld",
        age=16,
        address=fsf_address,
        verified=True,
    )

    assert not Shop.can_order(user)


def test_cannot_order_if_not_verified_and_minor(fsf_address):
    user = User(
        name="bob",
        email="bob@domain.tld",
        age=16,
        address=fsf_address,
        verified=False,
    )

    assert not Shop.can_order(user)

def test_cannot_order_if_not_verified_and_major(fsf_address):
    user = User(
        name="bob",
        email="bob@domain.tld",
        age=25,
        address=fsf_address,
        verified=False,
    )

    assert not Shop.can_order(user)

def test_foreigners_must_be_foreign_fee(paris_address):
    user = User(
        name="bob",
        email="bob@domain.tld",
        age=25,
        address=paris_address,
        verified=False,
    )

    assert Shop.must_pay_foreign_fee(user)
