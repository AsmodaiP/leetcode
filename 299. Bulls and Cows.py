class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = 0
        b= 0 
        d = {}
        for i, char in enumerate(secret):
            if guess[i] == char:
                a += 1
            else:
                d[char] = d.get(char, 0) + 1

        for i, char in enumerate(secret):
            if guess[i] != char and d.get(guess[i], 0) > 0:
                d[guess[i]] -= 1
                b += 1

        return f'{a}A{b}B'