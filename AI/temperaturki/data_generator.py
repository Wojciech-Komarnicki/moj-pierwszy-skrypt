import pandas as pd
import numpy as np
from config import NUM_SAMPLES, RANDOM_STATE, TEMP_THRESHOLD, VIBRATION_THRESHOLD


class SensorSimulator:
    def __init__(self, n_samples=NUM_SAMPLES):
        self.n_samples = n_samples
        np.random.seed(RANDOM_STATE)

    def generate_readings(self):
        data = {
            'sensor_id': np.random.randint(1, 10, self.n_samples),
            'temperature': np.random.normal(70, 10, self.n_samples),
            'vibration': np.random.normal(15, 5, self.n_samples),
            'voltage': np.random.normal(230, 5, self.n_samples)
        }

        df = pd.DataFrame(data)

        df['failure_label'] = np.where(
            (df['temperature'] > TEMP_THRESHOLD) &
            (df['vibration'] > VIBRATION_THRESHOLD),
            1, 0
        )

        return df