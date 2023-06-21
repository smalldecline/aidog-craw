# AI dog 自动脚本

依赖：

```
playwright
pyperclip
```


运行 test_craw.py 查看运行效果

```
def craw(
    account: str,
    password: str,
    prompt: str,
    count=1,
    callback: Callable[str, Optional[int]] = None,
    model="gpt-4",
) -> str:
```

count 为生成的次数，callback为每次生成内容的回调，默认使用gpt-4，当然账号必须为能使用gpt4的
