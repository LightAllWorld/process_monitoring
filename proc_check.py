import psutil
from time import sleep
from setting import *


def __init__():
    ret_dict = dict()

    for _proc in psutil.process_iter():
        try:
            name = _proc.name()
            pid = _proc.pid
            ret_dict[name] = pid

        except:
            pass

    return ret_dict


def main():
    while 1:
        proc_list = __init__()
        print("Init done")
        sleep(PROC_TIME)

        if TARTGET_PROC not in proc_list:
            print("===================================")
            print("  {} is not found!!".format(TARTGET_PROC))
            print("===================================")

        print("Check Done.")


if __name__ == "__main__":
    main()
