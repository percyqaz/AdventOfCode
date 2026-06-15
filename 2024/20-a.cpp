#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <queue>
#include <map>

__int64 solution_20_a(const char* input)
{
	std::ifstream file(input);
	_ASSERT(file.is_open());
	std::string line;
	size_t grid_size{ 0 };
	size_t x{ 0 };
	std::pair<size_t, size_t> start;
	std::pair<size_t, size_t> end;
	auto lines = std::vector<std::string>();
	auto queue = std::queue<std::pair<size_t, size_t>>();
	while (std::getline(file, line))
	{
		x = line.find('S');
		if (x != std::string::npos)
		{
			start = { x, grid_size };
		}
		x = line.find('E');
		if (x != std::string::npos)
		{
			end = { x, grid_size };
		}
		lines.push_back(line);
		grid_size++;
	}
	lines[start.second][start.first] = '.';
	lines[end.second][end.first] = '.';
	auto distances = std::vector<std::vector<__int64>>(grid_size, std::vector<__int64>(grid_size, -1));
	queue.push(end);
	distances[end.second][end.first] = 0;
	size_t pass{ 1 };
	do {
		for (size_t i = queue.size(); i; i--)
		{
			const std::pair<size_t, size_t>& t{ queue.front() };
			size_t x = t.first;
			size_t y = t.second;
			queue.pop();

			if (x > 0 && lines[y][x - 1] == '.' && distances[y][x - 1] < 0)
			{
				distances[y][x - 1] = pass;
				queue.push({ x - 1, y });
			}
			if (x + 1 < grid_size && lines[y][x + 1] == '.' && distances[y][x + 1] < 0)
			{
				distances[y][x + 1] = pass;
				queue.push({ x + 1, y });
			}
			if (y > 0 && lines[y - 1][x] == '.' && distances[y - 1][x] < 0)
			{
				distances[y - 1][x] = pass;
				queue.push({ x, y - 1 });
			}
			if (y + 1 < grid_size && lines[y + 1][x] == '.' && distances[y + 1][x] < 0)
			{
				distances[y + 1][x] = pass;
				queue.push({ x, y + 1 });
			}
		}
		pass++;
	} while (queue.size());
	std::map<__int64, int> savings{};
	__int64 answer{ 0 };
	for (size_t y = 1; y < grid_size - 3; y++)
	{
		for (size_t x = 1; x < grid_size - 3; x++)
		{
			if (distances[y][x] < 0) continue;
			__int64 y_saving = std::abs(distances[y][x] - distances[y + 2][x]) - 2;
			if (distances[y + 2][x] < 0)
				y_saving = 0;
			__int64 x_saving = std::abs(distances[y][x] - distances[y][x + 2]) - 2;
			if (distances[y][x + 2] < 0)
				x_saving = 0;

			if (y_saving > 0)
			{
				std::cout << distances[y][x] << " -> " << distances[y + 2][x] << " saving " << y_saving << std::endl;
				savings[y_saving]++;
			}

			if (x_saving > 0)
			{
				std::cout << distances[y][x] << " -> " << distances[y][x + 2] << " saving " << x_saving << std::endl;
				savings[x_saving]++;
			}

			if (y_saving >= 100)
				answer++;
			if (x_saving >= 100)
				answer++;
		}
	}

	for (size_t y = 0; y < grid_size; y++)
	{
		for (size_t x = 0; x < grid_size; x++)
		{
			printf("%03i ", static_cast<int>(distances[y][x]));
		}
		std::cout << "\n";
	}

	for (auto& s : savings)
	{
		std::cout << s.second << " ways to save " << s.first << std::endl;
	}

	return answer;
}