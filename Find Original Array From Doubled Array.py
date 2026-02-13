class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        original = []
        changed.sort()
        count = Counter(changed)

        if len(changed)%2 != 0:
            return []

        for num in changed:
            if count[num] == 0:
                continue
            if count[num*2] == 0:
                return []

            count[num] -= 1
            count[num*2] -= 1
            original.append(num)

        return original
