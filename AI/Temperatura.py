import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# ==========================================
# 1. SYMULACJA DANYCH Z CZUJNIKÓW (Data Engineering)
# ==========================================
print("🔄 Krok 1: Generowanie syntetycznych danych z czujników...")

# Generujemy 1000 odczytów
n_samples = 1000
np.random.seed(42) # Żeby wyniki były powtarzalne

# Symulujemy dane:
# - Temperatura (normalna ok. 60-80 stopni, przy awarii rośnie)
# - Wibracje (normalne ok. 10-20 Hz, przy awarii rosną)
data = {
    'sensor_id': np.random.randint(1, 5, n_samples), # 4 różne silniki
    'temperature': np.random.normal(70, 10, n_samples),
    'vibration': np.random.normal(15, 5, n_samples),
    'voltage': np.random.normal(230, 5, n_samples)
}

df = pd.DataFrame(data)

# Logika awarii (Labeling):
# Jeśli temp > 90 ORAZ wibracje > 25 -> Oznaczamy jako "Awaria" (1), w przeciwnym razie "OK" (0)
df['failure_status'] = np.where((df['temperature'] > 85) & (df['vibration'] > 22), 1, 0)

print(f"✅ Wygenerowano {n_samples} rekordów.")
print(df.head()) # Podgląd danych

# ==========================================
# 2. ETL DO BAZY SQL (Database Management)
# ==========================================
print("\n🔄 Krok 2: Ładowanie danych do bazy SQL...")

# Tworzymy lokalną bazę SQLite (plik 'factory_data.db' pojawi się w folderze projektu)
engine = create_engine('sqlite:///factory_data.db')

# Wrzucamy DataFrame do tabeli SQL o nazwie 'sensor_readings'
df.to_sql('sensor_readings', con=engine, index=False, if_exists='replace')

print("✅ Dane zapisane w bazie SQL (SQLite).")

# ==========================================
# 3. POBRANIE DANYCH I TRENING AI (Machine Learning)
# ==========================================
print("\n🔄 Krok 3: Pobieranie danych z SQL i trening modelu...")

# Udajemy, że jesteśmy analitykiem - pobieramy dane z bazy zapytaniem SQL
query = "SELECT temperature, vibration, voltage, failure_status FROM sensor_readings"
df_ml = pd.read_sql(query, con=engine)

# Podział na cechy (X) i cel (y)
X = df_ml[['temperature', 'vibration', 'voltage']]
y = df_ml['failure_status']

# Podział na zbiór treningowy i testowy (80% trening, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Wybór modelu: Random Forest (Las Losowy) - świetny do danych inżynierskich
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predykcja na zbiorze testowym
predictions = model.predict(X_test)

# ==========================================
# 4. WYNIKI I EVALUACJA
# ==========================================
print("\n📊 WYNIKI MODELU:")
print("Confusion Matrix (Macierz Pomyłek):")
print(confusion_matrix(y_test, predictions))
print("\nRaport Klasyfikacji:")
print(classification_report(y_test, predictions))

# Symulacja sprawdzenia nowego odczytu
new_reading = [[92.5, 26.1, 229.0]] # Wysoka temperatura i wibracje
prediction = model.predict(new_reading)
print(f"\n🔍 Test dla nowego odczytu {new_reading}:")
print("🚨 PRZEWIDYWANA AWARIA!" if prediction[0] == 1 else "✅ STAN OK")