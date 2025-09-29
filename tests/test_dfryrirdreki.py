from src.kattis.dfryrirdreki import d_fyrir_dreki

def test_d_fyrir_dreki1():
    a = -5
    b = 1
    c = 1
    assert d_fyrir_dreki(a,b,c) == 2
    
def test_d_fyrir_dreki2():
    a = 1
    b = 1
    c = 1
    assert d_fyrir_dreki(a,b,c) == 0

    
def test_d_fyrir_dreki3():
    a = 2
    b = 4
    c = 2
    assert d_fyrir_dreki(a,b,c) == 1