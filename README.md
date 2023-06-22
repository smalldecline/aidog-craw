# AI dog 自动脚本

### 安装依赖：

playwright  
参考这个网站
https://playwright.dev/python/docs/intro

pyperclip
python-dotenv
直接包管理器安装


### 如何使用
在当前目录下创建.env文件，填写ACCOUNT和PASSWORD以及相关参数

示例(.env):
```
ACCOUNT=123456789
PASSWORD=123456789
BROWSER_COUNT=2
BLOCK_COUNT_PER_BROWSER=2
HEADLESS=true

```

或者直接在test_craw.py里填写account和password

然后在prompt.md里填写prompt

修改test_craw.py里的参数,然后运行

运行 test_craw.py 查看运行效果

test_craw很简单你可以自行修改

运行clean进行json格式校验

### 简介

```
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
```

count 为生成的次数，callback为每次生成内容的回调，默认使用gpt-4，当然账号必须为能使用gpt4的
