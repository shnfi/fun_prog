# include <stdio.h>
# include <stdlib.h>
# include <string.h>

int main()
{
	int count = 5;

	printf("count > ");
	scanf("%d", &count);

	int seq[count];
	memset(seq, 0, count * sizeof(int));
	seq[0] = 0;
	seq[1] = 1;
	seq[2] = 1;

	for (int i = 3; i < count; i++)
	{
		seq[i] = seq[i-1] + seq[i-2];
	}

	for (int i = 0; i < count; i++)
		printf("%d\n", seq[i]);

	return 0;
}
