import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    ops: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }
    if operation not in ops:
        raise ValueError(f"Unknown operation: {operation}")
    if not spells:
        return 0
    return functools.reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire_enchant": functools.partial(
            base_enchantment, 50, "fire"),
        "ice_enchant": functools.partial(
            base_enchantment, 50, "ice"),
        "lightning_enchant": functools.partial(
            base_enchantment, 50, "lightning"),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @functools.singledispatch
    def cast(spell: Any) -> str:
        return "Unknown spell type"

    @cast.register(int)
    def _(spell: int) -> str:
        return f"{spell} damage"

    @cast.register(str)
    def _(spell: str) -> str:
        return spell

    @cast.register(list)
    def _(spell: list) -> str:
        return f"{len(spell)} spells"

    return cast


def base_enchant(power: int, element: str, target: str) -> str:
    return f"{element} enchantment of power {power} on {target}"


if __name__ == "__main__":
    powers = [10, 20, 30, 40]
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(powers, 'add')}")
    print(f"Product: {spell_reducer(powers, 'multiply')}")
    print(f"Max: {spell_reducer(powers, 'max')}")
    print(f"Min: {spell_reducer(powers, 'min')}")
    try:
        spell_reducer(powers, "divide")
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting partial enchanter...")
    for name, fn in partial_enchanter(base_enchant).items():
        print(f"{name}: {fn('Sword')}")

    print("\nTesting memoized fibonacci...")
    for n in (0, 1, 10, 15):
        print(f"Fib({n}): {memoized_fibonacci(n)}")
    print(memoized_fibonacci.cache_info())

    print("\nTesting spell dispatcher...")
    cast = spell_dispatcher()
    print(f"Damage spell: {cast(42)}")
    print(f"Enchantment: {cast('fireball')}")
    print(f"Multi-cast: {cast(['a', 'b', 'c'])}")
    print(cast(3.14))
