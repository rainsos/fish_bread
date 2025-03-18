# stock(변수/딕셔너리) 
stock = {
    "팥붕어빵": 10,
    "슈크림붕어빵": 8,
    "초코붕어빵": 5
}

# 판매(변수/딕셔너리리)
sales =  {
    "팥붕어빵": 0,
    "슈크림붕어빵": 0,
    "초코붕어빵": 0
}

# 주문 기능
def order_bread():
    print("🍞 안녕하세요! 빵 주문 시스템에 오신 것을 환영합니다! 🍞\n")
    while True:
        bread_type = input("주문할 붕어빵을 선택하세요 (팥붕어빵, 슈크림붕어빵, 초코붕어빵) 또는 '뒤로가기' 입력 : ").strip().lower()
        if bread_type == "뒤로가기".strip().lower():
            break
        
        # 메뉴 주문
        if bread_type in stock:
            
            try:
                bread_count = int(input("주문할 갯수를 입력하세요"))
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









#메인 기능 선택
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

