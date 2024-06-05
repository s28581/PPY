class BelowZero(Exception):
    def __init__(self, message="Wartość nie może być mniejsza od zera."):
        self.message = message
        super().__init__(self.message)
