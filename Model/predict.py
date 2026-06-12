import pickle
import pandas as pd

with open ('Model/model.pkl','rb') as f:
    model = pickle.load(f)

class_labels= model.classes_.tolist()

def predict_output(user_input:dict):
    df=pd.DataFrame([user_input])
    predicted_class = model.predict(df)[0]
    probabilities = model.predict_proba(df)[0]
    confidence=max(probabilities)
   #create mapping :{class_name:probability}
    class_probs= dict(zip(class_labels, map(lambda p:round(p,4), probabilities  )))
    return {
        'predicted_class': predicted_class,
        'confidence': round(confidence,4),
        'class_probabilities': class_probs
    }

