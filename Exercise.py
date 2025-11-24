import math
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

class Exercise:
    # 파일 이름 정의
    file_name = 'notExercise.xlsx'

    # 파일을 읽어와서 DataFrame으로 변환
    def read_file_to_df(self):
        temp = pd.read_excel(self.file_name)
        df = pd.DataFrame(temp)
        return df

    # header 분리
    def sep_header(self, df):
        header = df.columns.tolist()
        start = header.index("운동을 할 충분한 시간이 없어서")
        end = header.index("운동을 싫어해서") + 1   # 끝 포함
        return header[start:end]

    # DataFrame 자르기 
    def slice_df(self, df, start, end):
        return df.iloc[start:end, 2:8]

    # pie 그래프 그리기
    def paint_pie(self, data, header):

        # Ex)  labels = ['남성', '여성']
        labels = data['분류'].tolist()

        num_charts = len(header)

        #전체 그래프 영역 만들기 (행/열 계산)
        rows = math.ceil(num_charts / 2)
        cols = 2

        plt.figure(figsize=(10, 5 * rows))

        for idx, col in enumerate(header):
            values = data[col].tolist()

            plt.subplot(rows, cols, idx+1)
            plt.pie(values, labels = labels, autopct='%.1f%%', startangle=90, counterclock = False)
            plt.title(f"{col}")
        plt.tight_layout()
        plt.show()


exercise = Exercise()

# 파일에서 읽은 데이터 DataFrame, header 분리
df = exercise.read_file_to_df()
header = exercise.sep_header(df)

# 성별, 연령병, 학력별, 소득별, 혼인상태별, 지역별로 DataFrame으로 분리
gender = exercise.slice_df(df, 1, 3)
age = exercise.slice_df(df, 3, 9)
education = exercise.slice_df(df, 9, 13)
in_come = exercise.slice_df(df, 13, 19)
marriage = exercise.slice_df(df, 19, 23)
location = exercise.slice_df(df, 23, 28)

# 각 df 값 pie graph로 그리기
exercise.paint_pie(gender, header)
exercise.paint_pie(age, header)
exercise.paint_pie(education, header)
exercise.paint_pie(in_come, header)
exercise.paint_pie(marriage, header)
exercise.paint_pie(location, header)