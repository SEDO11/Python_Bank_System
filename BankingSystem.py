class Account:
    
    def __init__(self,i_d,password,balance):    #생성자
        self.i_d = i_d                           #계좌번호
        self.name = password                 #이름
        self.balance = balance  
        self.i_d = []
        self.password = []
        self.balance = []  
     
    def print_info(self):         #고객정보
        print("계좌번호 : ",self.i_d)
        print("비밀번호 : ",self.password)    
        print("잔고 : ",self.balance)
        
    def get_info():
        print("정보를 입력해주세요")       #정보확인을 위한 함수.
        i_d = input("계좌 번호 : ") 
        password = input("비밀번호 : ")
        return i_d,password                        #계좌번호랑 이름을 반환.

#사용자 메뉴
def view():
    running = True
    account_list = []  #정보를 담을 배열 생성.
    while running: #True를 통한 무한 반복.
        print("1.계좌개설 2.입금 3.출금 4.계좌조회 5.프로그램종료")
        choose = int(input())

        if choose == 1:   # 고객 등록
            c_register=register(account_list)   #고객 등록함수 호출.
            account_list.append(c_register)    #리스트에 리턴받은 값을 넣는다.
        
        elif choose ==2:  # 입금
            deposit(account_list)  #입금 함수 호출.
        
        elif choose ==3:  # 출금
            withdraw(account_list) #출금 함수 호출.
        
        elif choose == 4:  # 계좌 조회                 
            getBalance(account_list) #잔고 함수 호출.
            
        elif choose == 6:  #종료                  
            running = False

#계좌개설
def register(account_list):  #고객정보를 매개변수로 받는다.
    i_d = input("계좌 번호 : ")  #각각 입력받은 정보를 변수에 담는다.
    password = input("비밀 번호 : ")
    balance = int(input("예금 금액 : "))
    for i,account in  enumerate(account_list):   #기존의 고객정보를 for문을 통해 계좌정보 중복 검사.
        if account.i_d == i_d:  
            account_list[i]
            print("계좌 번호가중복됩니다. \n다시 한 번 더 입력 해주십시오.")
            register(account_list) # register 호출 위에서부터 다시 시작.
        else:  
            Account().i_d.append(i_d)                         #계좌번호
            Account().password.append(password)              #이름
            Account().balance.append(balance)      #중복이 없을때 Account타입으로 변수에 넣는다.
            print("계좌 개설이 완료되었습니다.")   
    return                                 #Account 타입의 변수 account를 반환.

#입금
def deposit(account_list):
    i_d,password = Account.get_info() #기본클래스의 개인 정보 확인 함수 호출.
    
    for i,account in  enumerate(account_list): #반복문을 통한 개인정보 확인.
        if account.password == password and account.i_d == i_d:  # id와 password 모두 같을때 if 진입.
            account_list[i] 
            print("정보가 확인 되었습니다")
            
            money=int(input("입금하실 금액을 입력해주세요 : ")) #입금 할 금액을 입력받음. 
            account_list[i].balance += money   #기존의 잔고에 입력받은 금액을 더하여 저장.
            print("입금처리가 완료되었습니다.")
            print("잔액: {0}".format(account_list[i].balance))
            return account_list   #잔고가 업데이트된 리스트를 반환.
                    
        else:
            print("입력하신 정보가 맞지 않습니다.")       #개인 정보 확인 함수에 입력한 id와password이
            break  #일치하지않을때 반복문 종료.
            
#출금
def withdraw(account_list):               
    i_d,password = Account.get_info()
    
    for i,account in  enumerate(account_list):
        if account.password == password and account.i_d == i_d:
            account_list[i]
            print("정보가 확인 되었습니다")
            
            money=int(input("출금하실 금액을 입력해주세요 : "))
            a=account_list[i].balance - money      #입금처리와 다른 부분.
            if(a<0):                                        #계산후의 잔고가 0보다 작다면 안내문 출력
                print("잔액이 부족합니다.")
            else:                                            #문제가 없다면 정상처리
                account_list[i].balance -= money           
                print("출금처리가 완료되었습니다.")
                print("잔액: {0}".format(account_list[i].balance))
                return account_list                      #잔고가 업데이트된 리스트 반환

        else:
            print("입력하신 정보가 맞지 않습니다.")
            break

#이체
def withdraw(account_list):               
    i_d,password = Account.get_info()
    
    for i,account in  enumerate(account_list):
        if account.password == password and account.i_d == i_d:
            account_list[i]
            print("정보가 확인 되었습니다")
            
            money=int(input("이체하실 금액을 입력해주세요 : "))
            a=account_list[i].balance - money      
            if(a<0):                                        #계산후의 잔고가 0보다 작다면 안내문 출력
                print("잔액이 부족합니다.")
            else:
                print("보낼사람의 계좌번호를 입력해 주세요.")                                    #문제가 없다면 정상처리
                if account.password == password and account.i_d == i_d:
                    account_list[i].balance -= money 
                    account_list[i]
                    print("정보가 확인 되었습니다")
                    account_list[i].balance += money           
                    print("출금처리가 완료되었습니다.")
                    print("잔액: {0}".format(account_list[i].balance))
                    print("잔액: {0}".format(account_list[i].balance))
                    return account_list                      #잔고가 업데이트된 리스트 반환

        else:
            print("입력하신 정보가 맞지 않습니다.")
            break

#잔액 조회
def getBalance(account_list):         # 고객 리스트를 매개변수로 받는다.
    i_d,password = Account.get_info() #기본클래스의 개인 정보 확인 함수 호출.
    
    for i,account in  enumerate(account_list): #반복문을 통한 개인정보 확인.
        if account.password == password and account.i_d == i_d:  # id와 password 모두 같을때 if 진입.
            account_list[i] 
            print("정보가 확인 되었습니다")
            print("===========계좌정보=========")
            account.print_info()
            print("========출력되었습니다.======")
            break
                    
        else:
            print("입력하신 정보가 맞지 않습니다.")       #개인 정보 확인 함수에 입력한 id와password이
            break  #일치하지않을때 반복문 종료.

view()