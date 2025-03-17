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

