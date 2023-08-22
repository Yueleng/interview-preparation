class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        dct = {
            1: "A",
            2: "B",
            3: "C",
            4: "D",
            5: "E",
            6: "F",
            7: "G",
            8: "H",
            9: "I",
            10: "J",
            11: "K",
            12: "L",
            13: "M",
            14: "N",
            15: "O",
            16: "P",
            17: "Q",
            18: "R",
            19: "S",
            20: "T",
            21: "U",
            22: "V",
            23: "W",
            24: "X",
            25: "Y",
            26: "Z",
        }

        def _convert(columnNumber):
            val = columnNumber // 26
            remainder = columnNumber % 26
            if val == 0:
                return dct[remainder]
            elif val == 1 and remainder == 0:
                return "Z"
            elif remainder != 0:
                return _convert(val) + dct[remainder]
            else:  # remainder == 0 and value != 1
                return _convert(val - 1) + "Z"

        return _convert(columnNumber)
