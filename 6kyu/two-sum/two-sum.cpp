using namespace std;
pair<std::size_t, std::size_t> two_sum(const vector<int>& numbers, int target) {
  pair<int,int> res;
  unordered_map<int,int> m;
  for (int i=0; i<size(numbers); ++i) {
    if (m.find(target-numbers[i])!=m.end()) {
      return {m[target-numbers[i]],i};
    } else {
      m[numbers[i]]=i;
    }
  }
  return {0, 0};
}
