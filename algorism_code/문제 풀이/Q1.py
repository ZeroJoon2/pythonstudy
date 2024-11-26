ARRAY_LENGTH = 5  # 배열의 행과 열 크기(고정)

def replaceData(numData): # numData	2차원 정수 배열
    retData = [] # 조건에 따라서 전처리된 2차원 배열

    ###########   여기부터 코딩 (1) ---------------->
    for i in numData:
#        print(i)
        for num, j in enumerate(i):
              if j < 0:    
                j = 0
                i[num] = j
              elif j > 100:
                i[num] = j % 100
              else:
                pass
        retData.append(i)
#     print(f'여기 {i}')    
#     print(f'여기 {retData}')
     
        

    ###########   <-------------- 여기까지 코딩 (1)

    return retData


# 2x2 크기의 배열의 최대합을 구한다.
def getMaxSum(numData): # 요구 사항에 맞춰 처리된 2차원 정수 배열
    maxSum = 0 # 최대합

    ###########   여기부터 코딩 (2) ---------------->
    # 4개의 숫자가 하나의 박스
    minRange_r = 0
    MaxRange_r = 2
    minRange_c = 0
    MaxRange_c = 2
    
    #sum_list에 따로 보관하면 위치도 어느정도 추적할 수 있을듯
    sum_list = []

    # row를 기준으로 박스 상단의 위치가 3 초과되면 박스 못그림
    while minRange_r <= 3:
      minRange_c = 0
      MaxRange_c = 2

      # column을 기준으로 박스 왼쪽의 위치가 3 초과되면 박스 못그림
      while minRange_c <= 3:
        temp_list = []
        for i in range(minRange_r, MaxRange_r):
            # print(f'i ::: {i}')
            for j in range(minRange_c, MaxRange_c):
                  # print(f'numData[i][j] : {numData[i][j]}')
                  temp_list.append(numData[i][j])

        # print(temp_list)
        sum_list.append(sum(temp_list))
        # print("*************")
        # 박스 우측으로 하나씩 옮기기
        minRange_c += 1
        MaxRange_c += 1
      # 박스 하단으로 하나씩 옮기기
      minRange_r += 1
      MaxRange_r += 1
    
    # print(f'박스들의 합 : {sum_list}')
    # print(f'박스들 중 최고값 : {max(sum_list)}')

    # 정답을 위한 변수에 할당해줌
    maxSum = max(sum_list)
    ###########   <-------------- 여기까지 코딩 (2)

    return maxSum

## 전역 변수 선언 부분
numData =[] # 5x5 배열
ARRAY_LENGTH = 5 # 배열의 행과 열 크기(고정)

def main() :
        global numData

        loadData() # 2차원 배열 읽어오기

        ## 원본 출력
        print(' ----- 초기 배열 -----')
        printData()

        # 1. 데이터 치환 작업
        numData = replaceData(numData)
        print(' ----- 치환 후 배열 -----')
        printData()

        # 2. 최대 합 구하기.(2x2 크기)
        maxSum = getMaxSum(numData)
        print('최대 영역의 합: %d' % maxSum)

       
## 함수 선언 부분
def  loadData() : # 데이터 불러오기
    global numData

    ###########
    # 제공 데이터 세트 1 
    # 5x5 숫자 배열. 
    ###########
    numData = \
    [
        [ 5, 7, -5, 100, 73 ],
        [ 35, 23, 4, 190, 33 ],
        [ 49, 85, 662, 39, 81 ],
        [ 124, -59, 86, 46, 52 ],
        [ 27, 7, 8, 33, -56 ] 
    ]
    
    

def printData() :
        for i in range(0, ARRAY_LENGTH) :
                for k in range(0, ARRAY_LENGTH) :
                        try :
                                print("%5d" % numData[i][k], end='')
                        except :
                                pass
                print()
        print('--------------------------------------')

## 메인 함수 호출 ##
if __name__ == "__main__" :
    main()