# 大模型系统层

系统层关心“模型怎么训得动、跑得快、服务得稳”。

判断标准：如果一个概念主要解决算力、显存、通信、吞吐、延迟、稳定性、部署和服务问题，就放在这里。

| 子目录 | 关注点 |
| --- | --- |
| `01_训练系统` | DDP、FSDP、ZeRO、Tensor Parallel、Pipeline Parallel、Checkpoint |
| `02_推理系统` | KV Cache、PagedAttention、Continuous Batching、量化、Speculative Decoding |
| `03_服务系统` | API、流式输出、限流、缓存、监控、日志、灰度发布 |
| `04_硬件与通信` | GPU、HBM、NVLink、PCIe、RDMA、存储与网络瓶颈 |
| `05_框架与引擎` | PyTorch、DeepSpeed、Megatron、vLLM、SGLang、TGI |

一句话：系统层解决“模型能力如何被高效稳定地运行出来”。
