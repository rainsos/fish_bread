# stock(변수/딕셔너리) 
stock = {
    "팥붕어빵": 10,
    "슈크림붕어빵": 8,
    "초코붕어빵": 5
}

# 판매(변수/딕셔너리)
sales =  {
    "팥붕어빵": 0,
    "슈크림붕어빵": 0,
    "초코붕어빵": 0
}

# 가격(변수/딕셔너리)
price =  {
    "팥붕어빵": 1000,
    "슈크림붕어빵": 800,
    "초코붕어빵": 900
}

# 주문 기능
def order_bread():
    print("🍞 안녕하세요! 빵 주문 시스템에 오신 것을 환영합니다! 🍞\n")
    while True:
        bread_type = input("주문할 붕어빵을 선택하세요 (팥붕어빵, 슈크림붕어빵, 초코붕어빵) 또는 '뒤로가기' 입력 : ")
        if bread_type == "뒤로가기":
            break
        
        # 메뉴 주문
        if bread_type in stock:
            
            try:
                bread_count = int(input("주문할 갯수를 입력하세요"))

                if bread_count < 0:
                    print("❌ 붕어빵 개수는 음수일 수 없습니다. 다시 입력해주세요.\n")
                    break  

                if stock[bread_type] >= bread_count:
                    stock[bread_type] -= bread_count
                    sales[bread_type] += bread_count
                    print(f"✅ {bread_type} {bread_count}개가 주문되었습니다.\n")
                    print(f"📦 남은 재고: {stock[bread_type]}개\n")
                    print(f"💰 현재 판매량: {sales[bread_type]}개\n")
        
                else:
                   print(f"❌ 재고가 부족합니다. 현재 {bread_type} 재고는 {stock[bread_type]}개입니다.\n")
        
            except ValueError:
                print("❌ 잘못된 입력입니다. 숫자로 입력해주세요.\n")

                
        else:
            print("❌ 해당 붕어빵은 존재하지 않습니다. 다시 입력해주세요.\n")
      
#관리자모드
def admin_mode():
    while True:
        bread_type = input("추가할 붕어빵을 선택하세요 (팥붕어빵, 슈크림붕어빵, 초코붕어빵) 또는 '종료' 입력 : ")
        if bread_type == "종료":
            break

        if bread_type in stock:
            
            try:
                bread_count = int(input("추가할 개수를 입력하세요 : "))
                
                if bread_count < 0:
                    print("❌ 붕어빵 개수는 음수일 수 없습니다. 다시 입력해주세요.\n")
                    break  
                
                stock[bread_type] += bread_count
                print(f"✅ {bread_type} {bread_count}개가 추가 되었습니다.\n")
                print(f"📦 현재 재고: {stock[bread_type]}개\n")

            except ValueError:
                print("❌ 잘못된 입력입니다. 숫자로 입력해주세요.\n")

        else:
            print("❌ 해당 붕어빵은 존재하지 않습니다. 다시 입력해주세요.\n")

def calculate_sales():
    total_sales = 0  # 총 판매 금액 초기화

    # 각 붕어빵 종류에 대해 판매 금액을 계산하여 합산
    for key in sales:
        total_sales += (price[key] * sales[key])
        print(f"💰 총 판매액: {total_sales}원")
        return total_sales # 리턴을 안쓸경우에는 그냥 프린트만 출력 리턴을써서 밖에서 다른변수로 저장해서 사용하려면 리턴사용
    # return total_sales # total_sales 값이 calculate_sales로 저장되며 total_sales_price = calculate_sales() 홒출했을때 값을가져온다다 

while True:
    mode = input("원하는 모드를 선탁하세요 ( 주문, 관리자, 종료 : ")
    if mode == "종료":
        print("프로그램을 종료합니다.")
        break
      
    elif mode =="주문":
        print("주문 모드로 이동합니다.")
        order_bread()

    elif mode == "관리자":
        print("관리자 모드로 이동합니다")
        admin_mode()

    else:
        print("잘못된 입력입니다. '주문', '관리자', '종료' 중에서 선택해주세요.")

# 판매액 계산하기
calculate_sales()