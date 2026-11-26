
import torch
import torch.nn as nn
import torch.nn.functional as F


class Head(nn.Module):

    def __init__(self, n_embd, head_size, block_size):
        super().__init__()

        self.key = nn.Linear(n_embd, head_size, bias=False)
        self.query = nn.Linear(n_embd, head_size, bias=False)
        self.value = nn.Linear(n_embd, head_size, bias=False)

        self.register_buffer(
            "tril",
            torch.tril(torch.ones(block_size, block_size))
        )

    def forward(self, x):
        B, T, C = x.shape

        k = self.key(x)
        q = self.query(x)
        v = self.value(x)

        wei = q @ k.transpose(-2, -1)
        wei = wei * (k.shape[-1] ** -0.5)

        wei = wei.masked_fill(
            self.tril[:T, :T] == 0,
            float("-inf")
        )

        wei = F.softmax(wei, dim=-1)

        out = wei @ v

        return out

class MultiHeadAttention(nn.Module):

    def __init__(self, n_embd, num_heads, block_size):
        super().__init__()

        head_size = n_embd // num_heads

        self.heads = nn.ModuleList([
            Head(n_embd, head_size, block_size)
            for _ in range(num_heads)
        ])

    def forward(self, x):
        outputs = [head(x) for head in self.heads]

        out = torch.cat(outputs, dim=-1)

        return out

class FeedForward(nn.Module):

    def __init__(self, n_embd):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(n_embd, 5*n_embd),
            nn.ReLU(),
            nn.Linear(5*n_embd, n_embd)
        )

    def forward(self, x):
        return self.net(x)