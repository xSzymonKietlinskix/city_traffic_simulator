import heapq
class Cell:
    def __init__(self):
        self.parent_i = 0  # Parent row index
        self.parent_j = 0  # Parent column index
        self.f = float('inf')  # Total cost (g + h)
        self.g = float('inf')  # g cost
        self.h = 0  # h cost

# Czy pole jest w obszarze?
def is_valid(row, col, L):
    return (row >= 0) and (row < L) and (col >= 0) and (col < L)

# Czy pole jest zablokowane?
def is_unblocked(city, row, col):
    return city[row][col] == 0

# Czy pole jest metą?
def is_destination(row, col, end):
    return row == end[0] and col == end[1]

# Liczenie heurestyki = odległość euklidesowa
def h_cost(row, col, end):
    return ((row - end[0]) ** 2 + (col - end[1]) ** 2) ** 0.5

# Znajdowanie ścieżki
def trace_path(cell_details, dest):
    path = []
    row = dest[0]
    col = dest[1]

    # Pętla od mety do startu
    while not (cell_details[row][col].parent_i == row and cell_details[row][col].parent_j == col):
        path.append((row, col))
        temp_row = cell_details[row][col].parent_i
        temp_col = cell_details[row][col].parent_j
        row = temp_row
        col = temp_col

    # Dodanie mety do ścieżki
    path.append((row, col))
    # Odwrócenie ścieżki, tak aby prowadziła od startu do mety
    path.reverse()
    return path

# Algorytm a* do znajdowania ścieżki
def a_star(city, start, end, L):
    # Zabezpieczenie jeżeli start == end
    if start == end:
        print("Start = Meta")
        return None

    # Closed list = lista odwiedzonych punktów. Jest to dwuwymiarowa lista, początkowo zawierająca wartości FALSE
    closed_list = [[False for _ in range(L)] for _ in range(L)]
    # Lista dwuwymiarowa zawierająca informacje o danych polach
    cell_details = [[Cell() for _ in range(L)] for _ in range(L)]

    # Inicjalizacja pola startowego
    i = start[0]
    j = start[1]
    cell_details[i][j].f = 0
    cell_details[i][j].g = 0
    cell_details[i][j].h = 0
    cell_details[i][j].parent_i = i
    cell_details[i][j].parent_j = j

    # Stworzenie listy punktów do odwiedzenia i dodanie tam punktu startowego
    open_list = []
    heapq.heappush(open_list, (0.0, i, j))

    # Główna pęla A*
    while len(open_list) > 0:
        # Wybranie punktu z najniższym kosztem całkowitym
        p = heapq.heappop(open_list)

        # Oznaczenie punktu jako odwiedzonego
        i = p[1]
        j = p[2]
        closed_list[i][j] = True

        # Sprawdzenie punków w lewo, prawo, góra, dół
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dir in directions:
            new_i = i + dir[0]
            new_j = j + dir[1]
            # Jeżeli punk jest niezablokowany, znajduje się w polu planszy oraz nie był już odwiedzony
            if is_valid(new_i, new_j, L) and is_unblocked(city, new_i, new_j) and not closed_list[new_i][new_j]:
                # Jeżeli jest to meta
                if is_destination(new_i, new_j, end):
                    cell_details[new_i][new_j].parent_i = i
                    cell_details[new_i][new_j].parent_j = j
                    print("Znaleziono drogę do mety!")
                    path = trace_path(cell_details, end)
                    return path
                else:
                    # Obliczenie kosztu
                    g_new = cell_details[i][j].g + 1.0
                    h_new = h_cost(new_i, new_j, end)
                    f_new = g_new + h_new

                    # Dodanie punktu do listy do odwiedzenia, jeżeli go tam nie ma lub znaleziono krótszą drogę do niego
                    if cell_details[new_i][new_j].f == float('inf') or cell_details[new_i][new_j].f > f_new:
                        heapq.heappush(open_list, (f_new, new_i, new_j))
                        cell_details[new_i][new_j].f = f_new
                        cell_details[new_i][new_j].g = g_new
                        cell_details[new_i][new_j].h = h_new
                        cell_details[new_i][new_j].parent_i = i
                        cell_details[new_i][new_j].parent_j = j

    #Jeżeli nie znaleziono ścieżki
    print("Nie isteniej ścieżka ze startu do mety!")
    return None
