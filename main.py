from data_manager import DataManager
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

dm = DataManager()
sheet_data = dm.get_data()

# Updates the dictionary element for the appropriate IATA Code corresponding to the city column
# for elem in sheet_data:
    # dm.update_iata_code(elem)
