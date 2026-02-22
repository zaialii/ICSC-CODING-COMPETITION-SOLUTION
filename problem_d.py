import sys
import random

def create_crossword(words: list) -> list:
    """
    Generate a 10x10 word search puzzle containing the given words.
    
    Args:
        words: A list of words to include in the puzzle.
        
    Returns:
        A 2D array (list of lists) representing the word search puzzle.
    """
    # WRITE YOUR CODE HERE


    size = 10
    grid = [['' for _ in range(size)] for _ in range(size)]

    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]  # right, down, diagonal-down, diagonal-up

    def can_place(word, x, y, dx, dy):
        for i, ch in enumerate(word):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= size or ny >= size:
                return False
            if grid[nx][ny] not in ('', ch):
                return False
        return True

    def place_word(word):
        for _ in range(200):
            x, y = random.randint(0, size - 1), random.randint(0, size - 1)
            dx, dy = random.choice(directions)
            if can_place(word, x, y, dx, dy):
                for i, ch in enumerate(word):
                    nx, ny = x + i * dx, y + i * dy
                    grid[nx][ny] = ch
                return True
        return False

    for word in words:
        word = word.lower().strip()
        if word:
            if not place_word(word):
                place_word(word[::-1])

    letters = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(size):
        for j in range(size):
            if grid[i][j] == '':
                grid[i][j] = random.choice(letters)

    return grid



# --- Main execution block. DO NOT MODIFY.  ---
if __name__ == "__main__":
    try:
        # Read words from first line (comma-separated)
        words_input = input().strip()
        words = [word.strip() for word in words_input.split(',')]
        
        # Generate the word search puzzle
        puzzle = create_crossword(words)
        
        # Print the result as a 2D grid
        for row in puzzle:
            print(''.join(row))
            
    except ValueError as e:
        print(f"Input Error: {e}", file=sys.stderr)
        sys.exit(1)
    except EOFError:
        print("Error: Not enough input lines provided.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)