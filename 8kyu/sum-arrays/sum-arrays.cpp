#include <vector>

int sum(std::vector<int> nums) {
  int returnsum = 0;
  for (int i = 0; i < nums.size(); i++) {
    returnsum += nums[i];
  }
  return returnsum;
}
