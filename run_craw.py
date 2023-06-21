import craw
from dotenv import load_dotenv
import os
import threading

load_dotenv()

# 读取prompt 从 prompt.md中
prompt = ""
with open("prompt.md", "r") as f:
    prompt = f.read()

account = os.getenv("ACCOUNT")
password = os.getenv("PASSWORD")

def count_pattern_occurrences(string, pattern)->int:
    count = 0
    start = 0
    while True:
        index = string.find(pattern, start)
        if index == -1:
            break
        count += 1
        start = index + 1
    return count

global total_size
global block_count_per_browser

browser_count = 10
block_count_per_browser = 25
total_size = 0

def start_browser(browserId):
    global total_size
    def my_callback(content, count):
        global total_size
        size = count_pattern_occurrences(content, "},")+1
        total_size += size

        with open("out/b%d-%d.json" % (browserId,count), "w") as f:
            f.write(content)

        print("[block generated] - id:%d size:%d total:%d" % (browserId,size, total_size))

    output = craw.craw(account, password, prompt, block_count_per_browser, my_callback, "gpt-4",show_output=False, headless=False)



threads = []
for i in range(browser_count):
    t = threading.Thread(target=start_browser, args=(i,))
    threads.append(t)
    t.start()