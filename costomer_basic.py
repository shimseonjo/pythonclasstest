import re
custlist=[{'name': 'honggildong', 'gender': 'M', 'email': 'a@gmail.com', 'birthyear': '2000'}]
page=-1


while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''').upper()  

    if choice=="I":        
        print("고객 정보 입력")
        customer={'name':'','gender':'',"email":'',"birthyear":''}
        customer['name'] = input('이름 >>> ')
        while True:
            customer['gender'] = input('성별입력(m/M,f/F) >>>').upper()
            if customer['gender'] in ('M',"F"):
                break
        while True:
            customer['email'] = input('이메일 입력>>> ')
            check = 0
            for i in custlist:
                if i['email'] == customer['email']:
                    check = 1
                    break
            if check == 0:
                break
            print('중복되는 이메일이 있습니다.')    
        while True:
            customer['birthyear'] = input('태어난 연도 입력(4자리) >>>')
            if str(customer['birthyear']).isdigit() and len(customer['birthyear']) == 4 :
                customer['birthyear'] = int(customer['birthyear'])
                break
        print(customer)
    elif choice=="C":
        print("현재 고객 정보 조회")
    elif choice == 'P':
        print("이전 고객 정보 조회")
    elif choice == 'N':
        print("다음 고객 정보 조회")
    elif choice=='D':
        print("고객 정보 삭제")
    elif choice=="U": 
        print("고객 정보 수정")
    elif choice=="Q":
        print("프로그램 종료")
        break
    else:
        print("메뉴선택을 잘못하셨습니다.")
