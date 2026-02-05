import json


class LindenmayerSystem:
    @classmethod
    def from_json(cls, path: str) -> tuple["LindenmayerSystem", float]:
        with open(path, mode="r", encoding="utf-8") as file:
            data = json.load(file)

        return (cls(data["axiom"], data["production_rules"]), data["dtheta"])

    def __init__(self, axiom: str, production_rules: dict[str, str]) -> None:
        self._axiom = axiom
        self._production_rules = production_rules
        self._sentence = axiom

    def __str__(self) -> str:
        return self._sentence

    def iterate(self) -> str:
        new_sentence = ""

        for character in self._sentence:
            new_sentence += self._production_rules.get(character, character)

        self._sentence = new_sentence

        return self._sentence

    def get_sentence(self) -> str:
        return self._sentence
