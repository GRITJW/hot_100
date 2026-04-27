# 08 大模型

本板块把大模型放在同一个最大目录下，再按三层拆开：

```text
大模型
├── 大模型核心算法层：模型怎么被造出来、怎么变强
├── 大模型系统层：模型怎么训得动、跑得快、服务得稳
└── 大模型应用层：模型怎么被接入真实任务、真实系统、真实场景
```

这三个层次的判断标准：

| 问题 | 所属层次 | 例子 |
| --- | --- | --- |
| 是否改变模型参数或训练目标？ | 核心算法层 | Tokenizer、Transformer、预训练、SFT、RLHF、DPO、GRPO、LoRA |
| 是否改变模型训练/推理/服务的效率与稳定性？ | 系统层 | FSDP、ZeRO、Tensor Parallel、KV Cache、vLLM、量化、服务并发 |
| 是否改变模型的使用方式和任务完成能力？ | 应用层 | Prompt、结构化输出、RAG、Tool Calling、MCP、Agent、业务落地 |

## 01 大模型核心算法层

回答“模型本身怎么来”的问题。

- `01_Tokenizer与文本建模`：文本如何变成 token 序列，Chat Template 如何影响训练和推理。
- `02_Transformer与模型架构`：Attention、位置编码、归一化、激活函数、MoE 等模型结构。
- `03_预训练`：数据、目标函数、Scaling Law、训练配比。
- `04_后训练与偏好对齐`：SFT、Reward Model、RLHF、DPO、GRPO。
- `05_高效微调`：LoRA、QLoRA、Adapter、Prefix/Prompt Tuning。
- `06_模型评测与安全`：benchmark、LLM-as-a-Judge、幻觉、安全对齐、越狱防御。

## 02 大模型系统层

回答“模型怎么跑”的问题。

- `01_训练系统`：DDP、FSDP、ZeRO、TP、PP、Checkpoint、混合精度。
- `02_推理系统`：KV Cache、PagedAttention、Continuous Batching、Speculative Decoding、量化。
- `03_服务系统`：API、流式输出、限流、缓存、日志、监控、灰度发布。
- `04_硬件与通信`：GPU、HBM、NVLink、PCIe、RDMA、存储与网络瓶颈。
- `05_框架与引擎`：PyTorch、DeepSpeed、Megatron、vLLM、SGLang、TGI。

系统层不是模型架构本身，也不只是芯片。它是从硬件、通信、分布式训练、推理引擎到线上服务的一整层工程能力。

## 03 大模型应用层

回答“模型怎么用”的问题。

- `01_Prompt与结构化输出`：Prompt、Few-shot、CoT、JSON Schema、guided decoding。
- `02_RAG与知识增强`：chunk、embedding、向量库、混合检索、rerank、上下文构造、答案校验。
- `03_ToolCalling与MCP`：函数调用、工具协议、MCP server、工具权限与沙箱。
- `04_Agent工程`：Planning、ReAct、Reflection、handoff、多 Agent、workflow 编排。
- `05_记忆与状态`：短期上下文、长期记忆、会话状态、任务状态。
- `06_可观测与评测`：Tracing、Guardrails、Human-in-the-loop、Agent 成功率评测。
- `07_场景落地`：客服、代码助手、搜索问答、数据分析、推荐解释、办公自动化。

RAG 放在应用层，因为它通常不改变模型参数，而是通过外部知识检索和上下文构造增强整个应用系统的回答能力。
