# Classification Assignment: Machine Learning

## Classification Assignment OrbitShift
**Overview:**

Objective: Perform multi-class classification on a given dataset using the "sentence-transformers/all-MiniLM-L6-v2" model from Hugging Face.
Tools and Libraries Used: Python, Jupyter, Sentence Transformers, Logistic Regression, Pickle.

Steps:
-Data Cleaning:
Removed unnecessary strings from the dataset's "title" column to ensure high-quality training data.
Retained records with cleaned titles to avoid missing data during training.

-Handling Imbalanced Data:
Identified class imbalance with some classes having more than 450 records and others less than 100.
Applied oversampling to classes with fewer than 300 records to balance the dataset.

-Data Splitting:
Split the dataset into training, validation, and test sets for model evaluation.

-Text Processing:
Used the tokenizer to process textual data and prepare it for model training.

-Model Training:
Utilized logistic regression for the multi-class classification task.

-Model Deployment:
Incorporated Pickle for serialization, enabling deployment on FastAPI or other platforms.

-Included an example to showcase the functionality and effectiveness of the code.
