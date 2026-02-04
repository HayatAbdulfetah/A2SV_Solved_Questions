class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans = []
        Kelevin = celsius + 273.15
        ans.append(Kelevin)
        Fahrenheit = celsius * 1.80 + 32.00
        ans.append(Fahrenheit)
        return ans
