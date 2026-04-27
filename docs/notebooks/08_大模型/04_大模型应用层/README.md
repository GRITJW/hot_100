# 大模型应用层

应用层关心“模型怎么被用于真实任务、真实系统、真实业务”。

判断标准：如果一个概念通常不改模型权重，而是改变模型的使用方式、外部知识、工具连接、执行流程或业务交互，就放在这里。

| 子目录 | 关注点 |
| --- | --- |
| `01_Prompt与结构化输出` | Prompt、Few-shot、CoT、JSON Schema、guided decoding |
| `02_RAG与知识增强` | chunk、embedding、向量库、混合检索、rerank、上下文构造 |
| `03_ToolCalling与MCP` | Tool Calling、Function Calling、MCP、工具权限与沙箱 |
| `04_Agent工程` | Planning、ReAct、Reflection、handoff、多 Agent、workflow 编排 |
| `05_记忆与状态` | 短期上下文、长期记忆、会话状态、任务状态 |
| `06_可观测与评测` | tracing、guardrails、human-in-the-loop、Agent 成功率评测 |
| `07_场景落地` | 客服、代码助手、搜索问答、数据分析、推荐解释、办公自动化 |

RAG 属于应用层里的“能力增强算法”：它增强的是整个应用系统的回答能力，而不是直接增强模型参数本身。
