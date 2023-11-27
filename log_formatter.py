import json
import os
import re


def get_username(id):
    with open(f"raw_export/users.json", "r") as u:
        users = json.load(u)
        for user in users:
            if user["id"] == id:
                return user["name"]


def log_formatter(channel, date):
    raw_file = f"raw_export/{channel}/{date}.json"
    output_dir = f"message_logs/{channel}"
    output_file = f"{output_dir}/{date}.txt"

    with open(raw_file, "r") as f:
        logs = []
        raw = json.load(f)
        for message in raw:
            if "subtype" in message.keys() and message["subtype"] == "channel_join":
                logs.append(message["text"])
            elif "user_profile" in message.keys():
                logs.append(f'{message["user_profile"]["name"]}: {message["text"]}')
            else:
                logs.append(f'{message["bot_profile"]["name"]}: {message["text"]}')

    logs = "\n".join(logs)
    ping_match = re.compile("<@(.*)>")

    pings = ping_match.findall(logs)

    for ping in pings:
        name = get_username(ping)
        logs = logs.replace(ping, name)

    if not os.path.isdir("message_logs"):
        os.mkdir("message_logs")

    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    with open(output_file, "w") as f:
        f.write(logs)
