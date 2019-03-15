#include <iostream>
#include <vector>
#include <random>
#include <functional>
#include <algorithm>

using namespace std;

int main()
{
	random_device seeder;
	const auto seed = seeder.entropy() ? seeder() : time(nullptr);
	mt19937 eng(static_cast<mt19937::result_type>(seed));
	uniform_int_distribution<int> dist(1, 99);

	auto gen = std::bind(dist, eng);
	vector<int> vec(10);

	generate(begin(vec), end(vec), gen);

	for (auto i : vec) { 
		cout << i << " "; }

	cout << endl;
}


