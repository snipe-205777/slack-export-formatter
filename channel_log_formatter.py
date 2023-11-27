import os
from log_formatter import log_formatter


if __name__ == "__main__":
    channel = ""

    dates = os.listdir(f"raw_export/{channel}")

    dates = [date.strip(".json") for date in dates if date[-5:] == ".json"]

    for date in dates:
        log_formatter(channel, date)
