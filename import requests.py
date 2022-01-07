import requests
from tabulate import tabulate
from os import system

class Provinsi:
    total_data = 10

    def __init__(self, order="", page=1):
        self.order = order.upper()
        self.page = page
        self.url = "https://dev.farizdotid.com/api/daerahindonesia/provinsi"
        self.data = []

    def dataProvinsi(self):
        header = ['No', 'Nama Provinsi']
        response = requests.get(self.url).json()['provinsi']
        for i in range(len(response)):
            self.data.append([i+1, response[i]['nama']])
        start = self.total_data * (self.page -1)
        self.data = self.data[start:start+self.total_data]
        self.data = sorted(self.data, reverse=True if self.order == "DESC" else False)
        print(tabulate(self.data, header, tablefmt="github"))


def preview():
    system('cls')
    print("="*16)
    print("DATA PROVINSI")
    print("="*16)
    print()

    order = input("Urutan Data ASC/DESC : ")
    page = int(input("Halaman : "))
    data = Provinsi(order, page)

    data.dataProvinsi()

    again = input("Lihat Data Lainnya (Y/N) : ").upper()

    while again == "Y":
        preview()

preview()