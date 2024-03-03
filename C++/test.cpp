#include <iostream>

int main(void) {
    int x = 5;
    int y[4] = {0, 1, 2, 3};
    
    int *ptr = &y[0];
    std::cout << *(y+2) << '\n';
    std::cout << ptr+2 << '\n';
    //std::cout << x << '\n';  // print the value of variable x
    //std::cout << &x << '\n'; // print the memory address of variable x
    std::cout << "test" << y;
    return 0;
}
