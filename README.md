## 설정
>pip install oracledb sqlalchemy python-dotenv


database.py 11번째 줄 instantclient 경로 설정


-DB 연결 테스트-
>python test.py

-DB 테이블 생성(USERS,FOLDERS, FILES, LOGS)-
>python create_tables.py

--------------------------

## 테이블 관계

<img width="691" height="664" alt="image" src="https://github.com/user-attachments/assets/159d5ff1-2add-4d69-981b-078b1cf56312" />






--------------------------

## 각 테이블 컬럼 타입 & 의미

*USERS TABLE*
| 컬럼명              | 타입           | 의미 / 설명                                     
| ------------------ | ------------- | ------------------------------------------- 
| **USER_ID**        | NUMBER (PK)   | 사용자 고유 식별번호    
| **USER_LOGIN_ID**  | VARCHAR2(50)  | 로그인용 사용자 ID      
| **USER_PASSWORD**  | VARCHAR2(200) | 사용자 비밀번호               
| **EMAIL**          | VARCHAR2(100) | API 접근 토큰 / 인증키로 활용 가능             
| **CREATED_AT**     | DATE          | 계정 생성 시각                  
| **ACCESS_KEY**     | VARCHAR2(100) | API 접근 토큰 / 인증키로 활용 가능
| **LAST_WORK**      | DATE          | 마지막 작업

*FILES TABLE*
| 컬럼명                     | 타입           | 의미 / 설명                                          
| ------------------------- | ------------- | ------------------------------------------------ 
| **FILE_ID**               | NUMBER (PK)   | 업로드된 파일의 고유 ID                   
| **USER_ID**               | NUMBER (FK)   | 파일을 업로드한 사용자 ID
| **FOLDER_ID**             | NUMBER (FK)   | 폴더 ID           
| **FILE_NAME**             | VARCHAR2(200) | 업로드된 파일 이름                    
| **FILE_TYPE**             | VARCHAR2(50)  | 파일 확장자 또는 유형 
| **FILE_PATH**             | VARCHAR2(300) | 파일이 저장된 서버 내 절대 또는 상대 경로  
| **IS_TRANSFORM**          | NUMBER(1)     | 변환(OCR 등) 완료 여부 
| **TRANSFORM_TXT_PATH**    | VARCHAR2(300) | 변환 텍스트 주소
| **IS_CLASSIFICATION**     | NUMBER(1)     | AI 분류 완료 여부                     
| **CATEGORY**              | VARCHAR2(200) | 카테고리    
| **UPLOADED_AT**           | DATE          | 업로드 시각      

*LOGS TABLE*
| 컬럼명           | 타입            | 의미 / 설명                                              
| --------------- | -------------- | ---------------------------------------------------- 
| **LOG_ID**      | NUMBER (PK)    | 로그 고유 ID                         
| **USER_ID**     | NUMBER (FK)    | 업로더                   
| **LOG_TIME**    | DATE           | 로그 기록 시각                         
| **LOG_CONTENT** | VARCHAR2(1000) | 로그 내용 

*FOLDERS TABLE*
| 컬럼명                  | 타입          | 의미 / 설명                                  
| -----------------------| -------------| ----------------------------------------------
| **FOLDER_ID            | NUMBER (PK)  | 폴더 고유 ID
| **USER_ID**	         | NUMBER (FK)  | 사용자 ID
| **FOLDER_NAME**	     | VARCHAR2     | 폴더 이름
| **CATEGORY_LIST**	     | VARCHAR2     | 카테고리
| **CONNECTED_DIRECTORY**| VARCHAR2     | 연결된 디렉토리
| **CATEGORY_CHANGE**	 | VARCHAR2     | 분류 후 변경된 카테고리
| **LAST_WORK** 	     | DATE         | 최근 작업 시간/ 최근 폴더 내림차순
















