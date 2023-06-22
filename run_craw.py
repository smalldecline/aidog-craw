import craw
from dotenv import load_dotenv
import os
import threading
import time

load_dotenv()

global total_size
global block_count_per_browser

account = os.getenv("ACCOUNT")
password = os.getenv("PASSWORD")
browser_count = int( os.getenv("BROWSER_COUNT"))
block_count_per_browser = int(os.getenv("BLOCK_COUNT_PER_BROWSER"))
headless = os.getenv("HEADLESS") == "true"


total_size = 0


prompt = ""
with open("prompt_test.md", "r") as f:
    prompt = f.read()



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


# 程序开始运行的时间
start_time = time.time()

def start_browser(browserId):
    global total_size
    global time
    global headless
    def my_callback(content, count):
        global total_size
        global start_time
        size = count_pattern_occurrences(content, "},")+1
        total_size += size
        t = time.time() - start_time
        speed = total_size / t

        with open("out/b%d-%d.json" % (browserId,count), "w") as f:
            f.write(content)

        print("[data generated] - browser_id:%d size:%d last_count:%d total:%d speed:%.2f json/s" % (browserId,size,block_count_per_browser-count, total_size, speed))

    output = craw.craw(account, password, prompt, block_count_per_browser, my_callback, "gpt-4",show_output=False, headless=headless)


threads = []
for i in range(browser_count):
    t = threading.Thread(target=start_browser, args=(i,))
    threads.append(t)
    t.start()

