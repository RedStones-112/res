#include <iostream>

int make_num(int *pointer_number){
    int result, num1;
    num1 = *pointer_number / 10 + *pointer_number % 10;
    if (num1 >= 10){
        num1 = num1 % 10;
    }
    *pointer_number = *pointer_number % 10 * 10 + num1;
    return 0;
}

int main(){
    int N;
    std::cout << "0에서 99사이의 정수를 입력하세요"<< '\n';
    std::cin >> N;
    
    int num = N;
    int *pointer_num = &num;
    
    if ( N < 0 || N > 99){
        std::cout << "조건에 충족되는 값이 아닙니다.";
    }

    if(N < 10){
        N*=10;
    }
    
    int a = 1;
    make_num(pointer_num);
    while(num!=N){
        make_num(pointer_num);
        a+=1;
        std::cout<< "num = " << num << '\n' << N << '\n';
        std::cout<< "loop_count = " << a << '\n';
    }

    std::cout << a;
    return 0;
    

}