from src.si_person.person import Person
from src.si_person import data
import pytest

p = Person()

def test_always_passes():
    print(p.name())


def test_always_fails():
    pass