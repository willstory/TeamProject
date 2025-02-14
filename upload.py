import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
import os

# 모든 행과 열을 출력할 수 있도록 설정
pd.set_option("display.max_rows", None)  # 행 제한 해제
pd.set_option("display.max_columns", None)  # 열 제한 해제

# 파일 경로
file_path = "고1 변형문제 DB.xlsx"

# 엑셀 파일 읽기 (첫 번째 시트)
df = pd.read_excel(file_path, engine="openpyxl")

# 데이터 전체 출력
print(df.to_string())

load_dotenv()# 데이터베이스 연결 정보 (AWS RDS) 
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

# PostgreSQL 연결 엔진 생성 (MySQL 부분 제거)
engine = create_engine(f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

# 데이터 저장할 테이블명
table_name = "question_data"

def upload_excel_to_postgres(filepath, table_name, db_connection_string):
    try:
        # 파일 존재 여부 확인
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"파일을 찾을 수 없습니다: {filepath}")

        # 엑셀 파일 읽기
        df = pd.read_excel(filepath)
        
        # PostgreSQL 엔진 생성
        engine = create_engine(db_connection_string)
        
        # 데이터프레임을 PostgreSQL 테이블로 저장
        df.to_sql(
            name=table_name,
            con=engine,
            if_exists='replace',  # 'replace'는 테이블을 덮어씁니다. 'append'는 데이터를 추가합니다.
            index=False,
            schema='public'  # 스키마 이름을 필요에 따라 변경하세요
        )
        
        print(f"'{filepath}' 파일이 '{table_name}' 테이블에 성공적으로 업로드되었습니다.")
        return True

    except Exception as e:
        print(f"에러가 발생했습니다: {str(e)}")
        return False

# 사용 예시
if __name__ == "__main__":
    # AWS RDS PostgreSQL 연결 문자열
    db_connection_string = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    
    # 파일 경로와 테이블 이름 설정
    excel_filepath = "고1 변형문제 DB.xlsx"
    table_name = "question_data"
    
    # 업로드 실행
    upload_excel_to_postgres(excel_filepath, table_name, db_connection_string)