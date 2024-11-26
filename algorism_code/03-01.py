## 함수 선언부

## 전역 변수부
katok = ['다현','정연', '쯔위','사나','지효']


## 메인 코드부
print(katok)

## 데이터 추가(모모에게 카톡 1회)
# 1단계 : 빈 칸을 준비
katok.append(None)

# 2단계 : 마지막 칸에 추가
katok[5] = '모모'

print(katok)

## 데이터 삽입(미나가 40회 연속 카톡 == 미나를 3등)
# 1단계 : 빈 칸을 준비
katok.append(None)

# 2단계 : 모모부터 사나까지 한칸씩 뒤로 이동
katok[6] = katok[5] # 모모 이동
katok[5] = None
katok[5] = katok[4] # 지효 이동
katok[4] = None
katok[4] = katok[3] # 사나 이동
katok[3] = None

# 3단계 : 3등 자리에 미나 넣기
katok[3] = '미나'
print(katok)

## 데이터 삭제 (사나가 카톡 차단 == 4등인 친구 삭제)
# 1단계 : 4등 지우기
katok[4] = None

# 2단계 : 지효부터 마지막 친구까지 앞으로 한칸씩 이동
katok[4] = katok[5] #지효 이동
katok[5] = None
katok[5] = katok[6] #모모 이동
katok[6] = None

# 3단계 : 마지막 칸을 완전히 제거
del(katok[6])
print(katok)

