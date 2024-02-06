class Accumul{
    public:
        static std::string accum(const std::string &str){
            std::string result = "";
            for (std::string::size_type i = 0; i < str.size(); i++){
                for (std::string::size_type j = 0; j <= i; j++){
                    if (j==0){
                        result += std::toupper(str[i]);
                    } else {
                        result += std::tolower(str[i]);
                    };                
                };
                result += "-";  
            };
            result.pop_back();
            return result;
    };
}
