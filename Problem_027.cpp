#include <iostream>
#include <cmath>
#include <ctime>

using namespace std;
bool isPrime(int n);
double primeElapsed, mainElapsed;

int main() {

	clock_t start = clock();
	//int a = -79, b = 1601;
				for (int n = 0; n <= 100; n++) {

					//calculate results
					result = n * n + n * a + b;

					//check if the current value is prime;
					if (isPrime(abs(result))) {
						lastWasPrime = true;

						//cout << n << "^2 + \t" << a << "n +\t" << b << " = \t" << result << endl;

					} else {
						lastWasPrime = false;
					}

					//check if the last was prime, if not, stop counting and see if it was more than the last run.
					//Then take the a and b values for the sequence
					if (mostInRow < currentInRow) {
						mostInRow = currentInRow;
						mostPosition[0] = a;
						mostPosition[1] = b;
						//break from loop
					}

					if (lastWasPrime) {
						currentInRow++;
					} else {
						currentInRow = 0;
						break;
					}

				}
	int result = 0, factor = 1000;
	int mostInRow = 0, currentInRow = 0;
	int mostPosition[2];
	bool lastWasPrime = false;

	for (int a = -factor; a < factor; a++) {
		for (int b = 0; b <= factor; b++) {
//int a = -79, b = 1601;
			for (int n = 0; n <= 100; n++) {

				//calculate results
				result = n * n + n * a + b;

				//check if the current value is prime;
				if (isPrime(abs(result))) {
					lastWasPrime = true;

					//cout << n << "^2 + \t" << a << "n +\t" << b << " = \t" << result << endl;

				} else {
					lastWasPrime = false;
				}

				//check if the last was prime, if not, stop counting and see if it was more than the last run.
				//Then take the a and b values for the sequence
				if (mostInRow < currentInRow) {
					mostInRow = currentInRow;
					mostPosition[0] = a;
					mostPosition[1] = b;
					//break from loop
				}

				if (lastWasPrime) {
					currentInRow++;
				} else {
					currentInRow = 0;
					break;
				}

			}
			currentInRow = 0;

		}

	}

	cout << "Most primes in a row: " << mostInRow << endl;
	cout << "Occurred at: a = " << mostPosition[0] << " b = " << mostPosition[1]
			<< endl;
	cout << "a * b = " << mostPosition[0] * mostPosition[1] << endl << endl;

	clock_t end = clock();

	double elapsed = double(end - start) / CLOCKS_PER_SEC;
	primeElapsed = primeElapsed / CLOCKS_PER_SEC;
	double mainElapsed = elapsed - primeElapsed;

	int a = mostPosition[0], b = mostPosition[1];
	for (int n = 0; n <= 100; n++) {
		//calculate results
		result = n * n + n * a + b;

		//check if the current value is prime;
		if (isPrime(abs(result))) {
			lastWasPrime = true;

			cout << "Prime #";
			if(n < 9) cout << "0";
			cout << n + 1<< ":\t" <<  n << "^2 + \t" << a << "n +\t" << b << " = \t" << result << endl;

		} else {
			lastWasPrime = false;
		}

		//check if the last was prime, if not, stop counting and see if it was more than the last run.
		//Then take the a and b values for the sequence
		if (mostInRow < currentInRow) {
			mostInRow = currentInRow;
			mostPosition[0] = a;
			mostPosition[1] = b;
			//break from loop
		}

		if (lastWasPrime) {
			currentInRow++;
		} else {
			currentInRow = 0;
			break;
		}

	}

	cout << "\n\nTotal time Elapsed: " << elapsed << " seconds.";
	cout << "\nisPrime - time Elapsed: " << primeElapsed << " seconds.";
	cout << "\nmain time Elapsed: " << mainElapsed << " seconds.";

	return 0;
}

bool isPrime(int n) {
	//int sqrtN = sqrt(n);

	clock_t start = clock();
	if (n < 3)
		return false;

	for (int i = 2; i * i < n; i++) {
		if (n % i == 0) {
			return false;
		}
	}
	clock_t end = clock();

	primeElapsed += double(end - start);
	return true;
}
