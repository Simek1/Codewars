std::string spinWords(const std::string &str){
    std::vector<std::string> words;
    std::string word = "";
    for (int i = 0; i < str.length(); i++){
        if (str[i] != ' '){
            word += str[i]; 
        } else {
            words.push_back(word);
            word = "";
        };
    };
    words.push_back(word);
    word="";
    std::string result = "";
    for (int i = 0; i < words.size(); i++){
        if (words[i].size() >= 5){
            for (int j = words[i].length() - 1; j >= 0; j--){
                word += words[i][j];
            };
        } else {
            word = words[i];
        };
        if (i == words.size()-1){
            result += word;
        } else {
            result += word + " ";
        };
        word = "";
    };

    return result;
}
