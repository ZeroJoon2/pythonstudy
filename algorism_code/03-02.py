## 함수
def add_data(friend):
    # 1단계 빈칸 추가
    katok.append(None)

    # 배열의 길이 파악
    klen = len(katok)

    # 2단계 마지막 칸에 친구 넣기
    katok[klen-1] = friend

# 데이터 삽입 함수
def insert_data(position, friend): #3, 미나
    # 1단계 : 빈칸 추가
    katok.append(None)
    # 2단계 : 반복문 처리
    klen = len(katok)
    for i in range(klen-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None

    #3단계 : 미나를 넣기
    katok[position] = friend
        
# 데이터 삭제 함수
def delete_data(position) : #4
    # 1단계 : 그 위치 지우기
    katok[position] = None
    klen = len(katok)

    # 2단계 : 지운 위치 다음부터, 마지막 친구까지 한칸씩 앞으로
    for i in range(position+1, klen, 1):
        katok[i-1] = katok[i]
        katok[i] = None

    # 3단계 : 마지막 칸을 완전 제거
    del(katok[klen-1])





## 전역
katok = []

## 메인
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')

insert_data(3, '미나')
print(katok)

delete_data(4)
print(katok)

if __name__ == "__main__" :
    select = ''
    while (select != 4):     

        select = int(input("선택하세요 [추가(1), 삽입(2), 삭제(3), 종료(4)"))
        
        if (select == 1):
            data = input("추가할 데이터")
            add_data(data)
            print(katok)
            continue

        elif (select == 2):
            pos = int(input("추가할 위치"))
            data = input("삽입할 데이터")
            insert_data(pos, data)
            print(katok)
            continue

        elif (select ==3):
            pos = int(input("삭제할 데이터 위치"))
            del(katok[pos])
            print(katok)
            continue

        elif (select == 4):
            print(katok)
            print('프로그램 종료합니다~~')
            exit

        else :
            print("1~4까지만 고르세요~")
            continue