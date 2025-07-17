from email.policy import default


class Model:
    def __init__(self):
        self.value = ""
        self.operator = ""
        self.previous_value = ""

    def calculate(self, caption):
        # print(f"calculating {caption}")
        if caption == "C":
            self.value = ""
            self.operator = ""
            self.previous_value = ""

        elif caption == "+/-":
            if self.value.startswith("-"):
                self.value = self.value[1:]
            else:
                self.value = "-" + self.value

        elif caption == ".":
            if not caption in self.value:
                self.value += caption

        elif caption == "=":
            value = str(self._evaluate())
            if value.endswith(".0"):
                self.value = value[:-2]  # Removes the last 2 characters
            else:
                self.value = value

        elif isinstance(caption, int):
            self.value += str(caption)

        else:
            if self.value:
                self.operator = caption
                self.previous_value = self.value
                self.value = ""

        return self.value

    def _evaluate(self):
        try:
            return eval(self.previous_value + self.operator + self.value)
        except ZeroDivisionError:
            return "Math Error!"
        except:
            return "Error!"
