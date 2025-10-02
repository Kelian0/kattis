from src.kattis.goggi import gluttonous_george

def test_goggi1():
    assert gluttonous_george('21 ? 13') == '>'

def test_goggi1():
    assert gluttonous_george('1 ? 100') == '<'

def test_goggi1():
    assert gluttonous_george('26 ? 26') == 'Goggi svangur!'
