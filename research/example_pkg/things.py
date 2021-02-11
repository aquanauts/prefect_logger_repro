import logging
import sys

logging.basicConfig(stream=sys.stdout)
_LOGGER = logging.getLogger(__name__)

def thing1():
    _LOGGER.info(f"running thing1")
    for i in range(10):
        _LOGGER.info(f"loop#: {i}")
    return True

def thing2():
    _LOGGER.info(f"running thing2")
    for i in ["a", "b", "c", "d", "e", "f"]:
        _LOGGER.info(f"loop#: {i}")
    return True

def main():
    thing1()
    thing2()


if __name__ == "__main__":
    main()
