{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "65b17ab9-c000-45dd-83dd-7da3ccfb7d77",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pickle\n",
    "import numpy as np\n",
    "\n",
    "# Load the saved logistic regression model\n",
    "with open('logistic_regression_model.pkl', 'rb') as file:\n",
    "    model = pickle.load(file)\n",
    "\n",
    "# App title\n",
    "st.title(\"Titanic Survival Prediction App\")\n",
    "\n",
    "# User input fields\n",
    "pclass = st.selectbox(\"Passenger Class\", [1, 2, 3])\n",
    "sex = st.radio(\"Sex\", ['Male', 'Female'])\n",
    "age = st.slider(\"Age\", 0, 100, 25)\n",
    "fare = st.number_input(\"Fare\", min_value=0.0, value=10.0)\n",
    "sibsp = st.number_input(\"Siblings/Spouses Aboard\", min_value=0, max_value=10, value=0)\n",
    "parch = st.number_input(\"Parents/Children Aboard\", min_value=0, max_value=10, value=0)\n",
    "embarked = st.selectbox(\"Port of Embarkation\", ['C', 'Q', 'S'])\n",
    "\n",
    "# Convert categorical inputs to numerical values\n",
    "sex = 1 if sex == 'Male' else 0\n",
    "embarked_Q = 1 if embarked == 'Q' else 0\n",
    "embarked_S = 1 if embarked == 'S' else 0\n",
    "\n",
    "# Prepare the feature array\n",
    "features = np.array([[pclass, sex, age, sibsp, parch, fare, embarked_Q, embarked_S]])\n",
    "\n",
    "# Predict when the button is clicked\n",
    "if st.button(\"Predict\"):\n",
    "    prediction = model.predict(features)[0]\n",
    "    if prediction == 1:\n",
    "        st.success(\"The passenger is likely to survive! 🛟\")\n",
    "    else:\n",
    "        st.error(\"The passenger is unlikely to survive. 💀\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
