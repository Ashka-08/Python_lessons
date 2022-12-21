import view
import model

def button_click():
    data_base = model.read_database()
    new_data = model.exoprt_json()
    model.add_to_database(data_base, new_data)
