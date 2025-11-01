# 🌾 AI Crop Yield Prediction Model  

## 📘 Project Overview  
This project predicts **crop yield** based on key climatic and agricultural factors such as rainfall, fertilizer use, pesticide application, and seasonal variations.  
It leverages **Machine Learning (XGBoost)** for predictive modeling and is deployed using a **Flask web application** for real-time yield prediction.  

> 🎯 **Goal:** Help farmers, policymakers, and agronomists make data-driven decisions to improve productivity and optimize resource use.

---

## ⚙️ Key Features  
- 📊 **Exploratory Data Analysis (EDA):**  
  - Correlation heatmaps  
  - Distribution and trend visualizations  
  - Feature importance insights  

- 🧠 **Model Building:**  
  - XGBoost Regressor for robust yield prediction  
  - Label Encoding for categorical features  
  - Scaler for numerical normalization  

- 💡 **Model Evaluation:**  
  - **R² Score:** `0.9997`  
  - **MAE:** `5.9464`  
  - **RMSE:** `15.3940`  

- 🌐 **Flask Deployment:**  
  - User-friendly web interface for input  
  - Real-time yield prediction output  
  - Hosted locally (ready for cloud deployment)

---

## 🧰 Tech Stack  
| Category | Tools/Technologies |
|-----------|--------------------|
| **Language** | Python |
| **Libraries** | Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib, Seaborn |
| **Framework** | Flask |
| **Version Control** | Git, GitHub |
| **IDE** | PyCharm |
| **Visualization** | Heatmaps, Feature Importance, Correlation Matrix |

---


AI-Crop-Yield-Prediction-Model/
│
├── app.py # Flask web app
├── model.pkl # Trained XGBoost model
├── templates/ # HTML templates for Flask
│ ├── index.html
│ └── result.html
├── static/ # CSS, JS, images (if any)
├── Data/ # (Ignored in repo - large datasets excluded)
├── EDA_notebook.ipynb # Jupyter notebook with full EDA & modeling
├── requirements.txt # Dependencies
├── .gitignore
└── README.md


---

## 🚀 How to Run Locally  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/somay1/AI-Crop-Yield-Prediction-Model.git
   cd AI-Crop-Yield-Prediction-Model
2.**Create and activate virtual environment**
  python -m venv venv
  venv\Scripts\activate
3. **Install dependencies**
  pip install -r requirements.txt
4.**python app.py**


| Metric   | Score       |
| -------- | ----------- |
| **R²**   | **0.9997**  |
| **MAE**  | **5.9464**  |
| **RMSE** | **15.3940** |

🔮 Future Enhancements


Add crop recommendation system using classification models


Integrate real-time weather APIs for dynamic prediction


Host on Render / Hugging Face Spaces / AWS EC2


Add dashboard for data visualization using Plotly or Dash



🖼️ Sample Visualizations

(Optional: Add screenshots here)


Heatmap of feature correlations


Feature importance chart


Flask web app interface




👨‍💻 Author
Somay Attri
Data Science & Machine Learning Enthusiast
📍 Delhi, India
 https://github.com/somay1 

💬 Feedback & Support
If you find this project helpful, consider giving it a ⭐ on GitHub!
Suggestions and contributions are always welcome.


---





    

## 🗂️ Project Structure
