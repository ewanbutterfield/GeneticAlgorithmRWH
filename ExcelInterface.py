import xlwings as xw


def get_satisfaction(x):
    wb = xw.Book('GeneticAlgorithmRWHCopy.xlsx')  # connect to a file that is open or in the current working directory

    sheet = wb.sheets['Parameters and Satisfaction']

    sheet.range('B2').value = x[0]

    if x[1]:
        roof_catchment_string = "Full Roof"
    else:
        roof_catchment_string = "Half Roof"
    sheet.range('C5').value = roof_catchment_string

    sheet.range('C6').value = x[2]

    if x[3] == 0:
        collection_tank_string = 400
    elif x[3] == 1:
        collection_tank_string = 1500
    elif x[3] == 2:
        collection_tank_string = 2500
    else:
        collection_tank_string = 10000

    sheet.range('C7').value = collection_tank_string
    sheet.range('C8').value = x[4]
    sheet.range('C9').value = x[5]
    sheet.range('C10').value = x[6]
    sheet.range('C12').value = x[7]

    if x[8] == 0:
        pump_string = "Pump A"
    elif x[8] == 1:
        pump_string = "Pump B"
    else:
        pump_string = "Pump C"

    sheet.range('C13').value = pump_string

    if x[9] == 0:
        filter_location_string = "Down"
    else:
        filter_location_string = "Up"

    sheet.range('C14').value = filter_location_string
    sheet.range('C16').value = x[10]
    sheet.range('C17').value = x[11]

    if x[12] == 0:
        UV_string = "36W"
    else:
        UV_string = "50W"

    sheet.range('C18').value = UV_string

    if x[13] == 0:
        chemical_type_string = "Chlorine"
    else:
        chemical_type_string = "Ozone"

    sheet.range('C19').value = chemical_type_string

    if x[14] == 0:
        power_system_choice_string = "Solar"
    else:
        power_system_choice_string = "Generator"

    sheet.range('C20').value = power_system_choice_string
    sheet.range('C21').value = x[15]

    if x[16] == 0:
        solar_panel_type_string = "HES-260"
    elif x[16] == 1:
        solar_panel_type_string = "SW-80"
    else:
        solar_panel_type_string = "HES-305P"

    sheet.range('C22').value = solar_panel_type_string
    sheet.range('C23').value = x[17]

    if (sheet.range('K5') != "Requirement not met" and sheet.range('K6') != "Requirement not met" and
            sheet.range('K7') != "Requirement not met" and sheet.range('K8') != "Requirement not met" and
            sheet.range('K9') != "Requirement not met" and sheet.range('K10') != "Requirement not met" and
            sheet.range('K11') != "Requirement not met" and isinstance(sheet.range('F14').value, float)):
        # print(sheet.range('F14').value)
        return sheet.range('F14').value
    else:
        return 0
