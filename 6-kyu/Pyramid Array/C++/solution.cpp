#include <vector>

std::vector<std::vector<int>> pyramid(std::size_t n) {
    std::vector<std::vector<int>> result;
    std::vector<int> row;
    for (int i = 1; i <= n; i++){
        std::vector<int> row;
        for (int j = 0; j < i; j++){
            row.push_back(1);
        };
        result.push_back(row);
    };
    return result;
}
