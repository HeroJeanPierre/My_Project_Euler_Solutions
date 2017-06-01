#include <iostream>
#include <string>

using namespace std;

int main (){

	long first = 1, second = 1, next, sum = 0;



	for(int i = 0; i <= 4000000; i++){
		next = first + second;
		first = second;
		second = next;

		if(next % 2 == 0){
			sum += next;
		}
		if(next > 4000000){
			break;
		}
	}

	cout << "The sum of fib elements under 4million that are even is: " << sum;


	return 0;
}
