import sys
sys.path.append('.')
import shared as sh
import pytest

test = [
    (" This! is      a ,test string  ", 'This is a test string'),
pytest.param(1234, "1234", marks=pytest.mark.xfail)
]

@pytest.mark.parametrize('sample, expected', test)
def test_clean_string(sample, expected): 
    #test_str1 = " This! is      a ,test string  "
    #test_str2 = 1234 #expected to fail
    assert sh.clean_string(sample), "String <{}> not cleaned as expected".format(test_str1) == expected
    assert sh.clean_string(sample), "String <{}> not cleaned as expected".format(test_str2) == expected
