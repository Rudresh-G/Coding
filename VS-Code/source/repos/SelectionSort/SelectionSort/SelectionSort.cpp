#include<iostream>
void sort(int *p)
{
	int startIndex, smallestIndex, CurrentIndex;
	for (startIndex = 0; startIndex < 9; startIndex++)
	{
		smallestIndex = startIndex;
		for (CurrentIndex = startIndex+1; CurrentIndex < 10; CurrentIndex++)
		{
			if (p[CurrentIndex] < p[smallestIndex])
			{
				smallestIndex = CurrentIndex;
			}
		}
		std::swap(p[smallestIndex], p[startIndex]);
	}
	
	/*int i;
	std::cout << "The sorted array is:" << std::endl;
	for (i = 0; i < 10; i++)
	{
		std::cout << p[i] << "\t";
	}*/
}

int main()
{
	int i;
	int arr[10];
	std::cout << "Enter a few integers." << std::endl;
	for (i = 0; i < 10; i++)
	{
		std::cin >> arr[i];
	}
	sort(arr);
	std::cout << "The sorted array is:" << std::endl;
	for (i = 0; i < 10; i++)
	{
		std::cout << arr[i] << "\t";
	}
	return 0;
}