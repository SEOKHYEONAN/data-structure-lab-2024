#include<cstdio>
#include "Car.h"
#include "Rectangle"

int main() {
	Car myCar(50, "K3", 4);
	Car yourCar(100, "K5", 3);
	myCar. display();
	yourCar. display();
	myCar. whereAmI();
	yourCar. whereAmI();

	Rectangle r(10, 20) :
		double perimeter = r.getPerimeter();
	std::cout << "Rectangle 1:" << std::endl;
	std::cout << "Area:" << r. getarea() << std::endl;
	std::cout << "Perimeter"<< perimeter << std::endl;
	std::cout << "is square:" << std::endl;
}


