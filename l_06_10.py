
class SuperStr(str):

    def __init__(self, s):
        self.s = s

    def is_repeatance(self, s):
        if not isinstance(s, str):
            return False
        n = len(self) // (len(s) or 1)
        return self == n * s

    def is_palindrome(self):
        s = self.lower()
        return s == s[::-1]


a = SuperStr('123454321')
print(a.is_repeatance('123'))
print(a.is_palindrome())
