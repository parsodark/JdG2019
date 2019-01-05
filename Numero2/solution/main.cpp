// Solution Numero 2
// Acad Informatique JDG2019
// Polytechnique Montréal
// Olivier Gareau
// 5 janvier 2019

#include <iostream>
#include <sstream>
#include <string>

int countConsecutive(std::string line)
{
	int count = 0;
	for (size_t i = 1; i < line.size(); i++) {
		if (line[i] == line[i - 1]) {
			count++;
		}
	}
	return count;
}

int countE(std::string line)
{
	int count = 0;
	for (size_t i = 0; i < line.size(); i++) {
		if (line[i] == 'e') {
			count++;
		}
	}
	return count;
}

int countWords(std::string line)
{
	int count = 0;
	std::stringstream stream(line);
	std::string buf;

	while (stream >> buf) {
		count++;
	}
	return count;
}

int main()
{
	std::cout << "Bienvenue au simulateur de président." << std::endl;
	
	for (;;) {
		std::string line;
		std::getline(std::cin, line);

		// Si rien, on continue
		if (line.size() == 0) {
			continue;
		}

		// Si 1 char, refused
		if (line.size() == 1) {
			std::cout << "Refused" << std::endl;
			continue;
		}

		int consecutiveCount = countConsecutive(line);
		int eCount = countE(line);
		int wordCount = countWords(line);

		if (!(consecutiveCount <= wordCount)) {
			if (!(consecutiveCount <= eCount)) {
				std::cout << "Accepted" << std::endl;
				continue;
			}
		}

		if (!(wordCount <= consecutiveCount)) {
			if (!(wordCount <= eCount)) {
				std::cout << "Refused" << std::endl;
				continue;
			}
		}

		std::cout << "Negotiate" << std::endl;
	}

	return 0;
}