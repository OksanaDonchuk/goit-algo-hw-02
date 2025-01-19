import queue
import random
import time
from typing import NoReturn

# Створення черги заявок
request_queue: queue.Queue = queue.Queue()

def generate_request() -> None:
    """
    Генерує нову заявку з унікальним ідентифікатором та додає її до черги.
    """
    # Створення унікального ідентифікатору для заявки
    request_id: int = random.randint(1, 1000)
    request_data: str = f"Заявка #{request_id}"
    print(f"Створено заявку: {request_data}")
    # Додавання заявки до черги
    request_queue.put(request_data)

def process_request() -> None:
    """
    Обробляє заявку з черги. Якщо черга порожня, виводить відповідне повідомлення.
    """
    if not request_queue.empty():
        # Видалення заявки з черги
        request_data: str = request_queue.get()
        print(f"{request_data} оброблено!")
    else:
        print("Черга пуста, немає заявок для обробки.")

def main() -> NoReturn:
    """
    Головна функція програми, яка виконує генерацію та обробку заявок.
    """
    for _ in range(20):  # 20 ітерацій
        generate_request()
        process_request()
        time.sleep(0.5)  # Затримка в 0.5 секунди

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Сталася помилка: {e}")
    
print("\nУсі заявки оброблено. Виконання програми завершено.")