std::vector<int> reverseSeq(int n) {
  std::vector<int> nums;
  for (int i = n; i > 0; i--) {
    nums.push_back(i);
  }
  return nums;
}
