using namespace std;
class Bouncingball{
public:
    static int bouncingBall(double h, double bounce, double window){
        if (h > 0 and bounce > 0 and bounce < 1 and window < h){
            double ball_h = h;
            int res = 0;
            while (ball_h > window){
                ball_h *= bounce;
                res += 2;
            };
            res --;
            return res;
        } else {
            return -1;
        };
    };
};
