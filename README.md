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
调整browser_count来调整并发数
4个浏览器并发大约消耗1gb内存
headless为是否不显示浏览器

示例(.env):
```
ACCOUNT=123456789
PASSWORD=123456789
BROWSER_COUNT=2
TOTAL_COUNT=2000
HEADLESS=true
OUT_DIR=./out
PROMPT_PATH=./prompt.md
```

运行run_craw开始生产
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
