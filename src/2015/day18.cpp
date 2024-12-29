#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <filesystem>
#include <algorithm>

std::vector<std::pair<int, int>> directions = {
    {-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};

int find_neighbors(std::vector<std::vector<char>> &matrix, int y, int x, size_t size_y, size_t size_x)
{
    int alive_neighbors = 0;
    int yy, xx;
    for (std::pair dir : directions)
    {
        yy = y + dir.first, xx = x + dir.second;
        if (yy >= 0 && yy < size_y && xx >= 0 && xx < size_x)
        {
            if (matrix[yy][xx] == '#')
            {
                alive_neighbors += 1;
            }
        }
    }
    return alive_neighbors;
}

int solve(bool part2 = false)
{
    std::ifstream file("inputs/2015/day18.txt");
    if (!file)
    {
        std::cerr << "Unable to open file\n";
        return 1;
    }

    std::vector<std::vector<char>> matrix; // 2D vector to store characters
    std::string line;
    while (std::getline(file, line))
    {
        std::vector<char> row(line.begin(), line.end()); // Convert string to vector of chars
        matrix.push_back(row);
    }

    std::vector<std::vector<char>> matrix2(100, std::vector<char>(100, '.'));

    size_t size_y = matrix.size();
    size_t size_x = matrix[0].size();
    for (int i = 0; i < 100; i++)
    {
        for (size_t y = 0; y < size_y; y++)
        {
            for (size_t x = 0; x < size_x; x++)
            {
                int neighbors = find_neighbors(matrix, y, x, size_y, size_x);
                if (matrix[y][x] == '#')
                {
                    if (neighbors == 2 || neighbors == 3)
                    {
                        matrix2[y][x] = '#';
                    }
                    else
                    {
                        matrix2[y][x] = '.';
                    }
                }
                else
                {
                    if (neighbors == 3)
                    {
                        matrix2[y][x] = '#';
                    }
                    else
                    {
                        matrix2[y][x] = '.';
                    }
                }
            }
        }
        // Correct for Part 2
        if (part2)
        {
            matrix2[0][0] = '#';
            matrix2[99][0] = '#';
            matrix2[0][99] = '#';
            matrix2[99][99] = '#';
        }
        matrix = std::move(matrix2);
    }

    int count = 0;
    for (const auto &row : matrix)
    {
        count += std::count(row.begin(), row.end(), '#');
    }
    return count;
}

int main()
{
    std::cout << solve() << std::endl;
    std::cout << solve(true) << std::endl;
}