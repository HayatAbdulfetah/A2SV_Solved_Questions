class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)

        for start, end, direction in shifts:

            if direction == 1:
                diff[start] += 1
                diff[end + 1] -= 1
            else:
                diff[start] -= 1
                diff[end + 1] += 1

        result = []
        running = 0

        for i in range(n):
            running += diff[i]

            old = ord(s[i]) - ord('a')

            new = (old + running) % 26

            result.append(chr(new + ord('a')))

        return "".join(result)
