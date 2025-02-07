from board import Board

class Solver:
    def __init__(self, board):
        self._initial_board = board

    def is_solvable(self) -> bool:
        # передаємо к-сть перестановок в даній дошці, користуючись методом з Board
        inversion_count = self._initial_board.inversions()

        dimension_even = self._initial_board._dimension % 2 == 0
        inversion_even = (inversion_count-1) % 2 == 0
        # перевіряємо, чи сумісно це з розмірами дошки і
        # умовою розв'язності(з файлику)
        return dimension_even == inversion_even


    # перевіряємо, чи є сенс нам рухати блоки(, скільки разів допоки система не буде вирішеною)

    def moves(self):
    # тут знаходим список послідовності дошок для найшвидшого розв'язку (або -1, якщо рішення нема)
        if not self.is_solvable():
            return None

        queue = Min_proir_queue()
        queue.add(self._initial_board, 0)


        # cтворюємо словник з значеннями відстаней до представлених дошок від даної
        distance_to = {}
        distance_to[self._initial_board] = 0
        # словник, що описує зв'язність систем розв'язків(шлях з однієї в іншу)
        boards_connection_route = {}
        boards_connection_route[self._initial_board] = None

        while not queue.is_empty():
            # виймаємо дошку з найменшою відстанню
            my_board = queue.pop_min_el()
            # перевіряємо, чи є вона взагалі розв'язком
            if my_board.solution_check():
                break
            # якщо ні, то берем всі "сусідні дошки" до поданої
            for neighbor in my_board.neighbors():
                # наступна частина виконується, якщо такий хід ми ще не перевіряли
                # бо його нема всловнику
                if neighbor not in distance_to:
                    # записуємо її в словник з дистанцією на 1 більшою, аніж у поточної
                    distance_to[neighbor] = distance_to[my_board] + 1
                    # додаємо її в чергу, опираючись на відстань до неї, як на пріоритетність
                    queue.add(neighbor, distance_to[neighbor])
                    # записуємо в словник зв'язності, що шлях до дошки-сусіда йшов через подану
                    boards_connection_route[neighbor] = my_board
        # тут ми вже знайшли розв'язок
        # формуємо список для всіх дошок, що пов'язали задану від початку та кінцеву
        solution_way = []
        while my_board is not None:
            # починаючи з дошки-розв'язку додаємо -1 крок від однієї до іншої
            # аж допоки не дійдемо до 0ї(першої) дошки з умови
            solution_way.append(my_board)
            my_board = boards_connection_route[my_board]

        solution_way = solution_way[::-1]
        return solution_way


class Min_proir_queue:
    # прописуєм логіку розставлення елементів в черзі
    def __init__(self):
        # ліст з чергою
        self.pq = []
        self.tree_size = 0

    def replace(self, i, j):
        # міняємо місцями елементи
        self.pq[i - 1], self.pq[j - 1] = self.pq[j - 1], self.pq[i - 1]

    def add(self, board, priority):
        # додаємо вершину в дерево, збільшуємо його розмір
        self.pq.append((board, priority))
        self.tree_size += 1
        # підіймаємо її за потреби(якщо вона має вищу пріоритетність)
        self.swim(self.tree_size)

    def pop_min_el(self):
        # зменшуємо чергу видаляючи найнижчий за пріоритетністю елемент і
        # занурюємо той, що перед ним на його місце
        # ну і черга зменшується на 1 позицію
        if self.tree_size == 0:
            raise IndexError("Priority queue underflow")
        self.replace(1, self.tree_size)
        board, _ = self.pq.pop()
        self.tree_size -= 1
        # занурюємо передостанню вершину нижче по дереву
        self.sink(1)
        return board

    def swim(self, k):
        # допоки батько має меншу пріоритетність за нащадка - міняємо їх місцями
        while k > 1 and self.greater(k // 2, k):
            self.replace(k, k // 2)
            k = k // 2

    def sink(self, k):
        while 2 * k <= self.tree_size:
            j = 2 * k
            if j < self.tree_size and self.greater(j, j + 1):
                j += 1
            if not self.greater(k, j):
                break
            self.replace(k, j)
            k = j

    def greater(self, i, j):
        # порівнюємо, хто з двох елементів є пріоритетнішим
        _, priority_i = self.pq[i - 1]
        _, priority_j = self.pq[j - 1]
        return priority_i > priority_j

    def is_empty(self):
        return self.tree_size == 0

    def tree_size(self):
        return self.tree_size


def read_data_from_file(filename):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            row = line.strip().split()
            matrix.append([int(num) for num in row])
    return matrix


def main():
    list = read_data_from_file("/your/path/puzzle31.txt")
    board = Board(list[0][0], list[1:])
    board.hamming()
    board.manhattan()
    solver = Solver(board)
    # repr нашу board
    print(board.__str__())
    if not solver.is_solvable():
        print("Board does not have solutions")
    else:
        print(f"Minimal number of steps {len(solver.moves())-1}")
        i = 1
        for board in solver.moves():
            if i == 1:
                print("INITIAL BOARD:")
            else:
                print(f"STEP NUMBER {i-1}:")
            print(board)
            i += 1


if __name__ == "__main__":
    main()