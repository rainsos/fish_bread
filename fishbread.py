# 붕어빵 가격이 필요해요
price = {
    "팥붕어빵" : 1000,
    "슈크림붕어빵" : 1200,
    "초코붕어빵" : 1500
}

# 붕어빵 판매갯수수
sales = {
    "팥붕어빵" : 0,
    "슈크림붕어빵" : 0,
    "초코붕어빵" : 0
}

def calculate_sales():
    total_sales = 0  # 총 판매 금액 초기화

    # 각 붕어빵 종류에 대해 판매 금액을 계산하여 합산
    for key in sales:
        total_sales += (price[key] * sales[key])

    print(f"💰 총 판매액: {total_sales}원") # 리턴을 안쓸경우에는 그냥 프린트만 출력 리턴을써서 밖에서 다른변수로 저장해서 사용하려면 리턴사용
    return total_sales # total_sales 값이 calculate_sales로 저장되며 total_sales_price = calculate_sales() 홒출했을때 값을가져온다다 

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