#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>
#include <string.h>

typedef struct club
{
	char name[20];
	int point;
	int pl;
} CLUB;

void simulate(CLUB clubs[], bool uesr_want_to_see_fixtures)
{
	srand(time(NULL));

	if (uesr_want_to_see_fixtures)
		printf("\n");
		
	for (int i = 0; i < 20; i++)
	{
		for (int j = 0; j < 20; j++)
		{
			if (clubs[i].name != clubs[j].name)
			{
				int t1_goal = rand() % 6;
				int t2_goal = rand() % 6;

				char wld;
	
				if (t1_goal > t2_goal)
				{
					clubs[i].point += 3;
					wld = 'w';
				}
				else if (t1_goal < t2_goal)
				{
					clubs[j].point += 3;
					wld = 'l';
				}
				else
				{
					clubs[i].point += 1;
					clubs[j].point += 1;
					wld = 'd';
				}

				if (uesr_want_to_see_fixtures)
				{
					if (wld == 'w')
					{
						printf("\033[0;32m");
						printf("%s %d - %d %s\n", clubs[i].name, t1_goal, t2_goal, clubs[j].name);
						printf("\033[0m");
					}
					if (wld == 'd')
					{
						printf("\033[0;37m");
						printf("%s %d - %d %s\n", clubs[i].name, t1_goal, t2_goal, clubs[j].name);
						printf("\033[0m");
					}
					else
					{
						printf("\033[0;31m");
						printf("%s %d - %d %s\n", clubs[i].name, t1_goal, t2_goal, clubs[j].name);
						printf("\033[0m");
					}
				}

				clubs[i].pl += 1;
				clubs[j].pl += 1;
			}
		}
	
		if (uesr_want_to_see_fixtures)
			printf("\n#-----------------------------------#\n\n");
	}

	printf("\n");

	for (int i = 0; i < 19; i++)
	{
		for (int j = 0; j < 19; j++)
		{
			if (clubs[j].point < clubs[j+1].point)
			{
				char tmp_name[20];
				int tmp_point;

				strcpy(tmp_name, clubs[j].name);
				tmp_point = clubs[j].point;

				strcpy(clubs[j].name, clubs[j + 1].name);
				clubs[j].point = clubs[j + 1].point;

				strcpy(clubs[j + 1].name, tmp_name);
				clubs[j + 1].point = tmp_point;
			}
		}
	}

	printf("  ------------------------------------------\n");

	printf(" |   pos    club                 pl   pt    |\n");

	printf("  ------------------------------------------\n");

	for (int i = 0; i < 20; i++)
	{
		printf(" | ");

		if (i == 0 || i == 1 || i == 2 || i == 3)
		{
			printf("\033[0;34m");
			printf("# ");
			printf("\033[0m");			
		}
		else if (i == 4)
		{
			printf("\033[0;33m");
			printf("# ");
			printf("\033[0m");			
		}
		else if (i == 5)
		{
			printf("\033[0;32m");
			printf("# ");
			printf("\033[0m");			
		}
		else if (i == 17 || i == 18 || i == 19)
		{
			printf("\033[0;31m");
			printf("# ");
			printf("\033[0m");
		}
		else
		{
			printf("\033[0;37m");
			printf("# ");
			printf("\033[0m");
		}

		printf("[%02d]   %s   %*d   %d    |\n", i + 1, clubs[i].name, 20 - (int) strlen(clubs[i].name), clubs[i].pl, clubs[i].point);
	}

	printf("  ------------------------------------------\n\n");
}

int main()
{
	bool uesr_want_to_see_fixtures;
	char ans[1];

	CLUB atletico_madrid = { "Atletico Madrid", 0, 0};
	CLUB real_madrid = { "Real Madrid", 0, 0};
	CLUB barcelona = { "Barcelona", 0, 0};
	CLUB athletic_bilbao = { "Athletic Bilbao", 0, 0};
	CLUB villarreal = { "Villarreal", 0, 0};
	CLUB real_mallorca = { "Real Mallorca", 0, 0};
	CLUB real_sociedad = { "Real Sociedad", 0, 0};
	CLUB girona = { "Girona", 0, 0};
	CLUB real_betis = { "Real Betis", 0, 0};
	CLUB osasuna = { "Osasuna", 0, 0};
	CLUB celta_vigo = { "Celta Vigo", 0, 0};
	CLUB rayo_vallecano = { "Rayo Vallecano", 0, 0};
	CLUB las_palmas = { "Las Palmas", 0, 0};
	CLUB sevilla = { "Sevilla", 0, 0};
	CLUB leganes = { "Leganes", 0, 0};
	CLUB alaves = { "Alaves", 0, 0};
	CLUB getafe = { "Getafe", 0, 0};
	CLUB espanyol = { "Espanyol", 0, 0};
	CLUB valencia = { "Valencia", 0, 0};
	CLUB real_valladolid = { "Real Valladolid", 0, 0};

	CLUB clubs[20] = {
		 atletico_madrid,
		 real_madrid,
		 barcelona,
		 athletic_bilbao,
		 villarreal,
		 real_mallorca,
		 real_sociedad,
		 girona,
		 real_betis,
		 osasuna,
		 celta_vigo,
		 rayo_vallecano,
		 las_palmas,
		 sevilla,
		 leganes,
		 alaves,
		 getafe,
		 espanyol,
		 valencia,
		 real_valladolid
	};

	system("clear");

	printf("Do you want to see fixtures? [y/n] ");
	
	scanf("%s", ans);

	if (strcmp(ans, "y") == 0)
		uesr_want_to_see_fixtures = true;
	else if (strcmp(ans, "n") != 0)
	{
		printf("\nInvalid choice!\n");
		return 1;
	}

	simulate(clubs, uesr_want_to_see_fixtures);

	return 0;
}
