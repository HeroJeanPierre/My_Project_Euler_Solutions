#include <iostream>

using namespace std;

int pent(int n);
bool isPent(int p);

int main() {
	int sum, diff;

	for (int i = 1; i < 10000; i++) {
		for (int j = 1; j < 10000; j++) {
			sum = pent(j) + pent(i);
			diff = pent(i) - pent(j);
			if (isPent(diff) && isPent(sum)) {
				cout << "P" << i << " + " << "P" << j << " = " << pent(i) << " + " << pent(j) << " = " << sum << endl;
				cout << "P" << j << " - " << "P" << i << " = " << pent(j) << " - " << pent(i) << " = " << diff << endl;

			}
		}
	}

	return 0;
}

int pent(int n) {
	return n * (3 * n - 1) / 2;
}

bool isPent(int p) {
	for (int i = 1; i < 10000; i++) {
		if (p == pent(i)) {
			return true;
		}
	}
	return false;
}
