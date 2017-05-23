from random import choice
from string import ascii_uppercase

def make_grid(height, width):
    return {(row, col):  choice(ascii_uppercase)
                for row in range(height)
                for col in range(width)}

def neighbours_of_position(row, col):
    return [ (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
             (row, col - 1),                     (row, col + 1),
             (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]


    
def all_grid_neighbours(grid):
    neighbours = {}
    for position in grid:
        row, col = position
        position_neighbours = neighbours_of_position(row, col)
        neighbours[position] = [p for p in position_neighbours if p in grid]
    return neighbours

def path_to_word(grid, path):
    return ''.join([grid[p] for p in path])  


def search(grid, dictionary):
    neighbours = all_grid_neighbours(grid)
    paths = []
    full_words, stems = dictionary

    def do_search(path):
        word = path_to_word(grid, path)
        if word in full_words:
            paths.append(path)
        if word not in stems:
            return
        for next_pos in neighbours[path[-1]]:
            if next_pos not in path:
                do_search(path + [next_pos])
 
    for position in grid:
        do_search([position])
 
    words = []
    for path in paths:
        words.append(path_to_word(grid, path))
    return set(words) 

def get_dictionary(dictionary_file):
    full_words, stems = set(), set()

    with open(dictionary_file) as f:
        for word in f:
            word = word.strip().upper()
            full_words.add(word)

            for i in range(1, len(word)):
                stems.add(word[:i])
    return full_words,stems

def main():
    grid = make_grid(3, 3)
    dictionary = get_dictionary('bogwords.txt')
    words = search(grid, dictionary)
    for word in words:
        print(word)
    print ("Found {0} words".format(len(words)))

main()  