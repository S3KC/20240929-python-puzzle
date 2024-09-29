from main import main, challenge
import pytest


def test_main_output():
    result = main()
    assert result == 1312850, "Did not get the expected result, check your work and try again."


def test_challenge():
    try:
        result = challenge()
        assert result == 36749103, "Did not get the expected result, check your work and try again."
    except NotImplementedError:
        pytest.skip("challenge function not implemented")
