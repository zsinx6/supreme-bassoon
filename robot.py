STANDARD = "STANDARD"
SPECIAL = "SPECIAL"
REJECTED = "REJECTED"


def _is_bulky(width: float, height: float, length: float) -> bool:
    if width * height * length >= 1_000_000 or any(
        dim >= 150 for dim in (width, height, length)
    ):
        return True
    return False


def _is_heavy(mass: float) -> bool:
    if mass >= 20:
        return True
    return False


def sort(width: float, height: float, length: float, mass: float) -> str:
    is_bulky = _is_bulky(width, height, length)
    is_heavy = _is_heavy(mass)
    if is_bulky and is_heavy:
        return REJECTED
    if is_bulky or is_heavy:
        return SPECIAL
    return STANDARD
