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

	# there is nothing to do anymore!

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
	printf("0 = in game hand   1 = gol hand   2 = pooch hand\n\n");
   	show_visual_hands(visual_hands);
    printf("[1] guess the gol\n[2] hit a pooch\n[3] using a card\n[4] exit\n\n> ");
}

void guessing_the_gol(int hands[3][2], int *poochs)
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

	gol_person_guess--;
	gol_hand_guess--;

	if (hands[gol_person_guess][gol_hand_guess] == 1)
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

void hazfe_dast_card(int hands[3][2], int visual_hands[3][2], int *poochs, int *remaining)
{
	if (*remaining == 1)
	{
		int random_person = rand() % (2 - 0 + 1) + 0;
		int random_hand = rand() % (1 - 0 + 1) + 0;

		if (hands[random_person][random_hand] != 1)
		{
			hands[random_person][random_hand] = 2;
			visual_hands[random_person][random_hand] = 2;
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

		*remaining -= 1;
	}
	else
	{
		printf("\n\n%s\n", COOR_ERR);
		sleep(2);
	}
}

void sang_moft_card(int hands[3][2], int visual_hands[3][2], int *poochs, int *remaining)
{
	if (*remaining == 1) {
		int gol_person_guess, gol_hand_guess;
	
		printf("\n\nYour target > ");
		scanf("%d", &gol_person_guess);
	
		printf("His hand > ");
		scanf("%d", &gol_hand_guess);
	
		gol_person_guess--;
		gol_hand_guess--;
	
		if (hands[gol_person_guess][gol_hand_guess] == 1)
		{
			printf("\n\n");
			show_the_gol(hands);
			printf("\n\nYou won!\n");
			sleep(6);
			*poochs = 10;
		}
		else
		{
			hands[gol_person_guess][gol_hand_guess] = 2;
			visual_hands[gol_person_guess][gol_hand_guess] = 2;
			*poochs += 1;
		}
	
		*remaining -= 1;
	}
	else
	{
		printf("\n\n%s\n", COOR_ERR);
		sleep(2);
	}
}


int main()
{
	int hands[3][2] = {{0, 0}, {0, 0}, {0, 0}};
	int visual_hands[3][2] = {{0, 0}, {0, 0}, {0, 0}};
	int random_person, random_hand;
	int *poochs = calloc(1, sizeof(int));
	*poochs = 0;

	int *remaining_antens = calloc(1, sizeof(int));
	*remaining_antens = 1;

	int *remaining_hazfe_dasts = calloc(1, sizeof(int));
	*remaining_hazfe_dasts = 1;

	int *remaining_sang_mofts = calloc(1, sizeof(int));
	*remaining_sang_mofts = 1;

	srand(time(NULL));
	printf("\e[1;1H\e[2J");

	random_person = rand() % (2 - 0 + 1) + 0;
	random_hand = rand() % (1 - 0 + 1) + 0;

	randomize_the_gol(hands, random_person, random_hand);

	int user_choice;
	
	while (*poochs != 10) 
	{
		printf("\e[1;1H\e[2J");
		show_menu(hands, visual_hands);

		scanf("%d", &user_choice);

		switch (user_choice)
		{
			case 1 : 
				guessing_the_gol(hands, poochs);
				break;
	
			case 2 : 
				hit_a_pooch(hands, visual_hands, poochs);
				break;
	
			case 3 : 
				int c;
				printf("\n\n[1] Anten (%d remaining)\n[2] Hazfe dast (%d remaining)\n[3] Sang moft (%d remaining)\n\n> ", *remaining_antens, *remaining_hazfe_dasts, *remaining_sang_mofts);
				scanf("%d", &c);

				switch (c)
				{
					case 1 : 
						anten_card(hands, poochs, remaining_antens);
						break;

					case 2 : 
						hazfe_dast_card(hands, visual_hands, poochs, remaining_hazfe_dasts);
						break;

					case 3 : 
						sang_moft_card(hands, visual_hands, poochs, remaining_sang_mofts);
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
