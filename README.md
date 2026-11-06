# 💬 Jesh Chatbox Python

> A sleek, plug-and-play Python AI chat application featuring a FastAPI backend, custom web UI, and generic LLM adapter logic.

---

### 🏗 Architecture

```mermaid
graph LR
    subgraph Frontend [Presentation Layer]
        UI[Templates & Static Assets]
    end

    subgraph Backend [FastAPI Service Layer]
        Router[API Endpoint Router]
        Logic[LLM Dispatcher Logic]
    end

    subgraph Providers [Inference Providers]
        Mock[Local Mock Mode]
        Remote[External Provider<br/>OpenAI / Ollama / API Gateway]
    end

    UI <--> Router
    Router <--> Logic
    Logic <-->|Default| Mock
    Logic <-->|Configured| Remote







