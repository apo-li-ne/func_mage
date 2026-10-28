def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: "* " + s + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    strongest = max(mages, key=lambda m: m["power"])
    weakest = min(mages, key=lambda m: m["power"])
    total = sum(map(lambda m: m["power"], mages))
    return {
        "max_power": strongest["power"],
        "min_power": weakest["power"],
        "avg_power": round(total / len(mages), 2),
    }


if __name__ == "__main__":
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "orb"},
        {"name": "Fire Staff", "power": 92, "type": "staff"},
    ]
    mages = [
        {"name": "Ana", "power": 70, "element": "fire"},
        {"name": "Bob", "power": 95, "element": "ice"},
        {"name": "Cleo", "power": 50, "element": "wind"},
    ]

    print("Testing artifact sorter...")
    s = artifact_sorter(artifacts)
    print(f"{s[0]['name']} ({s[0]['power']} power) comes before "
          f"{s[1]['name']} ({s[1]['power']} power)")

    print("\nTesting power filter...")
    print(power_filter(mages, 60))

    print("\nTesting spell transfornmer...")
    print(" ".join(spell_transformer(["fireball", "heal", "shield"])))

    print("\nTesting mage stats...")
    print(mage_stats(mages))

