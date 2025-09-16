import konversi
try:
    suhu_celcius = float(input("Masukkan suhu Celcius: "))
    suhu_fahrenheit = konversi.c_to_f(suhu_celcius)
    print(f"Suhu dalam Fahrenheit= {suhu_fahrenheit}")

except ValueError:
    print("Input tidak valid. Harap masukkan angka.")