class Solution:
    numbers = {
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        30,
        40,
        50,
        60,
        70,
        80,
        90,
    }
    strings = {
        'Hundred',
        'Thousand',
        'Million',
        'Billion',
    }
    string2number = [
        ('Billion', 1000000000),
        ('Million', 1000000),
        ('Thousand', 1000),
        ('Hundred', 100),
        ('Ninety', 90),
        ('Eighty', 80),
        ('Seventy', 70),
        ('Sixty', 60),
        ('Fifty', 50),
        ('Forty', 40),
        ('Thirty', 30),
        ('Twenty', 20),
        ('Nineteen', 19),
        ('Eighteen', 18),
        ('Seventeen', 17),
        ('Sixteen', 16),
        ('Fifteen', 15),
        ('Fourteen', 14),
        ('Thirteen', 13),
        ('Twelve', 12),
        ('Eleven', 11),
        ('Ten', 10),
        ('Nine', 9),
        ('Eight', 8),
        ('Seven', 7),
        ('Six', 6),
        ('Five', 5),
        ('Four', 4),
        ('Three', 3),
        ('Two', 2),
        ('One', 1),
        ('Zero', 0)
    ]
    number2string = {
        1000000000: 'Billion',
        1000000: 'Million',
        1000: 'Thousand',
        100: 'Hundred',
        90: 'Ninety',
        80: 'Eighty',
        70: 'Seventy',
        60: 'Sixty',
        50: 'Fifty',
        40: 'Forty',
        30: 'Thirty',
        20: 'Twenty',
        19: 'Nineteen',
        18: 'Eighteen',
        17: 'Seventeen',
        16: 'Sixteen',
        15: 'Fifteen',
        14: 'Fourteen',
        13: 'Thirteen',
        12: 'Twelve',
        11: 'Eleven',
        10: 'Ten',
        9: 'Nine',
        8: 'Eight',
        7: 'Seven',
        6: 'Six',
        5: 'Five',
        4: 'Four',
        3: 'Three',
        2: 'Two',
        1: 'One',
        0: 'Zero'
    }

    def parse(self, num, res):
        for k, v in self.string2number[:len(self.string2number) - 1]:
            r, num = divmod(num, v)
            if r:
                if k in self.strings:
                    if r in self.numbers:
                        res.append(self.number2string[r])
                        res.append(k)
                    else:
                        self.parse(r, res)
                        res.append(k)
                else:
                    res.append(k)

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        res = []
        self.parse(num, res)
        return ' '.join(res)


s = Solution()
print(s.numberToWords(1234567))
