class Worker:
    ROLE_PAY = {
        "kalfa": 50,
        "usta": 70,
        "cırak": 30,
        "stajer": 20
    }

    def __init__(self, id, name, role, hours_worked):
        self.id = id
        self.name = name
        self.role = role
        self.hours_worked = hours_worked
        self.salary = self.hours_worked * self.ROLE_PAY[self.role]

    def __str__(self):
        return f"{self.name} ({self.role}) - Çalışma Saatleri: {self.hours_worked}, Maaş: {self.salary} TL"

    def save_to_file(self, filename="calisanlar.txt"):
        with open(filename, "a") as file:
            file.write(f"{self.id},{self.name},{self.role},{self.hours_worked},{self.salary}\n")

def main():
    while True:
        worker_id = input("İşçi ID'sini girin (Çıkmak için 'q' tuşuna basın): ")
        if worker_id.lower() == 'q':
            break

        name = input("İşçinin adını girin: ")
        role = input("İşçinin rolünü girin (kalfa, usta, cırak, stajer): ").lower()
        hours_worked = int(input("İşçinin çalıştığı saat sayısını girin: "))

        worker = Worker(worker_id, name, role, hours_worked)
        print(worker)

        worker.save_to_file()

if __name__ == "__main__":
    main()


#Leans