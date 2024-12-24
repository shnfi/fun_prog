#include <iostream>

using namespace std;

int main()
{
	long values[6];

	for (int i = 0; i < 6; i++)
	{
		cout << "value " << i + 1 << " > ";
		cin >> values[i];
	}

	// sorting process

	for (int i = 0; i < 6; i++)
	{
		for (int j = 0; j < 6; j++)
		{
			for (int k = 0; k < 6; k++)
			{
				if (values[k] > values[k + 1])
				{
					int tmp = values[k];
					values[k] = values[k + 1];
					values[k + 1] = tmp;
				}
			}
		}
	}

	// displaying process

	for (int i = 0; i < 6; i++)
		if (i == 0)
			cout << endl << "[ " << values[i] << " ";

		else if (i == 5)
			cout << values[i] << " ]" << endl;

		else
			cout << values[i] << " ";

	return 0;
}
