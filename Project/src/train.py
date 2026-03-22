import joblib
from utils import load_data_in_batches
from model import get_vectorizer, get_model

file_path = "dataset_10M.parquet"

vectorizer = get_vectorizer()
model = get_model()

texts = []
labels = []

# 🔹 Load limited data (IMPORTANT)
for i, df in enumerate(load_data_in_batches(file_path)):
    texts.extend(df['DATA'].tolist())
    labels.extend(df['TOPIC'].tolist())

    if i == 5:  # Only ~5 batches (~5 lakh rows)
        break

print("Data loaded!")

# 🔹 Convert text → features
X = vectorizer.fit_transform(texts)

# 🔹 Train model
model.fit(X, labels)

# 🔹 Save model
joblib.dump(model, "../final_models/final_model.pkl")
joblib.dump(vectorizer, "../final_models/vectorizer.pkl")

print("Training complete & model saved!")