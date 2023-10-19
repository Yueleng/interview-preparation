class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def output_str(s: str) -> str:
            s_output = ""
            for char in s:
                if char != "#":
                    s_output += char
                else:
                    s_output = s_output[:-1]
            return s_output

        return output_str(s) == output_str(t)
