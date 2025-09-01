import logging
from datetime import datetime
logging.basicConfig(
    filename="watchtower.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def predict_and_log(model, input_data):
    prediction = model.predict(input_data)
    logging.info(f"Input: {input_data}, Prediction: {prediction}")
    return prediction
