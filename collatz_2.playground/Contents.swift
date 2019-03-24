import UIKit

var x: UInt64 = 1844674407370955161;

var steps = 0;

while (x != 1){
    if x % 2 == 0{
        x = x/2;
        steps += 1;
    }
    else {
        x = x * 3 + 1;
        steps += 1;
        print(x);
    }
}
print("steps: \(steps)");


