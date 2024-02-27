#include <bitset>

unsigned int countBits(unsigned long long n){
    std::bitset<sizeof(long) * 8 > binary(n);
    int s = 0;
    for (int i = 0; i < size(binary); i++){
        if (binary[i] == 1){
            s += 1;
        };
    };
    return s;
}
