#include <iostream>

using namespace std;

int main()
{
	int count;

	cout << "Enter the count of the sequence: ";
	cin >> count;

	int seq[count];
	seq[0] = 0;
	seq[1] = 1;
	seq[2] = 1;

	for (int i = 3; i < count; i++)
		seq[i] = seq[i - 1] + seq[i - 2];

	for (int i = 0; i < count; i++)
		cout << seq[i] << endl;

	return 0;
}
