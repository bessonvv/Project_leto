import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO) # Устанавливаем показывать логи от уровня INFO


class TableManager:
    def __init__(self):
        pass

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
            storage_path.write_text('id,'+','.join(columns) + '\n', encoding='utf-8')
        else:
            storage_path.write_text('id, value\n', encoding='utf-8') # По умолчанию создает id, value

    def add_value(self, value):
        pass

    def automatic_id(self):
        pass

    def show_table(self):
        pass