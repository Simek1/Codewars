std::string encrypt(std::string text, int n){
    while (n > 0){
        std::string even = "";
        std::string odd = "";
        for (int i = 0; i < text.length(); i++){
            if(i % 2 == 0){
                even += text[i];
            } else {
                odd += text[i];
            };
        };
        text = odd + even;
        n--;
    };
    return text;
}

std::string decrypt(std::string encryptedText, int n){
    int text_length = encryptedText.length();
    while (n>0){
        std::string odd = encryptedText.substr(0,text_length/2);
        std::string even = encryptedText.substr(text_length/2);
        std::string decrypted_text = "";
        for (int i = 0; i < text_length; i++){
            if (i % 2 == 0){
                decrypted_text += even[i / 2];
            } else {
                decrypted_text += odd[i / 2];
            };
        };
        encryptedText = decrypted_text;
        n--;
    };
    return encryptedText;
}
