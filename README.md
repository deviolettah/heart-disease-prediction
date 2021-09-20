
<h3 align="center">Heart Disease Prediction Using ANN</h3>


---


## 📝 Table of Contents

- [About](#about)
- [Dataset](#dataset)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)


## 🧐 About <a name = "about"></a>

Neural Network algorithm can be used to calculate and predict the possibility of heart disease in a person. The hope is that heart disease can be treated early so that it can reduce the death rate. The results of this study are in the form of knowledge in predicting a person's risk of heart disease by implementing the Artificial Neural Network (ANN) algorithm on the software. From the results of the application of the algorithm, an accuracy rate of 85.86% is obtained in determining more accurate results in accordance with actual data for a reference for predicting a person's risk of heart disease.

## 🏁 Dataset <a name = "dataset"></a>

Heart disease dataset from UCI with a sample of 303 data. 
There are 14 attributes in the dataset, including:
- Age is age in years.
- Sex is gender
- Cp (Chest Pain) is chest pain experienced (1= typical angina, chest pain typical for angina pectoris: feeling of pressure/heaviness in the back of the mid-chest bone, persistent >20 minutes, accompanied by accompanying complaints, 2 = atypical angina, chest pain that is not typical of angina pectoris: pain in the area of ​​transmission of typical angina, indigestion, shortness of breath, 3 = non-anginal pain, chest pain that is not angina or not caused by heart disease, 4 = asymptomatic, does not feel any complaints)
- Trestbps is blood pressure at rest (mm Hg)
- Chol is cholesterol in mg/dl.
- Fbs is blood sugar, if it is more than 120 mg/dl then it is 1 and if it is less than 120 mg/dl then it is 0.
- Restecg is an electrocardiogram value that measures the electrical activity of the heart at rest (0 = normal, 1 = abnormal ST-T wave, 2 = indicates the possibility of left ventricular hypertrophy)
- Thalach is the maximum heart rate.
- Exang is chest pain during exercise (1 = yes; 0 = no)
- Oldpeak is a decrease in ST during exercise.
- Slope is the peak slope of the ST Segment during exercise (Value 1: slope up, Value 2: flat, Value 3: slope down).
- Ca is the number of major vessels.
- Thal is a blood disorder or thalassemia (3 = Normal, 6 = Permanent Disability, 7 = Reversible Disability).
- The target is heart disease. A value of 0 means no risk, while a value of 1 is risky. 

## 🎈 Usage <a name="usage"></a>

1. Clone this repo
2. Run the 
```
gui.py
```
3. Complete the form
4. Press the Predict button and the application will show you are at risk of heart disease or not

## 🚀 Deployment <a name = "deployment"></a>

1. Data Cleaning is removing unnecessary data and creating noise, such as data that has an empty value (missing value). From the 303 data, there are 6 records that have missing values. Therefore, the total data selected are 297 records with attribute
2. Data Transformation is the process of transforming data into a format to be processed and ready to be mined. Where the target label or attribute that originally used a 0-4 scale was changed to 0-1.
3. Do experiments to build machine learning model using Artificial Neural Network
4. Prediction model results will be saved and implemented into desktop-based applications (using PyQt) that can then be used to predict whether someone at risk of heart disease or not

## ⛏️ Built Using <a name = "built_using"></a>

- Python - Programming Language
- TensorFlow - Machine Learning Framework
- PyQt - Python GUI

## ✍️ Authors <a name = "authors"></a>

- [@deviolettah](https://github.com/deviolettah) 
- [@raindyhardian](https://github.com/RaindyHardian)

