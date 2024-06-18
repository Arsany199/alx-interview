#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""

import sys

if __name__ == "__main__":

    file_s = 0
    count = 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stat = {k: 0 for k in codes}

    def print_stats(stat: dict, file_s: int) -> None:
        """function that print stats"""
        print("File size: {:d}".format(file_s))
        for k, v in sorted(stat.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        for line in sys.stdin:
            count = count + 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in stat:
                    stat[status_code] += 1
            except BaseException:
                pass
            try:
                file_s = file_s + int(data[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                print_stats(stat, file_s)
        print_stats(stat, file_s)
    except KeyboardInterrupt:
        print_stats(stat, file_s)
        raise
