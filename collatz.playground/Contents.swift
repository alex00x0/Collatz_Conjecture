import UIKit

//let num = pow(10,2)
//let run = Double(num)

var y = 0;

for i in 99...100 {
    var x = i;
    while (x != 1){
        if x % 2 == 0{
        x = x/2;
        }
        else {
            x = x * 3 + 1;
        }
        print(x);
    }
    y = y + 1;
}
print(y)

