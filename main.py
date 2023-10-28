from collections import deque


class Node:
    def __init__(self, chars: str, neighbors=None):
        self.chars = chars
        self.neighbors = neighbors if neighbors is not None else []
        self.visited = False

    def __str__(self):
        return f'Chars="{self.chars}"'


class Solution:
    def minMutation(self, start_gene: str, end_gene: str, bank: list[str]) -> int:
        storage = [start_gene]
        visited = {start_gene}
        steps = 0

        while storage:
            temp_storage = []

            for curr in storage:
                if curr == end_gene:
                    return steps
                neighbors = [gene for gene in bank if sum(a != b for a, b in zip(curr, gene)) == 1]
                for neighbor in neighbors:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        temp_storage.append(neighbor)

            steps += 1
            storage = temp_storage
        return -1


if __name__ == '__main__':
    task = Solution()

    startGene = "AACCGGTT"
    endGene = "AAACGGTA"
    Bank = []

    print(task.minMutation(startGene, endGene, Bank))
