# include <stdio.h>
# include <stdlib.h>

int main()
{
  int *values[7];
  
  for (int val = 0; val < 7; val++) values[val] = calloc(1, sizeof(int));

  for (int i = 0; i < 6; i++)
  {
    int x;
    printf("Value %d > ", i+1);
    scanf("%d", &x);
    *values[i] = x;
  }
  
  for (int j0 = 0; j0 < 5; j0++)
  {
    for (int j1 = 0; j1 < 5; j1++)
    {
      for (int j2 = 0; j2 < 5; j2++)
      {
        if (*values[j2] > *values[j2+1])
        {
          int temp;
          temp = *values[j2];
          *values[j2] = *values[j2+1];
          *values[j2+1] = temp;
        }
      }
    }
  }
  
  printf("\n");
  
  for (int k = 0; k < 6; k++)
  {
    if (k == 0) printf("[ ");
    printf("%d ", *values[k]);
    if (k == 5) printf("]");
  }
  
  printf("\n");
  
  return 0;
}
