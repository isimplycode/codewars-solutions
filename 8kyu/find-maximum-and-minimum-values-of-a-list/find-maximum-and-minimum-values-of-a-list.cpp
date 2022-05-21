#include <vector>
using namespace std;

int min(vector<int> list){
    
    int minimum=list[0];
    for(int i=0;i < list.size();i++){
      if(list[i] < minimum)
        minimum = list[i];
    }
    return minimum;
}

int max(vector<int> list){
    int maximum=list[0];
    for(int i=0;i < list.size();i++){
      if(list[i] > maximum)
        maximum = list[i];
    } 
    return maximum;
}
