#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <unistd.h>
#include <time.h>

void show(char *board[10][10], int *x, int *y)
{
	system("clear");

	printf("x %d - y %d\n", *x + 1, *y + 1);

	for (int i = 0; i < 10; i++)
	{
		for (int j = 0; j < 10; j++)
		{
			printf("[%s]", board[i][j]);
		}
		printf("\n");
	}
}

void move(char *board[10][10], int *x, int *y, bool *WIN, int *loses)
{
	printf("\n");

	srand(time(NULL));

	int dice = rand() % (6) + 1;

	board[*y][*x] = " ";

	if ((*x + dice) > 9)
	{
		if (*y < 9)
		{
			*x = (*x + dice) - 10;
			*y += 1;
		}
	}
	else
		*x += dice;

	/*
	 * checking if player lose or not
	 */

	if (board[*y][*x] == " ")
	{
		board[*y][*x] = "o";
	}
	else if (board[*y][*x] == "x")
	{
		board[*y][*x] = "x";
		board[0][0] = "o";
		*loses += 1;

		/*
		 * reseting the cordinate
		 */

		*x = 0;
		*y = 0;
	}
	else if (board[*y][*x] == "H")
	{
		board[*y][*x] = "o";
		show(board, x, y);
		*WIN = true;
	}
}

int main()
{
	int x = 0, y = 0;
	int loses = 0;

	bool WIN = false;

	/*
	 * 'o' = player
	 * 'x' = snake's head
	 * ' ' = empty block
	 * 'H' = home
	 */

	char *board[10][10] = {
		"o", " ", " ", " ", " ", " ", " ", " ", " ", " ", 
		" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", 
		" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", 
		" ", " ", " ", " ", "x", " ", " ", " ", "x", " ", 
		" ", " ", " ", " ", " ", " ", " ", "x", " ", " ", 
		" ", "x", " ", " ", " ", " ", " ", " ", " ", " ", 
		" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", 
		" ", " ", " ", " ", " ", " ", " ", "x", " ", " ", 
		" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", 
		" ", " ", " ", " ", "x", " ", "x", " ", " ", "H", 
	};

	while (!WIN)
	{
		show(board, &x, &y);
		move(board, &x, &y, &WIN, &loses);
		sleep(1);
	}

	printf("\n\nPLAYER WON WITH %d LOSES!\n", loses);
}
