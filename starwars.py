import os
import time

def main():
    LINES_PER_FRAME = 14
    DELAY = 67
    with open(os.path.join(os.path.dirname(__file__), 'starwars.txt'), 'r') as file:
        film_data = file.read().split('\n')
    print('\n' * LINES_PER_FRAME)
    for i in range(0, len(film_data), LINES_PER_FRAME):
        # Nascondi il cursore
        print('\x1b[?25l', end='')
        print('\x1b[{}A\x1b[J{}'.format(LINES_PER_FRAME, '\n'.join(film_data[i + 1:i + LINES_PER_FRAME])), end='')
        time.sleep(int(film_data[i]) * DELAY / 1000)
        # Riattiva il cursore
        print('\x1b[?25h', end='')

main()
