#include<iostream>
const float coef[3][3]{ {0,-1,-512},{1,0,512},{0,0,1} };

int main()
{
	float x, y, X, Y;
	int i, j;
	std::cout << "Enter coordinates" << std::endl;
	std::cin >> x >> y;
	float input[3], output[3] = {0,0,0};
	input[0] = x;
	input[1] = y;
	input[2] = 1;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			output[i] += coef[i][j] * input[j];
		}
		
	}
	X = output[0];
	Y = output[1];
	std::cout << "New Coordinates are:\nX= " << X << "\nY= " << Y << std::endl;
	
	return 0;
}