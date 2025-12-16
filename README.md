# Insurance Bought Prediction App

This project is a **Machine Learning–based web application** that predicts whether a person will buy insurance based on their **age**. The app is built using **Python**, **Streamlit**, and a trained **ML model** saved using `pickle`.

---

##  Features

* Simple and interactive **Streamlit UI**
* Takes **Age** as user input
* Predicts whether a person is **likely to buy insurance or not**
* Lightweight and easy to deploy

---

##  Technologies Used

* **Python**
* **Streamlit** (for web interface)
* **Scikit-learn** (for ML model)
* **Pickle** (for model serialization)

---

##  Project Structure

```
project-folder/
│-- myfile.py            # Streamlit application
│-- mymodel.pkl          # Trained ML model
│-- insurance_data.csv   # Dataset (optional / training data)
│-- model3.ipynb         # Jupyter notebook for model training
│-- README.md            # Project documentation
```

---

##  How to Run the Project

1. **Clone the repository**

```bash
git clone <repository-url>
cd project-folder
```

2. **Install required libraries**

```bash
pip install streamlit scikit-learn
```

3. **Run the Streamlit app**

```bash
streamlit run myfile.py
```

4. **Open the browser**

* The app will run on: `http://localhost:8501`

---

##  Model Logic

* The model uses **Age** as the input feature
* Output:

  * 0 → Person will not buy insurance
  * 1 → Person will buy insurance

##  App Preview

* Enter age in the input box
* Click Predict
* Result will be displayed instantly

## Use Case

* Beginner-level ML deployment project
* Academic mini project
* Resume / internship demonstration
