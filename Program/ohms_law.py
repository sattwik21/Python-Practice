from __future__ import annotations


def ohms_law(voltage: float, current: float, resistance: float) -> dict[str, float]:
    
    if (voltage, current, resistance).count(0) != 1:
        raise ValueError("One and only one argument must be 0")
    if resistance < 0:
        raise ValueError("Resistance cannot be negative")
    if voltage == 0:
        return {"voltage": float(current * resistance)}
    elif current == 0:
        return {"current": voltage / resistance}
    elif resistance == 0:
        return {"resistance": voltage / current}
    else:
        raise ValueError("Exactly one argument must be 0")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
