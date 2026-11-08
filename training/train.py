# from pathlib import Path
# dataset_path = Path("train.jsonl")
# print("Dataset exists:",dataset_path.exists())


# import json
# with open("train.jsonl", "r", encoding="utf-8") as file:
#     first_line = file.readline()
# example = json.loads(first_line)
# print(example)

# import json
# data=[]
# with open("train.jsonl", "r", encoding="utf-8") as file:
#     for line in file:
#         example = json.loads(line)

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = REPO_ROOT / "data" / "train.jsonl"

import json

data = []
with open(DATASET_PATH, "r", encoding="utf-8") as file:
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

# print("Total formatted conversations:", len(formatted_conversations))
# print("First conversation:\n", formatted_conversations[0])

### building a vocabulary from the dataset

all_text = "".join(formatted_conversations)
chars = sorted(set(all_text))
vocab_size = len(chars)
# print("Vocabulary:", chars)
# print("Vocabulary size:", vocab_size)

### creating a mapping from characters to integers and vice versa

stoi = {ch: i for i, ch in enumerate(chars)}
itos = {i: ch for i, ch in enumerate(chars)}
encode = lambda s: [stoi[c] for c in s]
decode = lambda l: ''.join([itos[i] for i in l])
# print(encode("hello"))
# print(decode(encode("hello")))

### including tensors for tokenization and batching

import torch
text = formatted_conversations[0]
encoded_text = encode(text)
data_tensor = torch.tensor(encoded_text, dtype=torch.long)
# print("First 20 token IDs:", data_tensor[:20])
# print("Tensor shape:", data_tensor.shape)
# print("Tensor datatype:", data_tensor.dtype)

### making gpt able to predict the next token in a sequence


block_size = 10
x = data_tensor[:block_size]
y = data_tensor[1:block_size+1]
# print("Input tokens:", x)
# print("Target tokens:", y)
# print("Input text:", decode(x.tolist()))
# print("Target text:", decode(y.tolist()))


for t in range(block_size):
    context = x[:t+1]
    target = y[t]
    # print(
    #     f"Input: {decode(context.tolist())!r} "
    #     f"--> Target: {decode([target.item()])!r}"
    # )

batch_size = 5
block_size = 10

encoded_conversations = [
    torch.tensor(encode(text), dtype=torch.long)
    for text in formatted_conversations
]
def get_batch():
    x_batch = []
    y_batch = []
    for _ in range(batch_size):
        conversation = encoded_conversations[
            torch.randint(len(encoded_conversations), (1,)).item()
        ]
        start = torch.randint(
            len(conversation) - block_size,
            (1,)
        ).item()
        x = conversation[start:start + block_size]
        y = conversation[start + 1:start + block_size + 1]
        x_batch.append(x)
        y_batch.append(y)
    return torch.stack(x_batch), torch.stack(y_batch)
xb, yb = get_batch()
# print("Input batch shape:", xb.shape)
# print("Target batch shape:", yb.shape)

### Turning numbers into learnable vectors using an embedding layer

import torch.nn as nn
n_embd = 50
token_embedding_table = nn.Embedding(vocab_size, n_embd)
token_embeddings = token_embedding_table(xb)
print("Input shape:", xb.shape)
print("Embedding shape:", token_embeddings.shape)
print("First token embedding:", token_embeddings[0, 0])

### Adding positional information to the embeddings

position_embedding_table = nn.Embedding(block_size, n_embd)
positions = torch.arange(block_size)
position_embeddings = position_embedding_table(positions)
x = token_embeddings + position_embeddings
print("Positions:", positions)
print("Position embeddings shape:", position_embeddings.shape)
print("Combined embeddings shape:", x.shape)
