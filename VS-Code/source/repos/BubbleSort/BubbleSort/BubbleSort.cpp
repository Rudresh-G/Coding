#include<iostream>

void sort(int* p)	//passing argument as a pointer, the function receives addr of arr and alters the elements there.
{
	int i,j;
	for (i = 0; i < 9; i++)
	{
		for (j = 0; j < 9; j++)
		{
			if (p[j] > p[j + 1])
			{
				std::swap(p[j], p[j + 1]);
			}
		}
	}
}

int main()
{
	int i, arr[10];
	std::cout << "Enter a few Integers"<<std::endl;
	for (i = 0; i < 10; i++)	//input array elements.
	{
		std::cin >> arr[i];
	}
	sort(arr);	//pass the array to the function "sort".
	std::cout << "The sorted array is:" << std::endl;
	for (i = 0; i < 10; i++)	//print the sorted array.
	{
		std::cout<< arr[i]<<"\t";
	}
	
	return 0;
}