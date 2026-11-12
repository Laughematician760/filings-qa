import pytest, math
from quant.returns import simple_returns, log_returns



prices = [100, 110, 99]

def test_simple():
    result = simple_returns(prices)
    assert result == [pytest.approx(.1), pytest.approx(-.1)]

def test_log():
    result = log_returns(prices)
    assert sum(result) == pytest.approx(math.log(99/100))

def test_simple_error():
    with pytest.raises(ValueError):
        simple_returns([-1, 2, 99])

def test_log_error():
    with pytest.raises(ValueError):
        log_returns([-1, 5, 6])

def test_simple_emptyerror():
    with pytest.raises(ValueError):
        simple_returns([])

def test_log_emptyerror():
    with pytest.raises(ValueError):
        log_returns([])

def test_simple_zeroerror():
    with pytest.raises(ValueError):
        simple_returns([0, 1, 1])

def test_log_zeroerror():
    with pytest.raises(ValueError):
        log_returns([0, 1, 1])

def test_simple_lenerror():
    with pytest.raises(ValueError):
        simple_returns([100])

def test_log_lenerror():
    with pytest.raises(ValueError):
        log_returns([200])











