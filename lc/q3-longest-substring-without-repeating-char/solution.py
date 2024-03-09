from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        _map = defaultdict(int)
        i = 0
        _max = 0
        left_p = 0

        while i < len(s):
            char = s[i]

            if char in _map:
                # update left_p index
                left_p = max(left_p, _map[char] + 1)

            _map[char] = i
            _max = max(_max, i - left_p + 1)
            i += 1

        return _max


if __name__ == "__main__":
    s = Solution()

    # Example 1
    assert s.lengthOfLongestSubstring("abcabcbb") == 3

    # Example 2
    assert s.lengthOfLongestSubstring("bbbbb") == 1

    # Example 3
    assert s.lengthOfLongestSubstring("pwwkew") == 3

    # Example 4
    assert s.lengthOfLongestSubstring("") == 0

    # Example 5
    assert s.lengthOfLongestSubstring("abba") == 2

    print("All passed")
