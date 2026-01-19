class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        chars = list(s)
        for i in range(len(s) - 1, -1, -1):
            if not chars[i].isalnum():
                chars.pop(i)
            elif chars[i].isupper():
                chars[i] = chars[i].lower()
            else:
                pass
        s = "".join(chars)
        return s == s[::-1]

        