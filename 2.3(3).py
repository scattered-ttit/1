class Calculation:
    def __init__(self):
        self.calculationLine = ""

    def SetCalculationLine(self, line):  # установить строку полностью
        self.calculationLine = line

    def SetLastSymbolCalculationLine(self, symbol):  # добавить символ в конец
        self.calculationLine += symbol

    def GetCalculationLine(self):  # получить всю строку
        return self.calculationLine

    def GetLastSymbol(self):  # получить последний символ
        if self.calculationLine:
            return self.calculationLine[-1]
        return None

    def DeleteLastSymbol(self):  # удалить последний символ
        self.calculationLine = self.calculationLine[:-1]

# Демонстрация:
calc = Calculation()

calc.SetCalculationLine("12+3")
print("Строка:", calc.GetCalculationLine())  # 12+3
calc.SetLastSymbolCalculationLine("*")
print("После добавления символа '*':", calc.GetCalculationLine())  # 12+3*
print("Последний символ:", calc.GetLastSymbol())  # *
calc.DeleteLastSymbol()
print("После удаления последнего символа:", calc.GetCalculationLine())  # 12+3
