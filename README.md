# 📘 프로젝트 개요

이 프로젝트는 “운동을 하지 않는 이유” 데이터를 중심으로, 성별, 연령, 학력, 소득, 혼인 상태, 지역별 인구집단이 운동을 하지 않는 주요 원인을 파이 그래프로 시각화한 분석 프로젝트입니다.
Excel 데이터를 기반으로 각 그룹의 응답 분포를 한눈에 비교할 수 있도록 시각화 환경을 설계했습니다.

---

# 📊 분석 결과 (파이 그래프)

아래 이미지는 실제 코드 실행 결과로, 각 인구집단이 운동을 하지 않는 이유의 상대적 비율을 파이 그래프로 보여줍니다.

## 성별

<img width="848" height="763" alt="Image" src="https://github.com/user-attachments/assets/b96f08c6-1782-41a9-837b-befa782d620c" />

## 연령별

<img width="791" height="745" alt="Image" src="https://github.com/user-attachments/assets/c6bc8a1a-c621-4cf7-ba42-5a8d27bce963" />

## 학력별

<img width="806" height="699" alt="Image" src="https://github.com/user-attachments/assets/f2941451-f293-4a57-bd22-1397894aee50" />

## 소득별

<img width="1017" height="713" alt="Image" src="https://github.com/user-attachments/assets/8b119dd5-94be-4deb-97e9-81f78390be11" />

## 혼인 상태별

<img width="891" height="741" alt="Image" src="https://github.com/user-attachments/assets/c0a7e18a-f1e4-43f4-84da-dd181e03fd19" />

## 지역대분류

<img width="893" height="797" alt="Image" src="https://github.com/user-attachments/assets/6d1d4a83-e0ff-49e9-a8a4-32e7423e122a" />

# 🔧 주요 기능 및 기술적 설계 포인트

## 1️⃣ 엑셀 데이터 분석 및 필요 데이터 처리

<img width="1150" height="133" alt="Image" src="https://github.com/user-attachments/assets/c395fd2e-a64a-4170-9eda-e489978c20c9" />

<p align="center">📄 Excel 데이터 일부 발췌</p>

설문 문항이 여러 컬럼에 걸쳐있기 때문에, "운동을 할 충분한 시간이 없어서"부터 "운동을 싫어해서"까지의 문항 범위를 인덱싱하여 추출했습니다.

## 2️⃣ 카테고리(성별/연령/학력/소득/혼인/지역)별 데이터 슬라이싱

`slice_df(df, start, end)`함수를 통해 필요한 데이터를 분류하고, 파이 그래프에 필요한 데이터만 추출하도록 구현했습니다.

```python
    start = temp_header.index("운동을 할 충분한 시간이 없어서")
    end = temp_header.index("운동을 싫어해서") + 1
```

## 3️⃣ 파이 그래프 렌더링

문항 수에 맞춰 subplot 개수를 계산하여 그래프를 배치하고 어떤 그룹이든 paint_pie(data, header) 함수에 인자를 전달하면 파이 그래프를 생성하도록 구현했습니다.

```python
    plt.subplot(rows, cols, idx+1)
    plt.pie(values, labels = labels, autopct='%.1f%%', startangle=90, counterclock = False)
    plt.title(f"{col}")
```

## 4️⃣ 코드 실행 예시

<img width="1107" height="343" alt="Image" src="https://github.com/user-attachments/assets/8136a59a-26e6-4737-bec4-ea7fbe35bca5" />

## 5️⃣ 한글 폰트와 음수 처리 설정

macOS에서 한글이 깨지는 이슈를 해결하기 위해 `AppleGothic`를 적용하고, 음수 기호 깨짐 방지를 위해 `unicode_minus=False`를 적용했습니다.

# 📁 기술 스택

- Python
- pandas
- matplotlib
- Excel 기반 데이터 분석
