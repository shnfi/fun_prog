# include <stdio.h>
# include <stdlib.h>
# include <time.h>
# include <unistd.h>

/*

	NOTES

	0 -> playing hand (not null yet) .
	1 -> has the gol .
	2 -> pooch .

	ending tasks of the main method by setting the "poochs" to 10 .

*/

/*

	TODO 

	- configuring the cards and they're usages .

*/ 

# define NV_ERR "[E] invalid choice!"
# define COOR_ERR "[E] card out of range!"

void randomize_the_gol(int hands[3][2], int r_person, int r_hand)
{
	hands[r_person][r_hand] = 1;
}

void show_the_gol(int hands[3][2])
{
	for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            printf("%d ", hands[i][j]);
        }

        if (i < 2) printf("     ");
    }

	printf("\n");
}

void show_visual_hands(int visual_hands[3][2])
{
	for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            printf("%d ", visual_hands[i][j]);
        }

        if (i < 2) printf("     ");
    }

	printf("\n\n");
}

void show_menu(int hands[3][2], int visual_hands[3][2])
{
	//show_the_gol(hands); // debug line. remove me later!
   	show_visual_hands(visual_hands);
    printf("[1] guess the gol\n[2] hit a pooch\n[3] using a card\n[4] exit\n\n> ");
}

void guessing_the_gol(int hands[3][2], int gol_person, int gol_hand, int *poochs)
{
	int gol_person_guess, gol_hand_guess;

	printf("\n\nYour target > ");
	scanf("%d", &gol_person_guess);

	printf("His hand > ");
	scanf("%d", &gol_hand_guess);

	if (gol_person_guess <= 0 || gol_person_guess >= 4) 
	{
		printf("\n\n%s\n", NV_ERR);
		sleep(6);
		*poochs = 10;
	}
	
	if (gol_hand_guess <= 0 || gol_hand_guess >= 3) 
	{
		printf("\n\n%s\n", NV_ERR);
		sleep(6);
		*poochs = 10;
	}

	if (
		gol_person_guess == gol_person && 
		gol_hand_guess == gol_hand 
	)
	{
		printf("\n\n");
		show_the_gol(hands);
		printf("\n\nYou won!\n");
		sleep(6);
		*poochs = 10;
	}
	else
	{
		printf("\n\n");
		show_the_gol(hands);
		printf("\n\nYou lost! you chosed a pooch hand!\n");
		sleep(6);
		*poochs = 10;
	}
}

void hit_a_pooch(int hands[3][2], int visual_hands[3][2],  int *poochs)
{
	int pooch_person, pooch_hand;

	printf("\n\nYour target > ");
    scanf("%d", &pooch_person);

    printf("His hand > ");
    scanf("%d", &pooch_hand);

	if (pooch_person <= 0 || pooch_person >= 4) 
	{
		printf("\n\n%s\n", NV_ERR);
		sleep(6);
		*poochs = 10;
	}
	
	if (pooch_hand <= 0 || pooch_hand >= 3) 
	{
		printf("\n\n%s\n", NV_ERR);
		sleep(6);
		*poochs = 10;
	}

	pooch_person--;
	pooch_hand--;

	if (hands[pooch_person][pooch_hand] != 1)
	{
		hands[pooch_person][pooch_hand] = 2;
		visual_hands[pooch_person][pooch_hand] = 2;
		*poochs += 1;
		
		if (*poochs == 5)
		{
			printf("\n\n");
			show_the_gol(hands);
			printf("\n\nYou won!\n");
			sleep(6);
			*poochs = 10;
		}
	}
	else
	{
		printf("\n\n");
		show_the_gol(hands);
		printf("\n\nYou lost! you pooched a gol hand!\n");
		sleep(6);
		*poochs = 10;
	}
}

void quit_the_game(int *poochs)
{
	printf("\n\nThanks for playing!\n");
	*poochs = 10;
}

void anten_card(int hands[3][2], int *poochs, int *remaining)
{
	if (*remaining == 1)
	{
		int target;

		printf("\n\nYour target > ");
		scanf("%d", &target);

		if (target <= 0 || target >= 4) printf("\n\n%s\n", NV_ERR);

		target--;

		if (hands[target][0] != 1 && hands[target][1] != 1)
		{
			printf("\n\nI CANNOT SEE THE GOL!\n");
			sleep(2);
		}
		else
		{
			printf("\n\nI CAN SEE THE GOL\n");
			sleep(2);
		}

		*remaining -= 1;
	}
	else
	{
		printf("\n\n%s\n", COOR_ERR);
		sleep(2);
	}
}

void sang_moft_card()
{}

void hazfe_dast_card()
{}

int main()
{
	int hands[3][2] = {{0, 0}, {0, 0}, {0, 0}};
	int visual_hands[3][2] = {{0, 0}, {0, 0}, {0, 0}};
	int random_person, random_hand;
	int *poochs = calloc(1, sizeof(int));
	*poochs = 0;

	int *remaining_antens = calloc(1, sizeof(int));
	*remaining_antens = 1;

	srand(time(NULL));
	printf("\e[1;1H\e[2J");

	random_person = rand() % (2 - 0 + 1) + 0;
	random_hand = rand() % (1 - 0 + 1) + 0;

	int gol_person, gol_hand;

	randomize_the_gol(hands, random_person, random_hand);

	for (int i = 0; i < 3; i++)
	{
		for (int j = 0; j < 2; j++)
		{
			if (hands[i][j] == 1)
			{
				gol_person = i;
				gol_hand = j;
			}
		}
	}

	gol_person++;
	gol_hand++;

	int user_choice;
	
	while (*poochs != 10) 
	{
		printf("\e[1;1H\e[2J");
		show_menu(hands, visual_hands);

		scanf("%d", &user_choice);

		switch (user_choice)
		{
			case 1 : 
				guessing_the_gol(hands, gol_person, gol_hand, poochs);
				break;
	
			case 2 : 
				hit_a_pooch(hands, visual_hands, poochs);
				break;
	
			case 3 : 
				int c;
				printf("\n\n[1] Anten (%d remaining)\n[2] Sang moft (coming soon)\n[3] Hazfe dast (coming soon)\n\n> ", *remaining_antens);
				scanf("%d", &c);

				switch (c)
				{
					case 1 : 
						anten_card(hands, poochs, remaining_antens);
						break;

					case 2 : 
						sang_moft_card();
						break;

					case 3 : 
						hazfe_dast_card();
						break;

					default :
						printf("\n\n%s\n", NV_ERR);
						sleep(2);
						break;
				}

				break;
	
			case 4 : 
				quit_the_game(poochs);
				break;
	
			default : 
				printf("\n\n%s\n", NV_ERR);
				sleep(2);
				break;
		}
	}
	
	return 0;
}
