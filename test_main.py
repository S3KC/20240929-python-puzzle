from main import main, challenge
import pytest


def test_main_output():
    result = main()
    assert result == 1312850, "Did not get the expected result, check your work and try again."


@pytest.mark.skipif(challenge.__code__.co_code == b'd\x00S\x00', reason="challenge function not implemented")
def test_challenge():
    result = challenge()
    assert result == 36749103, "Did not get the expected result, check your work and try again."
