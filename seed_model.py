_SEED_VALUE = 0  # default 0


def get_seed_value() -> int:
    return _SEED_VALUE


def set_seed_value(new_value: int) -> None:
    global _SEED_VALUE
    _SEED_VALUE = new_value
