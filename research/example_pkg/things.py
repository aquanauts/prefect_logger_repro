import logging


_LOGGER = logging.getLogger(__name__)

def thing1():
    for i in range(10):
        _LOGGER.warning(f"running thing1")
        _LOGGER.warning(f"loop#: {i}")
    return True

def thing2():
    for i in ["a", "b", "c", "d", "e", "f"]:
        _LOGGER.warning(f"running thing2")
        _LOGGER.warning(f"loop#: {i}")
    return True

def main():
    thing1()
    thing2()


if __name__ == "__main__":
    main()
