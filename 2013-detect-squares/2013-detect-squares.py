class DetectSquares:
    def __init__(self):
        self.frequency = Counter()

    def add(self, point: List[int]) -> None:
        self.frequency[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        ans = 0
        p1x, p1y = point
        for (p2x, p2y), count in self.frequency.items():
            if abs(p1x-p2x) == 0 or abs(p1x - p2x) != abs(p1y - p2y):
                continue  
            ans += count * self.frequency[(p1x, p2y)] * self.frequency[(p2x, p1y)]
        return ans