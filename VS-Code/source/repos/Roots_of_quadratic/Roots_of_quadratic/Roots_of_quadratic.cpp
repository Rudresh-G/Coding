#include<iostream>
#include<math.h>
using namespace std;
float *quad(float a, float b, float c)
{
	float x1, x2;
	x1 = (b + sqrt(b * b - 4 * a * c)) / 2 * a;
	x2 = (b - sqrt(b * b - 4 * a * c)) / 2 * a;
	static float arr[] = { x1,x2 };
	return arr;
}

int main()
{
	float a, b, c,x1,x2,D;
	float *p;
	float *quad(float a, float b, float c);
	cout << "enter coeficients" <<endl;
	cin >> a >> b >> c;
	D = b * b - 4 * a * c;
	if (D < 0)
	{
		cout << "The roots are imaginary" << endl;
	}
	else
	{
		p=quad(a, b, c);
		x1 =*p;
		x2 = *(p + 1);
		cout << "x1=" <<x1 <<endl<< "x2=" << *(p+1)<<endl;
	}
	return 0;
}