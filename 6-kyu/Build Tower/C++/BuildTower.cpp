#include <string>
#include <vector>

std::vector<std::string> towerBuilder(int nFloors) {
    std::vector<std::string> tower;
    int spaces = nFloors-1;
    int blocks = 1;
    std::string spaces_str = "";
    std::string floor = "";
    for (int x = 0; x < nFloors; x++){
        for (int spc = 0; spc < spaces; spc++){
            spaces_str += " ";
        };
        floor += spaces_str;
        for (int bl = 0; bl<blocks; bl++){
            floor += "*";
        };
        floor += spaces_str;
        tower.push_back(floor);
        spaces -= 1;
        blocks += 2;
        spaces_str = "";
        floor = "";
    }
    return tower;
};
