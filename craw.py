from playwright.sync_api import Playwright, sync_playwright, expect
import time
import pyperclip
from typing import Callable, Optional


def craw(
    account: str,
    password: str,
    prompt: str,
    count=1,
    callback: Callable[str, Optional[int]] = None,
    model="gpt-4",
    show_output=True,
    headless=False,
) -> str:
    output = []

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=headless)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://a5.1919qwe.com/#/login")
        page.get_by_placeholder("请输入用户名").fill(account)
        page.get_by_placeholder("请输入密码").fill(password)
        page.get_by_role("button", name="确定").click()

        if model == "gpt-4":
            # page.goto("https://a5.1919qwe.com/#/gpt4")
            page.get_by_role("button", name="GPT4").nth(1).click()

        last_count = count
        while last_count > 0:
            page.locator("div:nth-child(3) > .n-icon-wrapper").click()
            page.get_by_placeholder(
                "输入框上方功能图标，可设置角色，多会话，清除。请输入消息，Enter发送，Shift+Enter换行"
            ).fill(prompt)

            page.get_by_role("button", name="发送").click()
            page.locator("div:nth-child(3) > .chat-message-bubble").click()

            stop_sending = page.get_by_role("button", name="暂停回复")
            finished_generating = False
            t = 0
            while not finished_generating:
                if(show_output):
                    page.locator(
                        "div:nth-child(3) > .chat-message-meta > .chat-toolbar-icon"
                    ).click()

                    print(
                        "generating... wait:%ds model:%s last count:%d content:%s"
                        % (t, model, count - last_count + 1, pyperclip.paste())
                    )
                time.sleep(1)
                t += 1

                if not stop_sending.is_visible():
                    finished_generating = True

            # reply_bubble = page.locator("div:nth-child(3) > .chat-message-bubble")
            # reply_bubble.inner_text()  # get the reply

            page.locator(
                "div:nth-child(3) > .chat-message-meta > .chat-toolbar-icon"
            ).click()
            # 获取剪切板内容，输出到控制台
            result = pyperclip.paste()
            callback(result, count - last_count + 1)
            output.append(result)
            last_count = last_count - 1

        # ---------------------
        context.close()
        browser.close()

    return output
