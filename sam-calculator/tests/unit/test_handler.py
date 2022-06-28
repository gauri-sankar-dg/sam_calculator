import json

import pytest

from hello_world import app

def test_add():
    assert app.add(5,3) == 8

def test_sub():
    assert app.sub(5,3) == 2

def test_multiple():
    assert app.multiply(5,3) == 15