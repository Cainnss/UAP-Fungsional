import matplotlib.pyplot as plt

data = [
    ('Bus', 5, 200),
    ('Trem', 8, 150),
    ('Kereta', 12, 300),
    ('Minibus', 6, 180),
    ('Tram', 9, 220),
]

jenis_kendaraan = [item[0] for item in data]
penggunaan_energi = [item[1] for item in data]
biaya_operasional = [item[2] for item in data]

plt.scatter(jenis_kendaraan, penggunaan_energi, biaya_operasional)
plt.figure(figsize=(10,5))


plt.subplot(1, 3, 1)
plt.bar(jenis_kendaraan, penggunaan_energi)
plt.title('Jenis Kendaraan')
plt.xlabel('Jenis Kendaraan')
plt.ylabel('Penggunaan Energi')

plt.subplot(1, 3, 2)
plt.bar(jenis_kendaraan, biaya_operasional)
plt.title('Biaya Operasional')
plt.xlabel('Jenis Kendaraan')
plt.ylabel('Biaya Operasional')

plt.subplot(1, 3, 3)
plt.bar(jenis_kendaraan, biaya_operasional)
plt.title('Biaya Operasional')
plt.xlabel('Jenis Kendaraan')
plt.ylabel('Biaya Operasional')

plt.tight_layout()
plt.show()