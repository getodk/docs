from hypothesis import given, example

from hypothesis import strategies as st

HELLO_MSG = 'Hello Hypothesis'


@given(st.just(HELLO_MSG))
def test_framework(s):
    assert s == HELLO_MSG
