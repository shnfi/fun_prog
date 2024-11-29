#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

char *encode(char val[], int s)
{
	char *str = malloc(strlen(val));

	memset(str, 0, sizeof(str));

	for (int i = 0; i < strlen(val); i++)
	{
		str[strlen(str)] = (char) (s + 65) + i;
	}

	return str;
}

int main(int argc, char **argv)
{
	time_t t = time(NULL);
	struct tm tm = *localtime(&t);
	
	srand(time(NULL));
	
	/*
	 * starting to encode
	 */

	for (int i = 1; i < argc; i++)
	{
		printf("%s\n", encode(argv[i], tm.tm_sec + i));
	}

	return 0;
}
