import joblib
import pandas as pd  # Dodaliśmy import pandas
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from config import RANDOM_STATE


class PredictiveModel:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=RANDOM_STATE)
        self.X_test = None
        self.y_test = None

    def train(self, df):
        X = df[['temperature', 'vibration', 'voltage']]
        y = df['failure_label']

        X_train, self.X_test, y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, random_state=RANDOM_STATE
        )

        self.model.fit(X_train, y_train)

    def evaluate(self):
        predictions = self.model.predict(self.X_test)
        # Dodano zero_division=0, żeby wyciszyć ostrzeżenie o dzieleniu przez zero
        print(classification_report(self.y_test, predictions, zero_division=0))
        print(confusion_matrix(self.y_test, predictions))

    def predict_single(self, temp, vib, volt):
        # POPRAWKA: Tworzymy DataFrame z nazwami kolumn, tak jak przy treningu
        data = pd.DataFrame([[temp, vib, volt]], columns=['temperature', 'vibration', 'voltage'])

        result = self.model.predict(data)[0]
        return "AWARIA 🚨" if result == 1 else "OK 🟢"

    def save_model(self, filename='maintenance_model.pkl'):
        joblib.dump(self.model, filename)