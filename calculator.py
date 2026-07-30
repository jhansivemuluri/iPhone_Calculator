class Calculator:
    def __init__(self):
        self.current = ""
        self.history = []

    def add_input(self, value):
        self.current += str(value)
        return self.current

    def clear(self):
        self.current = ""
        return self.current

    def backspace(self):
        self.current = self.current[:-1]
        return self.current

    def calculate(self):
        try:
            result = str(eval(self.current))

            self.history.append(
                f"{self.current} = {result}"
            )

            self.current = result
            return result

        except:
            self.current = "Error"
            return self.current

    def percentage(self):
        try:
            self.current = str(float(self.current) / 100)
            return self.current

        except:
            return "Error"

    def plus_minus(self):
        try:
            if self.current.startswith("-"):
                self.current = self.current[1:]
            else:
                self.current = "-" + self.current

            return self.current

        except:
            return "Error"

    def get_history(self):
        return self.history