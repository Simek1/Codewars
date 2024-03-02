std::vector<std::string> wave(std::string y){
    std::vector<std::string> result;
    for (int i = 0; i < y.length(); i++){
        if (y[i] != ' '){
            std::string word = y.substr(0, i);
            word += toupper(y[i]);
            word += y.substr(i+1);
            result.push_back(word);
        };
    };
    return result;
}
