import os
import glob
import pandas as pd

# 🔴 CSV 파일들이 들어있는 폴더 경로를 적어주세요.
# 예: 'C:/Users/Username/Desktop/부산데이터' 또는 './csv_folder'
target_folder = './경상남도_실거래가' 

# 1. 해당 폴더 안에서 '부산광역시_실거래가_*.csv' 패턴의 파일 경로를 다 찾습니다.
search_path = os.path.join(target_folder, '경상남도_실거래가_*.csv')
file_list = glob.glob(search_path)

print(f"폴더에서 찾은 파일 개수: {len(file_list)}개")

# 2. 파일들을 읽어서 리스트에 담기
df_list = []
for file in file_list:
    df = pd.read_csv(file, encoding='utf-8')
    df_list.append(df)

# 3. 데이터프레임 합치기 및 저장
if df_list:
    combined_df = pd.concat(df_list, ignore_index=True)
    
    # 결과 파일은 해당 폴더 안에 저장하거나 원하는 곳으로 지정 가능합니다.
    output_path = os.path.join(target_folder, '경상남도_실거래가(11~25).csv')
    combined_df.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"🎉 병합 완료! 생성된 파일: {output_path}")
else:
    print("❌ 지정한 폴더에서 CSV 파일을 찾지 못했습니다. 경로를 다시 확인해주세요.")