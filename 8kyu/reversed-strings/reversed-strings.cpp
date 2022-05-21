#include <string>
using namespace std ; 

string reverseString (string str )
{
  string returnstring;
  for (int i = str.size()-1; i >= 0; i--) {
    returnstring += str[i];
  }
  return returnstring;
}