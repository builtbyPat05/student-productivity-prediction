# Student Productivity Prediction

Machine-learning analysis of a synthetic dataset containing 5,000 student observations and 21 attributes. The project explores behavioral, academic, and wellness-related variables associated with a continuous productivity score.

## Results

- Compared closed-form `LinearRegression` with `SGDRegressor`.
- Used shuffled four-fold cross-validation with a fixed random seed.
- Achieved 4.51 mean cross-validation RMSE and 4.55 held-out RMSE.
- Evaluated L1, L2, Elastic Net, and polynomial configurations.
- Selected L1 regularization with `alpha=0.001` among the tested SGD settings.
- Analyzed relationships involving focus, study time, screen time, and burnout.

## Repository contents

- `student_productivity_prediction.ipynb`: complete analysis, model comparison, visualizations, cross-validation, regularization search, and saved outputs.
- `requirements.txt`: Python dependencies needed to run the notebook.
- `data/README.md`: dataset attribution and setup instructions.

## Dataset

The analysis uses the public [Student Performance Dataset](https://www.kaggle.com/datasets/amar5693/student-performance-dataset) on Kaggle. It contains synthetic records, so the findings represent modeled associations and should not be interpreted as causal conclusions about real students.

The notebook attempts to download the dataset with `kagglehub`. If automatic download is unavailable, download the CSV from Kaggle and place it inside the `data/` directory before running the notebook.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook student_productivity_prediction.ipynb
```

## Tools

Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, and Jupyter.
