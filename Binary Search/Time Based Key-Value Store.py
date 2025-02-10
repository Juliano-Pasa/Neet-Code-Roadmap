from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.kv = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kv:
            return ""
        
        values = self.kv[key]

        l = 0
        r = len(values)

        while l != r:
            mid = (l + r) // 2

            if timestamp == values[mid][0]:
                l = mid + 1
                r = mid + 1
            elif timestamp < values[mid][0]:
                r = mid
            else:
                l = mid + 1
                
        if l < 1:
            return ""
        return values[l-1][1]