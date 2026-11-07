# from pathlib import Path
# dataset_path = Path("train.jsonl")
# print("Dataset exists:",dataset_path.exists())


# import json
# with open("train.jsonl", "r", encoding="utf-8") as file:
#     first_line = file.readline()
# example = json.loads(first_line)
# print(example)

import json
data=[]
with open("train.jsonl", "r", encoding="utf-8") as file:
    for line in file:
        example = json.loads(line)
        data.append(example)
# print("Total examples:", len(data))
# print("First example:", data[0])
example = data[0]
# print("data type:", type(example))
# print("Available keys:", example.keys())
# for key, value in example.items():
#     print("\nKey:", key)
#     print("Value type:", type(value))
#     print("Value:", value)
messages = example["messages"]
for message in messages:
    role = message["role"]
    content = message["content"]

    # print("ROLE:", role)
    # print("CONTENT:", content)
    # print("-" * 50)

### making one conversation a structured text format

def format_conversation(messages):
    text = ""
    for message in messages:
        role = message["role"]
        content = message["content"]
        text += f"[{role.upper()}]\n"
        text += content + "\n\n"
    text += "[END]\n"
    return text
# formatted_text = format_conversation(data[0]["messages"])
# print(formatted_text)

### making sure all examples in the dataset is properly formatted

formatted_conversations = []

for example in data:
    messages = example["messages"]
    formatted_text = format_conversation(messages)
    formatted_conversations.append(formatted_text)

print("Total formatted conversations:", len(formatted_conversations))
# print("First conversation:\n", formatted_conversations[0])