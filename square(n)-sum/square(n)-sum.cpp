#include <vector>

int square_sum(const std::vector<int>& numbers)
{
    int returnsum = 0;
    for (int i = 0; i < numbers.size(); i++) {
      returnsum += numbers[i]*numbers[i];
    }
    return returnsum;
}
