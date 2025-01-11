#include <iostream>
#include <unistd.h>
#include <ncurses.h>

#include "map.cpp"

#define UPDATE_TIME 75000

using namespace std;

class CHARACTER
{
public :
	int x;
	int y;
	int speed;
	char sprite;
	int health;

	void render(int p_y, int p_x)
	{
		mvprintw(p_y, p_x, " ");

		mvprintw(this->y, this->x, "%c", this->sprite);
		refresh();

		usleep(UPDATE_TIME);
	}
};

class PLAYER : public CHARACTER
{
public : 
	char direction;

	PLAYER(int x, int y, int speed, char sprite, int health)
	{
		this->x = x;
		this->y = y;
		this->speed = speed;
		this->sprite = sprite;
		this->health = health;
		this->direction = 'd';

		this->render(this->y, this->x);
	}

	void move()
	{
		int p_y = this->y;
		int p_x = this->x;

		if (this->direction == 'w')
			this->y -= this->speed;

		else if (this->direction == 'a')
			this->x -= this->speed * 2; // because we multiply the map's width to 2 (for more beautiful render)

		else if (this->direction == 's')
			this->y += this->speed;

		else if (this->direction == 'd')
			this->x += this->speed * 2; // because we multiply the map's width to 2 (for more beautiful render)


		this->render(p_y, p_x);
	}

	void change_direction(char new_direction)
    {
        if (new_direction == 'w' || new_direction == 'a' || new_direction == 's' || new_direction == 'd')
            this->direction = new_direction;
    }
};

class MAP
{
public :
	int height = MAP_HEIGHT;
	int width = MAP_WIDTH;

	void show_map()
	{
		for (int i = 0; i < height; i++)
		{
			for (int j = 0; j < width; j++)
			{
				mvprintw(i, j, "%c", map[i][j]);
			}
	
			printw("\n");
		}

		refresh();
	}
};

int main()
{
	initscr();
	cbreak();
	noecho();
	nodelay(stdscr, TRUE);

	bool abort = false;

	MAP m1;
	m1.show_map();

	/*
	 * CHARACTER ROLES :
	 *
	 * player -> it is the main character of the game, its you!
	 * enemy1 -> it is the normal enemy with 1 health and a normal speed. 
	 * enemy2 -> it is the normal enemy with 2 health and a normal speed. 
	 * enemy3 -> it is the normal enemy with 2 health and a high speed. 
	 */

	PLAYER player(1, 1, 1, 'O', 3);

	while (!abort)
	{
		int key = getch();

		if (key != ERR)
        {
            player.change_direction((char) key);
        }

        player.move();

        usleep(UPDATE_TIME);
	}

	endwin();
	return 0;
}
