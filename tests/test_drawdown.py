
import pytest
from quant.drawdown import drawdown


def test_drawdown_len_error():
    with pytest.raises(ValueError):
        drawdown([])

def test_drawdown_firstent_error():
    with pytest.raises(ValueError):
        drawdown([0, 100, 20])

def test_drawdown_neg_error():
    with pytest.raises(ValueError):
        drawdown([-1, 3, 100])

def test_drawdown_increasing():
    result = drawdown([100, 200, 300])
    assert result == pytest.approx(0)

def test_drawdown_doubles():
    result = drawdown([10, 20, 5])
    assert result == pytest.approx(drawdown([20, 40, 10]))

def test_drawdown_case_one():
    result = drawdown([100, 120, 90, 130])
    assert result == pytest.approx(-.25)

def test_drawdown_case_two():
    result = drawdown([100])
    assert result == pytest.approx(0)

def test_drawdown_case_three():
    result = drawdown([100, 90, 80, 90, 60, 50, 40])
    assert result == pytest.approx(-.6)

def test_drawdown_case_four():
    result = drawdown([100, 90, 80])
    assert result == pytest.approx(-.2)

def test_drawdown_range():
    result = drawdown([100, 0, 1])
    assert result == pytest.approx(-1)