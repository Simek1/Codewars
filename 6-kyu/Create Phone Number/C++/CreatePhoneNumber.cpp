#include <string>

std::string createPhoneNumber(const int arr [10]){
  std::string result = "(";
  for (int i = 0; i < 10; i++)
  {
    result+=std::to_string(arr[i]);
    if (i == 2) result+=") ";
    if (i == 5) result+='-';
  }
    return result;
}
