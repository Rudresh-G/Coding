#include<iostream>
#include<math.h>
void img(float a, float D, float &Xi)
{
	Xi = std::sqrt(D) / (2 * a);
}
int main()
{
	float a, b, c, D, Xr, Xi;
	std::cout << "Enter the Variables:";
	std::cin >> a >> b >> c;
	Xr = -b / (2 * a);
	D = b * b - 4 * a * c;
	if (D < 0)
	{
		D = -D;
		img(a, D, Xi);
		std::cout << "The Complex roots are:"<<std::endl<<"x1="<<Xr<<"+"<<Xi<<"i"<<std::endl<<"x2="<< Xr << "-" << Xi << "i" << std::endl;
	}
	else if (D == 0)
	{
		std::cout << "The only root is:" << std::endl << "x=" << Xr << std::endl;
	}
	else
	{
		img(a, D, Xi);
		std::cout << "The Real roots are:" << std::endl << "x1=" << Xr + Xi << std::endl << "x2=" << Xr - Xi << std::endl;
	}	
	return 0;
}