from __future__ import annotations
from abc import ABC, abstractmethod
from shop import User, Address


def fsf_address():
    return Address("51 Franklin Street", "Fifth Floor", "Boston", "02110", "USA")


def paris_address():
    return Address("33 quai d'Orsay", "", "Paris", "75007", "France")


class UserBuilder(ABC):
    @property
    @abstractmethod
    def build_name(self) -> None:
        pass

    @abstractmethod
    def build_email(self) -> None:
        pass

    @abstractmethod
    def build_age(self) -> None:
        pass

    @abstractmethod
    def build_address(self) -> None:
        pass

    @abstractmethod
    def build_verified(self) -> None:
        pass


class ConcreteUserBuilderLocalUnvalidatedMinor(UserBuilder):
    def __init__(self) -> None:
        self.user = User()

    def build_name(self):
        self.user.name = "bob"

    def build_email(self):
        self.user.email = "bob@domain.tld"

    def build_age(self):
        self.user.age = 16

    def build_address(self):
        self.user.address = fsf_address()

    def build_verified(self):
        self.user.verified = False


class ConcreteUserBuilderLocalValidatedMinor(UserBuilder):
    def __init__(self) -> None:
        self.user = User()

    def build_name(self):
        self.user.name = "bob"

    def build_email(self):
        self.user.email = "bob@domain.tld"

    def build_age(self):
        self.user.age = 16

    def build_address(self):
        self.user.address = fsf_address()

    def build_verified(self):
        self.user.verified = True


class ConcreteUserBuilderForeignUnvalidatedMinor(UserBuilder):
    def __init__(self) -> None:
        self.user = User()

    def build_name(self):
        self.user.name = "bob"

    def build_email(self):
        self.user.email = "bob@domain.tld"

    def build_age(self):
        self.user.age = 16

    def build_address(self):
        self.user.address = paris_address()

    def build_verified(self):
        self.user.verified = False


class ConcreteUserBuilderForeignValidatedMinor(UserBuilder):
    def __init__(self) -> None:
        self.user = User()

    def build_name(self):
        self.user.name = "bob"

    def build_email(self):
        self.user.email = "bob@domain.tld"

    def build_age(self):
        self.user.age = 16

    def build_address(self):
        self.user.address = paris_address()

    def build_verified(self):
        self.user.verified = True


class ConcreteUserBuilderLocalUnvalidatedMajor(UserBuilder):
    def __init__(self) -> None:
        self.user = User()

    def build_name(self):
        self.user.name = "bob"

    def build_email(self):
        self.user.email = "bob@domain.tld"

    def build_age(self):
        self.user.age = 19

    def build_address(self):
        self.user.address = fsf_address()

    def build_verified(self):
        self.user.verified = False

# Happy Path
class ConcreteUserBuilderLocalValidatedMajor(UserBuilder):
    def __init__(self) -> None:
        self.user = User()

    def build_name(self):
        self.user.name = "bob"

    def build_email(self):
        self.user.email = "bob@domain.tld"

    def build_age(self):
        self.user.age = 19

    def build_address(self):
        self.user.address = fsf_address()

    def build_verified(self):
        self.user.verified = True


class ConcreteUserBuilderForeignUnvalidatedMajor(UserBuilder):
    def __init__(self) -> None:
        self.user = User()

    def build_name(self):
        self.user.name = "bob"

    def build_email(self):
        self.user.email = "bob@domain.tld"

    def build_age(self):
        self.user.age = 19

    def build_address(self):
        self.user.address = paris_address()

    def build_verified(self):
        self.user.verified = False


class ConcreteUserBuilderForeignValidatedMajor(UserBuilder):
    def __init__(self) -> None:
        self.user = User()

    def build_name(self):
        self.user.name = "bob"

    def build_email(self):
        self.user.email = "bob@domain.tld"

    def build_age(self):
        self.user.age = 19

    def build_address(self):
        self.user.address = paris_address()

    def build_verified(self):
        self.user.verified = True