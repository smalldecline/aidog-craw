import glob
from datasets import load_dataset
from transformers import AutoTokenizer


tokenizer = AutoTokenizer.from_pretrained("huggyllama/llama-7b") # 羊驼分词器

json_files = glob.glob("*.json") # 文件夹下所有的 .json 文件
print(json_files)

dataset = load_dataset('json', data_files=json_files) # 加载.json文件作为数据集
print(dataset)

def tokenize_function(examples):
    # 预处理
    texts = [f"""
XXXXXXXXXX
### Instruction: 
{instr}


### Respond:
{out}
""" for instr, inp, out in zip(examples['instruction'], examples['input'], examples['output'])]
    return tokenizer(texts)

dataset = dataset.map(tokenize_function, batched=True) # 批量应用分词函数到数据集
print(dataset)