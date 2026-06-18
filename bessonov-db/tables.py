import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO) # Устанавливаем показывать логи от уровня INFO


class TableManager:
    def __init__(self):
        pass
        # self._path = './storage/storage.txt'
        # # Проверяем диск: вдруг таблица уже создавалась раньше?
        # if os.path.exists(self._path):
        #     self.address_storage = self._path  # подхватываем существующий файл

    @staticmethod
    def create(table_name: str, columns: str | None = None) -> None:
        storage_path = Path('storage') / f'{table_name}.txt'
        os.makedirs('storage', exist_ok=True)

        # Реализация "-n (--name)"
        if os.path.exists(storage_path):
            logging.error(f"Таблица {table_name} уже существует!")
        else:
            Path(f'./storage/{table_name}.txt').touch()
            logging.info(f"Вы создали таблицу {table_name}")

        # Реализация "-c (--columns)"
        if isinstance(columns, str):
            columns = [col.strip() for col in columns.split(',')]
            storage_path.write_text(','.join(columns) + '\n', encoding='utf-8')
        else:
            storage_path.write_text('id, value\n', encoding='utf-8') # По умолчанию создает id, value

    def add_value(self, value):
        pass

    def automatic_id(self):
        pass

    def show_table(self):
        pass