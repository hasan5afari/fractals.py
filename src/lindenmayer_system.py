class LindenmayerSystem:
    def __init__(self, axiom: str, production_rules: dict[str, str]) -> None:
        self.axiom = axiom
        self.sentence = axiom
        self.production_rules = production_rules

    def __str__(self) -> str:
        return self.sentence

    def iterate(self) -> str:
        new_sentence = ""

        for character in self.sentence:
            new_sentence += self.production_rules.get(character, character)

        self.sentence = new_sentence

        return self.sentence
