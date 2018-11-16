while True:
    #c = int(input("請輸入攝氏溫度:")) 溫度應為浮點數
    c = float(input("請輸入攝氏溫度:"))
    print ("您輸入的攝氏溫度為:", c)
    check = input("是否正確(Y/N)?")
    if check == 'Y' or check == 'y':
        f = c * 9 / 5 + 32       
        print ("對應華氏溫度為:", f)
        break
    else:
        print("請重新輸入攝氏溫度!")




