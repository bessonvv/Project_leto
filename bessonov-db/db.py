import argparse
from tables import TableManager

parser = argparse.ArgumentParser(prog='db')
# Создает область args.command в которую будут добавляться комманды
sub = parser.add_subparsers(dest='command', required=True)
# Команда create
create_cmd = sub.add_parser('create', help="Создать таблицу")
create_cmd.add_argument("-n","--name", help="Назначает имя таблице")
create_cmd.add_argument("-c", "--columns", help="Создает атрибуты таблицы")

if __name__=="__main__":
    args = parser.parse_args()
    if args.command == 'create':
        TableManager.create(args.name, args.columns)