class Board:
    def __init__(self, dimension, blocks) -> None:
        self._dimension = dimension
        self._blocks = blocks

    def dimension(self):
        return self._dimension

    def min_moves_to_match(self, i: int, j: int):
        element = self._blocks[i][j]
        target_i = (element - 1) // self._dimension
        target_j = (element - 1) % self._dimension

        return abs(i - target_i) + abs(j - target_j)

    def hamming(self):
        # геммінгтонова дистанція(скільки блоків не на своєму місці)
        count = []
        for i in range(self._dimension):
            for j in range(self._dimension):
                # print(self._blocks[i][j])
                # print(i+j+1)
                if self._blocks[i][j] != i+j+3 and self._blocks[i][j] != 0:
                    count.append((i,j, self._blocks[i][j]))
        print("Hamming dist:", len(count)-1)
        return count


    def manhattan(self) -> int:
        # менгеттенівська відстань(найкоротший шлях для вершин не на своїй позиції до вершини,що розглядається як їх
        # позиція)
        blocks = self.hamming()
        print(blocks)
        count = 0
        for i in blocks:
            dist = self.min_moves_to_match(i[0], i[1])
            count += dist
        # -1, бо не враховуємо перевірку позиції пустої ячейки
        print("Mahhattan dist:", count - 1)
        return count

    def find_empty_block(self):
        for i in range(self._dimension):
            for j in range(self._dimension):
                if self._blocks[i][j] == 0:
                    return i,j

    def __hash__(self):
        return hash(tuple(map(tuple, self._blocks)))

    def inversions(self):
        # рахуєм кількість перестановок на дошці
        inv_count = 0
        flattened = [num for row in self._blocks for num in row if num != 0]
        for i in range(len(flattened)):
            for j in range(i + 1, len(flattened)):
                if flattened[j] < flattened[i]:
                    inv_count += 1
        return inv_count

    # змінюємо місцями і повертаєм оновлену дошку
    def move_block(self, i1: int, j1: int, i2: int, j2: int) -> 'Board':
        new_blocks = [row[:] for row in self._blocks]
        new_blocks[i1][j1], new_blocks[i2][j2] = new_blocks[i2][j2], new_blocks[i1][j1]
        return Board(self._dimension, new_blocks)

    def solution_check(self):
        # Перевірка: чи ця дошка є метою/рішенням
        goal = 1
        for i in range(self._dimension):
            for j in range(self._dimension):
                if i == self._dimension - 1 and j == self._dimension - 1:
                    if self._blocks[i][j] != 0:
                        return False
                elif self._blocks[i][j] != goal:
                    return False
                goal += 1
        return True

    def __eq__(self, other) -> bool:
        for i in range(self._dimension):
            for j in range(self._dimension):
                if self._blocks[i][j] != other._blocks[i][j]:
                    return False
        return True

    def neighbors(self):
        neighbors = []
        empty_row, empty_col = self.find_empty_block()
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # праворуч, ліворуч, вниз, вгору відносно пустої
        for move in moves:
            new_row = empty_row + move[0]
            new_col = empty_col + move[1]
            if 0 <= new_row < self._dimension and 0 <= new_col < self._dimension:
                new_blocks = [row[:] for row in self._blocks]  # копія блоків
                new_blocks[empty_row][empty_col] = new_blocks[new_row][new_col]#вказуємо, де лежить пуста комірка
                new_blocks[new_row][new_col] = 0
                neighbor = Board(self._dimension, new_blocks) #варіянти нових дошок
                neighbors.append(neighbor)
        return neighbors

    def __str__(self) -> str:
        matrix_str = ""

        for row in self._blocks:
            row_str = "  ".join(str(element) for element in row)
            matrix_str += row_str + "\n"

        return matrix_str

