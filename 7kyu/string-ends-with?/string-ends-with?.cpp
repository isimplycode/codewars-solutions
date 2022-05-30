#include <string>
bool solution(std::string const &str, std::string const &ending) {
    int x = ending.length();
    if (str.length() < ending.length()) {
        return false;
    }
    std::string y = str.substr(str.length() - x);
    return y == ending;
}
