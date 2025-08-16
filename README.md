# Linear Regression: Cost Function & Gradient Descent  

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)  
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter&logoColor=white)  
![NumPy](https://img.shields.io/badge/NumPy-1.x-013243?logo=numpy&logoColor=white)  
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-yellow?logo=plotly&logoColor=white)  

## 🎯 Project Motivation  
This notebook was created as part of my journey to learn **machine learning fundamentals**. Instead of using libraries that hide the details, this project builds **linear regression from scratch** to understand the **math and logic** behind:  
- How predictions are made  
- How errors are measured (cost function)  
- How the model learns (gradient descent)  

The goal is to develop a strong intuition for the core concepts before moving on to more advanced algorithms and libraries.  

## 📌 Project Goals
- Implement the hypothesis function $f_{w,b} = wx + b$  
- Understand and compute the **cost function** $J(w,b)$  
- Apply **Gradient Descent** to optimize parameters $w$ and $b$  
- Visualize results on a housing price dataset  

## 📊 Dataset
For simplicity, we use a small dataset with **10 values** and **1 feature** (`size` of the house). The task is to predict the **house price**.  

## 🛠️ Technologies Used
- Python  
- NumPy  
- Matplotlib  
- Jupyter Notebook  

## 📂 File Structure
- `LinearRegression_Cost_GradientDescent.ipynb` → The main notebook with explanations, equations, and code.
- `Helpers.py` → Some helper functions to visualize the graphics

## 🚀 How to Run
1. Clone this repository:  
   ```bash
   git clone https://github.com/ahhmettulku/Simple-Linear-Regression-and-Gradient-Descent.git
   cd Simple-Linear-Regression-and-Gradient-Descent
   ```
2. Install dependencies:  
   ```bash
   pip install numpy matplotlib notebook
   ```
3. Run the Jupyter Notebook:  
   ```bash
   jupyter notebook LinearRegression_Cost_GradientDescent.ipynb
   ```

## 📖 Learning Outcomes
- Understand the relationship between **model parameters, cost, and optimization**.  
- Learn how **gradient descent updates weights** step by step.  
- Build intuition on how machine learning models “learn” from data.  

## 📝 Example Visualization
The notebook shows how the fitted line improves with each iteration of **Gradient Descent**:

<img width="1211" height="411" alt="image" src="https://github.com/user-attachments/assets/11fe372e-e59c-4181-a69f-6869a36a89f1" />
 

## 🔮 Next Steps
If you’d like to continue learning, here are some natural next steps:
1. **Multiple Features**: Extend the model to predict house prices using more than one feature (e.g., size + number of rooms).  
2. **Feature Scaling**: Apply normalization to improve gradient descent convergence.  
3. **Logistic Regression**: Learn classification with logistic regression and the sigmoid function.  
4. **Regularization**: Explore L1 (Lasso) and L2 (Ridge) to prevent overfitting.  
5. **Scikit-Learn Implementation**: Compare your manual implementation with scikit-learn’s `LinearRegression`.  

## 📚 References
- [Andrew Ng’s Machine Learning Specialization (Coursera)](https://www.coursera.org/specializations/machine-learning-introduction)  
- [Scikit-Learn: Linear Regression Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)  
- [NumPy Documentation](https://numpy.org/doc/)  
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)  

## 📜 License
This project is licensed under the **MIT License** – you are free to use, modify, and distribute this code for both personal and commercial purposes.  
See the [LICENSE](LICENSE) file for details.  
