import csv
import matplotlib.pyplot as plt

filename = 'wheater.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)

plt.style.use("seaborn-v0_8")
# print(plt.style.available)
fig, ax = plt.subplots()
ax.plot(highs, c='red')
ax.set_title('Najwyższa temperatura', fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Temperatura(F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
