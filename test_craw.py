import craw
from dotenv import load_dotenv
import os

load_dotenv()

# 读取prompt 从 prompt.md中
prompt = ""
with open("prompt.md", "r") as f:
    prompt = f.read()

account = os.getenv("ACCOUNT")
password = os.getenv("PASSWORD")


def my_callback(content, count):
    with open("output-%d.json" % count, "w") as f:
        f.write(content)


if prompt != "":
    output = craw.craw(account, password, prompt, 15, my_callback, "gpt-4")
