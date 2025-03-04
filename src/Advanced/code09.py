from typing import Never
from typing import assert_never

def stop() -> Never:
    """TODO: implement this function to make it type check"""
    raise RuntimeError('no way')

assert_never(stop())