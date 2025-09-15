# Loan Status Prediction with Perceptron Neural Network

This project demonstrates how to preprocess loan data, encode features, and train a simple perceptron neural network using PyTorch to predict loan status. The workflow includes data loading, preprocessing, model definition, training, evaluation, and visualization.

---

## Project Structure

- `loan_data.csv` — Input dataset containing loan features and the `loan_status` target.
- `neural_network/neural_network_scikitlearn.ipynb` — Main Jupyter notebook with all code and analysis.

---

## Requirements

- Ubuntu 24.04.2 LTS (dev container)
- Python 3.8+
- torch
- pandas
- matplotlib
- seaborn
- scikit-learn

Install dependencies with:
```bash
pip install torch pandas matplotlib seaborn scikit-learn
```

---

## Workflow

### 1. Data Loading & Exploration

- Load the dataset using pandas.
- Visualize feature distributions and class balance with matplotlib and seaborn.

### 2. Feature Preparation

- Separate features (`X`) and target (`y`).
- Identify numeric and categorical columns.
- Preprocess:
  - Numeric: Impute missing values, scale features.
  - Categorical: Impute missing values, one-hot encode.

### 3. Train/Test Split

- Split the data into training and testing sets using `train_test_split`.

### 4. Target Encoding

- Encode the `loan_status` target as integers using `LabelEncoder`.

### 5. Tensor Conversion

- Convert features and labels to PyTorch tensors for model training.

### 6. Model Definition

- Define a simple Perceptron class using PyTorch’s `nn.Module`.
- Implement a custom Heaviside step function for binary classification.

### 7. Training

- Train the perceptron using a custom loss function and manual parameter updates.
- Print training progress, weights, bias, and loss per epoch.

### 8. Evaluation

- Predict on the test set.
- Calculate and print accuracy.

### 9. Visualization

- Plot the test set with predicted classes for visual inspection.

---

## Usage

1. Place `loan_data.csv` in the `neural_network` directory.
2. Open and run `neural_network_scikitlearn.ipynb` in Jupyter.
3. Follow the notebook cells sequentially.

---

## Notes

- The perceptron model is suitable for binary classification.
- Ensure your dataset’s `loan_status` column contains only two classes.
- For more complex tasks, consider using deeper neural networks or other models.

---

## References

- [PyTorch Documentation](https://pytorch.org/docs/stable/index.html)
- [scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
- [pandas Documentation](https://pandas.pydata.org/docs/)
- [matplotlib Documentation](https://matplotlib.org/stable/users/index.html)
- [seaborn Documentation](https://seaborn.pydata.org/)

---