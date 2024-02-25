#include <cmath>

bool narcissistic(int value){
    std::string str_value = std::to_string(value);
    int digits = str_value.length();
    int result = 0;
    for (char ch : str_value) {
        int digit = ch - '0';
        result += pow(digit, digits);
    }
    if (result == value){
        return true;
    } else {
        return false;
    };
}
