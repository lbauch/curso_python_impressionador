# from datasets import load_dataset


# ds = load_dataset("facebook/natural_reasoning", split="train")

# print(ds["question"])

import pandas as pd

# Login using e.g. `huggingface-cli login` to access this dataset
df = pd.read_csv("hf://datasets/Anthropic/EconomicIndex/onet_task_mappings.csv")
print(df)