# 大模型核心算法层

核心算法层关心“模型本身怎么被造出来、怎么变强”。

判断标准：如果一个概念会改变模型参数、训练目标、模型结构或对齐方式，就放在这里。

| 子目录 | 关注点 |
| --- | --- |
| `01_Tokenizer与文本建模` | 文本到 token 的映射，词表、特殊 token、Chat Template |
| `02_Transformer与模型架构` | Attention、RoPE、RMSNorm、SwiGLU、MoE |
| `03_预训练` | 数据、目标函数、Scaling Law、训练配比 |
| `04_后训练与偏好对齐` | SFT、Reward Model、RLHF、DPO、GRPO |
| `05_高效微调` | LoRA、QLoRA、Adapter、Prefix/Prompt Tuning |
| `06_模型评测与安全` | benchmark、LLM-as-a-Judge、幻觉、安全对齐 |

一句话：核心算法层解决“模型能力从哪里来”。
