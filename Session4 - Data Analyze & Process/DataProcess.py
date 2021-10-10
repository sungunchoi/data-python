#!/usr/bin/env python
# coding: utf-8

#### 1.라이브러리 선언

import pandas as pd
import numpy as np

#### 2.데이터 불러오기
csData = pd.read_csv("../dataset/customerdata.csv", encoding="ms949")
csData
csData.info()

### 리스트에서 데이터프레임 생성
productList = ["aProduct", "bProduct", "cProduct", "dProduct"]
priceList = [1000,2000,3000,4000]
zipList = zip(productList,priceList)
productInfoDf =  pd.DataFrame( zipList, columns=["productname","price"])
productInfoDf

### 딕셔너리에서 데이터프레임 생성
regionList = ["A01","A02","A03","A04","A05"]
yearweekList = list(range(201501,201506,1))
qtyList = list(range(100,600,100))
dictDf = { "REGIONID":regionList,
"YEARWEEK":yearweekList,
"QTY":qtyList}
dictDf = pd.DataFrame(dictDf)
dictDf

# 데이터프레임 정보 확인
productInfoDf.info()

# 데이터프레임의 컬럼 자료형 확인
productInfoDf.dtypes

### 1.원하는 행 조회하기

csDataEmi3 = csData.loc[(csData.EMI >= 3) & (csData.AVGPRICE > 3500)]
csData.loc[0:3]
csDataEmi3

# 행과 열의 개수를 바로 보여줌
csData.shape
csDataEmi3.shape

#대/소문자 변경
uiInputId = "a13566"
csData.loc[csData.CUSTID.str.upper() == uiInputId.upper()]



#데이터프레임 타입변환
#데이터프레임명['컬럼명'].astype(변경할 타입)
#데이터프레임명 = 데이터프레임명.astype({"컬럼명":변경할 타입})


customerData = csData
customerData.dtypes

#존재하지않는 컬럼 방식
customerData["EMI2"] = customerData["EMI"].astype(float)

#존재하는 컬럼 변경
customerData.EMI = customerData.EMI.astype(str)
customerData.dtypes
csDataTypeStr = customerData.astype({"CUSTID":str, 
                    "AVGPRICE":str,
                    "EMI":str,
                    "DEVICECOUNT":str,
                    "PRODUCTAGE":str,
                    "CUSTTYPE":str,
                    "EMI2":str})
csDataTypeStr.dtypes

#원하는 행 조회 (컬럼 내 다중 포함 값)
emiCondition = ["2","3"]

answer1 = customerData[customerData.EMI.isin(emiCondition)] #in
answer2 = customerData[~customerData.EMI.isin(emiCondition)] #not in

textDf = ["A"]
angryCustomer = pd.DataFrame( list( csData.CUSTID[0:3]),columns = ["CSID"])
angryList = list(angryCustomer.CSID)
csData.loc[~csData.CUSTID.isin(angryList)].shape

#원하는 행 조회 (인덱스)
specificIndex = [1,3]
answer1 = customerData.loc[ specificIndex ]
answer2 = customerData.loc[ 1:3 ] 
answer3 = customerData.loc[ : ] 
print(len(answer1))
print(len(answer2))
print(len(answer3))


### 2.원하는 컬럼 조회하기

import pandas as pd
# CSV 파일을 읽어 Data Frame 변수에 저장하기
customerData = pd.read_csv("../dataset/customerData.csv")
# 타겟 컬럼 정의 및 조회
targetColumns = ["CUSTID","AVGPRICE"]
customerDataC = customerData.loc[ : , targetColumns ]
# 데이터 VIEW
customerDataC.head(2)


customerDataC2 = customerDataC.copy()
customerData.iloc[: , 0:3] # 3은 포함되지않음


### 3. 인덱스 설정하기

#인덱스 사용시: 형상 변경이 유연함
#값 사용시: 가독성이 좋다.

#인덱스 초기화
emi3Data = customerData.loc[customerData.EMI == 3]
#(inplace=True)바꾼다면 즉시 변수에 반영한다
emi3DataReset = emi3Data.reset_index(drop=True,inplace=True)
#(drop=True) 기존 인덱스 드롭


#인덱스 설정하기
customerData.set_index(keys=["CUSID"])


### 4.데이터 조작하기

import numpy as np

### 데이터조작방법
#1. np.where 조작한다. (* 복잡한 로직에는 힘들어진다)
#2. 함수를 활용하여 조작한다 (*복잡한 로직에도 강하다!)
#3. loc 함수를 활용해서 조작한다. (* 가독성이 뛰어나난 속도가 떨어짐)
#4. map함수를 사용할수도 있다. (머신러닝에서 많이 사용된다!)

#### 1.
customerData["PRODUCTAGE_NEW"] =     np.where(customerData.PRODUCTAGE < 1, 1,             np.where( customerData.PRODUCTAGE < 2, 2, 3))

##### 2.
# 함수정의
# inputValue < 1: 1
# 1 <= inputValue < 2 : 2
# inputValue >= 2 3

def valueClustering(inValue):
    #inValue = 0.3
    outValue = inValue

    if inValue < 1:
        outValue = 1
    elif inValue < 2:
        outValue =2
    else:
        outValue = 3
    return outValue

customerData["PRODUCTAGE_NEW"] = customerData.PRODUCTAGE.apply(valueClustering)

#### 3.loc
customerData.loc[ customerData.PRODUCTAGE < 1, "PRODUCTAGE_NEW"] = 1
customerData.loc [ (customerData.PRODUCTAGE >= 1) &                 (customerData.PRODUCTAGE_NEW < 2),                 "PRODUCTAGE_NEW"] = 2
customerData.loc[(customerData.PRODUCTAGE >= 2), "PRODUCTAGE_NEW"] = 3

#### 4. map 함수~

featuresData =     pd.read_csv("../dataset/feature_regression_example.csv")
ynMap = {"Y":1, "N":0}
featuresData["HOLIDAY_NEW"] = featuresData.HOLIDAY.map(ynMap)
featuresData.head(2)


#### 5. 데이터 컬럼간 연산하기

customerData["NEW_COLUMN"] = customerData.CUSTID.str.lower()+"_"+customerData.EMI.astype(str)
customerData.head()

