#include <vector>
std::vector<int> countBy(int x,int n){
  std::vector<int> returnarr;
  for (int i = 0; i < n; i += 1) {
    returnarr.push_back((i+1)*x);
  }
  return returnarr;
}
