import craw

prompt = """
# Your task is to generate a dataset for training a large language model, specifically fine-tuned for data analysis in the field of finance. Each data point in the dataset should consist of:\n\n1. `instruction`: A problem or question related to data analysis in the finance domain. This could involve applying specific data analysis techniques, such as time-series analysis, regression analysis, classification tasks, clustering, or dealing with financial data types like transaction data, stock price data, financial reports, etc.\n2. `input`: This field should be null or empty.\n3. `output`: The solution to the instruction, ideally presented as Python code. This could also include an explanation of the solution if necessary.\n\n# Here is an example of what a data point might look like:\n\n{\"instruction\": \"The CSMAR Database (China Stock Market & Accounting Research Database) is a research-oriented, precise database in the field of economics and finance developed by Shenzhen Xinsigma Data Technology Co., Ltd. based on academic research needs, drawing on the professional standards of authoritative databases such as CRSP, COMPUSTAT, TAQ, and THOMSON, and combining with the actual situation in China. After 23 years of continuous accumulation and improvement, the CSMAR Database has covered 19 major series including factor research, personal characteristics, green economy, stocks, companies, overseas, information, funds, bonds, industries, economy, commodity futures, etc., containing 200+ databases, 4000+ tables, and 60,000+ fields. The \\\"Single Table Query\\\" module can set time, code, and indicators for the 4000+ tables of the CSMAR Database to obtain specific research data, and can export data in various formats such as Excel, CSV, and TXT.\\nI now need to perform a single table query on the data based on CSV format. Can you provide me with the code framework?\",\"input\": \"\",\"output\": \"import csv\\nwith open('example.csv', newline='') as csvfile:\\n  reader = csv.reader(csvfile, delimiter=',', quotechar='\\\"')\\n  for row in reader:\\n    print(', '.join(row))\"}\n\n\n# Each data point should follow this json format:\n\n{\"instruction\": <question>,\"input\": \"\",\"output\": <The solution to the instruction>}\n\n# Topic\n1. Inventory management\n2. Pricing optimization\n3. Risk analysis and management\n4. Credit scoring\n5. Fraud detection in financial transactions\n6. Healthcare data analysis\n7. Genomics and bioinformatics analysis\n\n# Notice\nPlease try to generate datasets as high quality as the examples\nMultiple datasets need to be combined into a json array\n\n
"""

account = "your account"
password = "your password"


def my_callback(content, count):
    # content保存为文件，文件名为 output-count.txt
    with open("output-%d.txt" % count, "w") as f:
        f.write(content)


output = craw.craw(account, password, prompt, 3, my_callback, "gpt-4")
