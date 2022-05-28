for num in range(1, 101):
    string = ''

    # ここから記述
    if num % 15 == 0:
        # 15の倍数の判定
        string= string +  "FizzBuzz"
    else:
        if num % 3 == 0:
            # 3の倍数の判定
            string= string +"Fizz"
        elif num % 5 == 0:
            # 5の倍数の判定
            string= string +"Buzz"
        else:
            string = string  + str(num) 

    # ここまで記述

    print(string)