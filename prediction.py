import pandas as pd
import pickle

def label_encoder(data):

  col_cat = data.select_dtypes(include=['object']).columns

  # Memuat encoder dari file pickle
  with open('./model/label_encoder.pkl', 'rb') as f:
      encoders = pickle.load(f)

  # Transform kolom kategori di data menggunakan encoder yang sudah dilatih
  for col in col_cat:
      data[col] = encoders[col].transform(data[col])

  return data

def predict_attrition(data):
  model = pickle.load(open('./model/best_model.pkl', 'rb'))
  y_pred = model.predict(data)

  if y_pred == 1:
    y_pred = 'Yes'
  else:
    y_pred = 'No'

  return y_pred

data = {
    "Age": [37],
    "BusinessTravel": ["Travel_Rarely"],
    "DailyRate": [1141],
    "Department": ["Research & Development"],
    "DistanceFromHome": [11],
    "Education": [1],
    "EducationField": ["Medical"],
    "EnvironmentSatisfaction": [0],
    "Gender": ["Female"],
    "HourlyRate": [61],
    "JobInvolvement": [0],
    "JobLevel": [2],
    "JobRole": ["Healthcare Representative"],
    "JobSatisfaction": [3],
    "MaritalStatus": ["Married"],
    "MonthlyIncome": [4777],
    "MonthlyRate": [14382],
    "NumCompaniesWorked": [5],
    "OverTime": ["No"],
    "PercentSalaryHike": [15],
    "PerformanceRating": [4],
    "RelationshipSatisfaction": [0],
    "StockOptionLevel": [0],
    "TotalWorkingYears": [15],
    "TrainingTimesLastYear": [2],
    "WorkLifeBalance": [0],
    "YearsAtCompany": [1],
    "YearsInCurrentRole": [0],
    "YearsSinceLastPromotion": [0],
    "YearsWithCurrManager": [0]
}

#jadikan new_data menjadi dataframe
new_data = pd.DataFrame(data)

df = label_encoder(new_data)
y_pred = predict_attrition(df)

print(f'===========================')
print(f'Prediksi Attrition: {y_pred}')
print(f'===========================')