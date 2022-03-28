#include <SFML/Graphics.hpp>
#include<math.h>

int main()
{
	int x;
	sf::RenderWindow window(sf::VideoMode(1024, 1024), "Graph");
	//sf::RectangleShape Graph(sf::Vector2f(1024.0f, 1024.0f));
	//Graph.setFillColor(sf::Color::Black);
	//Graph.setOrigin(sf::Vector2f(512.0f, 512.0f));
	
	sf::VertexArray xaxis(sf::Lines, 2u);
	sf::VertexArray yaxis(sf::Lines, 2u);
	
	xaxis[0].position = sf::Vector2f(0, 512);
	xaxis[1].position = sf::Vector2f(1024, 512);
	yaxis[0].position = sf::Vector2f(512, 0);
	yaxis[1].position = sf::Vector2f(512, 1024);

	xaxis[0].color = sf::Color::White;
	xaxis[1].color = sf::Color::White;
	yaxis[0].color = sf::Color::White;
	yaxis[1].color = sf::Color::White;


	sf::VertexArray line(sf::LinesStrip,1024u);
	
	
	while (window.isOpen())
	{
		sf::Event evnt;
		while (window.pollEvent(evnt))
		{
			if (evnt.type == sf::Event::Closed)
			{
				window.close();
			}
		}
		for (x = -512; x < 512; x++)
		{
			line.append(sf::Vertex(sf::Vector2f(512 + x, -(256*sin(3.14/512*x) - 512))));
			//line[x+512].position = sf::Vector2f(x+512, (x*x)/100-3*x/10-50  +512);
			line[x + 512].color = sf::Color::White;
		}
		window.clear(sf::Color::Black);
		window.draw(xaxis);
		window.draw(yaxis);
		window.draw(line);
		window.display();
	}
	
	return 0;
}