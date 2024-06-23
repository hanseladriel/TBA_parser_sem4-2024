class PushdownParser:
    def __init__(self):
        self.stack = []
        self.valid_structures = [
            ["S", "P", "O", "K"],
            ["S", "P", "K"],
            ["S", "P", "O"],
            ["S", "P"]
        ]
    
    def parse(self, tokens):
        for structure in self.valid_structures:
            if tokens == structure:
                return True
        return False
