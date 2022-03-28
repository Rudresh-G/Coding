#include <iostream>
using namespace std;
class customer {
public:
	int add(int a, int b)
	{
		return (a + b);
	}
};

int main()
{
	int x, y,ans;
	customer c;
	cout << "Enter two numbers\n";
	cin >> x >> y;
	ans = c.add(x, y);
	cout << ans;
	return 0;
}