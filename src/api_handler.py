import requests

def scrape_slot_data():
    try:
        # URL website slot Spaceman
        url = "https://istanacasino.rest/welcome/slot-games"

        # Mengirim permintaan HTTP GET ke website
        response = requests.get(url)

        # Memeriksa apakah permintaan berhasil (kode status 200)
        if response.status_code == 200:
            # Mengambil data dari respons JSON
            slot_data = response.json()
            return slot_data
        else:
            print("Failed to retrieve slot data. Status code:", response.status_code)
            return None
    except Exception as e:
        print("An error occurred while scraping slot data:", str(e))
        return None

# Contoh penggunaan
slot_data = scrape_slot_data()
if slot_data:
    print("Slot data:", slot_data)
else:
    print("Failed to retrieve slot data.")