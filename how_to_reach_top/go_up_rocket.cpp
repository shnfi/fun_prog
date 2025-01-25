#include <iostream>
#include <ncurses.h>
#include <unistd.h>

#include "map.cpp"

#define MAX_HEIGHT 1

void try_to_move(int *y)
{
	srand(time(NULL));
	int new_y = ((rand() % 2) == 0) ? 1 : -1;

	*y += new_y;

	refresh();
}

int main()
{
	initscr();
	cbreak();
	noecho();
	nodelay(stdscr, TRUE);
	curs_set(0);

	int y = 5;

	for (int i = 0; i < HEIGHT; i++)
	{
		for (int j = 0; j < WIDTH; j++)
		{
			mvprintw(i, j, "%c", map[i][j]);
		}

		printw("\n");
	}

	while (true)
	{
		mvprintw(10, 10, "y: %d", y);

		mvprintw(y - 1, 3, " ");
		mvprintw(y + 1, 3, " ");

		mvprintw(y, 3, "A");

		if (y == 1)
		{
			mvprintw(13, 1, "Yes, the rocket goes out of the earth!");
			refresh();
			sleep(5);
			break;
		}
		else if (y == 10)
		{
			mvprintw(13, 1, "Oh, the rocket crashed!");
			refresh();
			sleep(5);
			break;
		}

		try_to_move(&y);

		sleep(1);
	}


	endwin();

	return 0;
}
