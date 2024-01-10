rain_data = open(r"C:\Users\tooco\Downloads\UofA CS 2027\CMPUT-175\lab1\rainfall_d1209bd237d8c429af7a133bbefa407e.txt", "r")
rain_sol = open(r"C:\Users\tooco\Downloads\UofA CS 2027\CMPUT-175\lab1\rainfallfmt.txt", "w")
data_list = []
for i in rain_data:
    data = i.split()
    data_list.append(data)
data_list.sort(key=lambda x: x[1])
dict_organized = {50: {}, 60: {}, 70: {}, 80: {}, 90: {}}
for i in data_list:
    for j in dict_organized:
        if j < float(i[1]) < j + 10:
            dict_organized[j][i[0]] = i[1]
for i in dict_organized:
    rain_sol.write(f"[{i}-{i + 10} mm)\n")
    for j in dict_organized[i]:
        rain_sol.write(f"{j.upper(): ^25}{round(float(dict_organized[i][j]), 1): >5}\n")
rain_data.close()
rain_sol.close()