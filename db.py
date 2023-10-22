import winreg as wrg

"""
The Structure of DB Variable:

* It is an dict with tuples. And tuples have 3 elements each.
First element is "Windows Registry Hive". Second element is path
to the desired cell. The last one element is name of the cell.

* There is more than one hundred pathes which you can use to
scrape the system information for interests.

* Please use this only on your computer or warn others about
manipulations whether you use their device.
"""

DB = {
    "ComputerName": (wrg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\ComputerName\ActiveComputerName", "ComputerName")
}