#include <iostream>
#include <math.h>
using namespace std;

#define PI 3.14159265

int main(){
    double r, h, d1, a1, d2, a2;
    while(!cin.eof()){
        cin >> r >> h >> d1 >> a1 >> d2 >> a2;
        double result = sqrt(pow(d1*sin(fabs(a1-a2)*PI/180.0), 2) + pow(d2-d1*cos(fabs(a1-a2)*PI/180.0), 2));
        cout << result << endl;
    }
}