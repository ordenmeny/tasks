class Chess:
    def __init__(self):
        # координата первой клетки
        self.x1 = int(input())
        self.y1 = int(input())

        # координата второй клетки
        self.x2 = int(input())
        self.y2 = int(input())

    def ladya(self):
        # ладья
        if self.x1 == self.x2 or self.y1 == self.y2:
            return 'YES'
        else:
            return 'NO'

    def king(self):
        # король
        if self.x1 == self.x2 and self.y2 in (self.y1 + 1, self.y1 - 1):
            return 'YES'
        if self.y1 == self.y2 and self.x2 in (self.x1 - 1, self.x1 + 1):
            return 'YES'
        if self.x2 in (self.x1 + 1, self.x1 - 1) and self.y2 in (self.y1 + 1, self.y1 - 1):
            return 'YES'
        return 'NO'

    def slon(self):
        # слон
        if max(self.x1, self.x2) - min(self.x1, self.x2) == max(self.y1, self.y2) - min(self.y1, self.y2):
            return 'YES'
        return 'NO'

    def fers(self):
        # ферзь
        if self.ladya() == 'YES' or self.slon() == 'YES':
            return 'YES'
        return 'NO'

    def horse(self):
        # конь
        if abs(self.x1 - self.x2) in (1, 2) and abs(self.y1 - self.y2) == (1 if abs(self.x1 - self.x2) == 2 else 2):
            return 'YES'
        return 'NO'


ch = Chess()
print(ch.horse())
