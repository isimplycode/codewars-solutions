#include <bits/stdc++.h>
using namespace std;

int sum_intervals(std::vector<std::pair<int, int>> intervals) {
  sort(begin(intervals),end(intervals));
  vector<pair<int,int>> temp;
  int i=0;
  while (i<size(intervals)-1) {
    if (intervals[i].second>=intervals[i+1].first) {
      intervals[i+1].first=intervals[i].first;
      intervals[i+1].second=max(intervals[i+1].second,intervals[i].second);
    } else {
      temp.push_back(intervals[i]);
    }
    ++i;
  }
  temp.push_back(intervals[i]);
  int res=0;
  for (int i=0; i<size(temp); ++i) {
    res+=temp[i].second-temp[i].first;
  }
  return res;
}
