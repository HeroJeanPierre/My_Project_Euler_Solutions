#include <iostream>
#include <string>

using namespace std;

int main (){

	int sum = 0;

	for(int i = 1; i <= 1000; i++){
		if(i % 3 == 0|| i % 5 == 0){
			sum += i;
		}

	}
	cout << "The sum of the elements divisible by 3 or 5 is: " << sum;
	return 0;
}
