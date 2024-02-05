std::vector<int> deleteNth(std::vector<int> arr, int n){
  std::unordered_map<int, int> myMap={};
  int j = 0;
  std::vector<int> arr_copy = arr;
  for (int i = 0; i < arr.size(); i++){
    myMap[arr[i]]++;
    if (myMap[arr[i]] > n){
      arr_copy.erase(arr_copy.begin() + j);
      j--;
    };
    j++;
  };
  return arr_copy;
}
