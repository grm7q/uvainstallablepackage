import sys
sys.path.append('.')
import shared as sh
import pytest

test_clean = [
    (" This! is      a ,test string  ", 'This is a test string'),
pytest.param(1234, "1234", marks=pytest.mark.xfail)  #expected to fail
]

@pytest.mark.parametrize('sample, expected', test_clean)
def test_clean_string(sample, expected): 
    assert sh.clean_string(sample) == expected
    assert sh.clean_string(sample) == expected

    
test_compress = [
    (" This! is      a ,test string  ", "This! is a ,test string"),
pytest.param(1234, "1234", marks=pytest.mark.xfail)  #expected to fail
]

@pytest.mark.parametrize('sample, expected', test_compress)
def test_space_compress(sample, expected): 
    assert sh.space_compress(sample) == expected
    assert sh.space_compress(sample) == expected
