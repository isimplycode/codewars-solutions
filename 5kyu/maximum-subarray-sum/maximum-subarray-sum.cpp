#include <vector>

int maxSequence(const std::vector<int>& arr){
    int maxsum = 0;
    int currsum = 0;
    for (int i = 0; i < arr.size(); i++) {
        currsum += arr[i];
        if (currsum < 0) {
            currsum = 0;
        }
        if (currsum > maxsum) {
            maxsum = currsum;
        }
    }
    return maxsum;
}
