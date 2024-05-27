import sys

def test_virtual_env():
    if (sys.prefix == sys.base_prefix):
        raise Exception("No estas en un ambiente virtual")