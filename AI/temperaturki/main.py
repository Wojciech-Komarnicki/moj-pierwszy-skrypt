from data_generator import SensorSimulator
from db_manager import DatabaseManager
from model import PredictiveModel

def main():
    simulator = SensorSimulator()
    df_sensors = simulator.generate_readings()

    db = DatabaseManager()
    db.save_to_db(df_sensors)

    df_train = db.load_from_db("SELECT * FROM sensor_readings")

    predictor = PredictiveModel()
    predictor.train(df_train)
    predictor.evaluate()
    predictor.save_model()

    test_result = predictor.predict_single(temp=88.5, vib=25.1, volt=228.0)
    print(f"Live Test Result: {test_result}")

if __name__ == "__main__":
    main()