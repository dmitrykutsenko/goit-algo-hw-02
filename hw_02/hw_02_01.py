from queue import Queue
import random
import time

class Request:
    _id = 1
    def __init__(self):
        self.id = Request._id
        Request._id += 1
        self.data = f"Data for request {self.id}"

class ServiceCenter:
    def __init__(self):
        self.requests = Queue()

    def generate_request(self):
        new_request = Request()
        self.requests.put(new_request)
        print(f"Згенеровано нову заявку з ID: {new_request.id}")

    def process_request(self):
        if not self.requests.empty():
            current_request = self.requests.get()
            start_time = time.time()  # Запам'ятовуємо час перед початком обробки
            print(f"      Обробляється заявка ID: {current_request.id}")
            # Тут можна додати логіку обробки заявки по суті або...
            # Імітація часу обробки
            time_to_process = random.randint(1, 5)
            time.sleep(time_to_process)

            end_time = time.time()  # Запам'ятовуємо час після завершення обробки
            print(f"       Час обробки заявки ID: {current_request.id}  зайняв {int(end_time - start_time)} сек.")
            
        else:
            print("! Черга пуста, немає заявок для обробки.")

# Створюємо сервісний центр
service_center = ServiceCenter()

# Імітація роботи протягом безкінечного циклу
try:
    while True:
        service_center.generate_request()
        time.sleep(random.randint(1, 3))  # Пауза для імітації часу очікування в черзі на обробку
        service_center.process_request()
        # time.sleep(random.randint(1, 5))  # Пауза для імітації часу обробки
except KeyboardInterrupt:
    print("Роботу зупинено.")
