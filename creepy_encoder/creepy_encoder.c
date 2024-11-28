#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

char *encode(int ran, char val[], int s, int m, int h)
{
	int n = 1;
	int key;
	char *str = malloc(strlen(val));

	memset(str, 0, sizeof(str));

	if (ran == 1) key = s;
	else if (ran == 2) key = m;
	else if (ran == 3) key = h;

	for (int i = 0; i < strlen(val); i++)
	{
		int x = rand() % (5 - 1 + 1) + 1;

		str[strlen(str)] = (char) (key + 65) + n;
		n += x;
	}

	return str;
}

int main(int argc, char **argv)
{
	time_t t = time(NULL);
	struct tm tm = *localtime(&t);
	
	srand(time(NULL));
	
	int ran = rand() % (3 - 1 + 1) + 1;

	/*
	 * starting to encode
	 */

	for (int i = 1; i < argc; i++)
	{
		printf("%s\n", encode(ran, argv[i], tm.tm_sec, tm.tm_min, tm.tm_hour));
	}

	return 0;
}
