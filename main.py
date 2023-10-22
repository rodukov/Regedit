import winreg as wrg
from db import DB


def get(hive: int, path: str, cell: str) -> tuple:
    path = wrg.OpenKeyEx(hive, path)
    data = wrg.QueryValueEx(path, cell)
    return data

print(
    get(*DB['ComputerName'])[0]
)
