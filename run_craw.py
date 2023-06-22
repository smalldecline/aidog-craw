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
total_count = int(os.getenv("TOTAL_COUNT"))
headless = os.getenv("HEADLESS") == "true"
out_dir = os.getenv("OUT_DIR")
prompt_path = os.getenv("PROMPT_PATH")

total_size = 0


prompt = ""
with open(prompt_path, "r") as f:
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

        with open("%s/b%d-%d.json" % (out_dir,browserId,count), "w") as f:
            f.write(content)

        if(total_size >= total_count):
            print("[task finished] - browser_id:%d" % browserId)
            exit(0)

        print("[data generated] - browser_id:%d size:%d total:%d progress:%.1f speed:%.2f json/s" % (browserId,size, total_size,total_size/total_count, speed))

    output = craw.craw(account, password, prompt, 1000, my_callback, "gpt-4",show_output=False, headless=headless)

print("[program started] - browser_count:%d total_count:%d prompt:%s outdir:%s" % (browser_count, total_count,prompt_path,out_dir))

threads = []
for i in range(browser_count):
    t = threading.Thread(target=start_browser, args=(i,))
    threads.append(t)
    t.start()
    print("[browser started] - id:%d" % i)

