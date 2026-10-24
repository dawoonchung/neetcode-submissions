class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not len(stones):
            return 0
        if len(stones) == 1:
            return stones[0]
        minHeap = []
        for stone in stones:
            minHeap.append(stone)

        heapq.heapify(minHeap)

        remaining = []

        while len(minHeap) > 2:
            remaining.append(heapq.heappop(minHeap))
        
        stone_1, stone_2 = minHeap

        if stone_1 != stone_2:
            remaining.append(abs(stone_1 - stone_2))

        return self.lastStoneWeight(remaining)