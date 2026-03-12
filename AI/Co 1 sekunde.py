import time


def wysylaj_komunikat():
    """Wysyła komunikat co 1 sekundę."""
    licznik = 1
    try:
        while True:
            # Komunikat, który chcesz wysłać
            komunikat = f"Komunikat nr {licznik}: Jestem wysyłany!"

            # W tym miejscu możesz umieścić kod, który faktycznie wysyła komunikat,
            # np. logowanie, wysyłanie przez socket, MQTT itp.
            print(komunikat)

            licznik += 1

            # Pauza na 1 sekundę
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nPrzerwanie programu przez użytkownika.")


if __name__ == "__main__":
    wysylaj_komunikat()