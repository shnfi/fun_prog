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

	REMINDER 

	- configuring the cards and they're usages .
	- and probably the hardest one, creating the scoreboard system .

*/ 

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
    printf("[1] guess the gol\n[2] hit a pooch\n[3] using a card (coming soon)\n[4] exit\n\n> ");
}

void guessing_the_gol(int hands[3][2], int gol_person, int gol_hand, int *poochs)
{
	int gol_person_guess, gol_hand_guess;

	printf("\n\nYour target > ");
	scanf("%d", &gol_person_guess);

	printf("His hand > ");
	scanf("%d", &gol_hand_guess);

	if (
		gol_person_guess == gol_person && 
		gol_hand_guess == gol_hand 
	)
	{
		printf("\n\nYou won!\n");
		*poochs = 10;
	}
	else
	{
		printf("\n\nYou lost! you chosed a pooch hand!\n");
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

	pooch_person--;
	pooch_hand--;

	if (hands[pooch_person][pooch_hand] != 1)
	{
		hands[pooch_person][pooch_hand] = 2;
		visual_hands[pooch_person][pooch_hand] = 2;
		*poochs += 1;
		
		if (*poochs == 5)
		{
			printf("\n\nYou won!\n");
			*poochs = 10;
		}
	}
	else
	{
		printf("\n\nYou lost! you pooched a gol hand!\n");
		*poochs = 10;
	}
}

void using_a_card()
{}

void quit_the_game(int *poochs)
{
	printf("\n\nThanks for playing!\n");
	*poochs = 10;
}

int main()
{
	int hands[3][2] = {{0, 0}, {0, 0}, {0, 0}};
	int visual_hands[3][2] = {{0, 0}, {0, 0}, {0, 0}};
	int random_person, random_hand;
	int *poochs = calloc(1, sizeof(int));
	*poochs = 0;

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
	
	while (*poochs != 10) {
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
				using_a_card(); // coming soon (actually im gonna code it myself so...)
				break;
	
			case 4 : 
				quit_the_game(poochs);
				break;
	
			default : 
				printf("\n\n[E] invalid choice!");
				break;
		}
	}
	
	return 0;
}
