# 🤖📰 AI News Analyst & Fact Checker

> *A modern Python application that combines intelligent web scraping with LLM-powered fact-checking and analysis of news articles*

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![UV Package Manager](https://img.shields.io/badge/package%20manager-UV-orange)](https://docs.astral.sh/uv/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 Project Overview

The **AI News Analyst** is a sophisticated news analysis platform that leverages cutting-edge technologies to scrape, analyze, and fact-check news articles from multiple sources. Built with modern Python tooling, it combines intelligent web scraping with advanced LLM capabilities to provide comprehensive news analysis.

### ✨ Key Features

- **🕷️ Intelligent Web Scraping**: Powered by [Crawl4AI](https://github.com/unclecode/crawl4ai) for LLM-friendly content extraction
- **🧠 LLM-Powered Analysis**: Uses [Pydantic AI](https://github.com/pydantic/pydantic-ai) for structured fact-checking and sentiment analysis
- **⚡ Modern Python Stack**: Built with FastAPI, SQLAlchemy, and async/await patterns
- **🔍 Multi-Source Analysis**: Aggregates news from BBC, Reuters, AP News, and more
- **📊 Structured Data Models**: Type-safe data models with Pydantic for reliability
- **🚀 REST API**: Clean FastAPI interface for integration with frontends
- **📈 Real-time Processing**: Async processing for high-performance analysis

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web Sources   │───▶│   Crawl4AI      │───▶│  Data Models    │
│  (BBC, Reuters) │    │  Web Scraper    │    │   (Pydantic)    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                        │
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend/API  │◀───│   FastAPI       │◀───│  LLM Agents     │
│   Integration   │    │   REST API      │    │ (Pydantic AI)   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                        │
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Database      │◀───│  SQLAlchemy     │◀───│   Services      │
│  (SQLite/Postgres)   │  Async ORM      │    │ (Orchestration) │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- **Python 3.11+** 
- **UV Package Manager** (recommended) - [Install UV](https://docs.astral.sh/uv/)
- **Git**

### 1. Clone & Setup

```bash
# Clone the repository
git clone https://github.com/MaxGaipl/ai-news-analyst.git
cd ai-news-analyst

# Install dependencies with UV
uv sync

# Initialize Crawl4AI (one-time setup)
crawl4ai-setup
```

### 2. Configuration

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your API keys
# At minimum, add your OpenAI API key:
# OPENAI_API_KEY="your_openai_api_key_here"
```

### 3. Run the Application

```bash
# Start the development server
uv run uvicorn src.news_analyst.api.main:app --reload

# Or use the FastAPI CLI
uv run fastapi dev src/news_analyst/api/main.py
```

## 📁 Project Structure

```
ai-news-analyst/
├── 📁 src/news_analyst/          # Main application package
│   ├── 📁 models/                # Pydantic data models
│   ├── 📁 scrapers/              # Crawl4AI web scraping
│   ├── 📁 agents/                # Pydantic AI LLM agents
│   ├── 📁 database/              # SQLAlchemy database layer
│   ├── 📁 services/              # Business logic orchestration
│   └── 📁 api/                   # FastAPI REST endpoints
├── 📁 tests/                     # Test suite
│   ├── 📁 unit/                  # Unit tests
│   ├── 📁 integration/           # Integration tests
│   └── 📁 e2e/                   # End-to-end tests
├── 📁 data/                      # Data storage
│   ├── 📁 raw/                   # Raw scraped data
│   ├── 📁 processed/             # Processed data
│   └── 📁 cache/                 # Cached content
├── 📁 scripts/                   # Utility scripts
└── 📁 logs/                      # Application logs
```

## 🛠️ Technology Stack

### Core Dependencies

| Technology | Purpose | Version |
|------------|---------|---------|
| [Crawl4AI](https://github.com/unclecode/crawl4ai) | Intelligent web scraping | `>=0.4.0` |
| [Pydantic AI](https://github.com/pydantic/pydantic-ai) | LLM agent framework | `>=0.2.14` |
| [FastAPI](https://fastapi.tiangolo.com/) | REST API framework | `>=0.115.12` |
| [SQLAlchemy](https://sqlalchemy.org/) | Async database ORM | `>=2.0.41` |
| [Alembic](https://alembic.sqlalchemy.org/) | Database migrations | `>=1.16.1` |
| [Uvicorn](https://uvicorn.org/) | ASGI server | `>=0.34.3` |

### Development Tools

- **UV**: Modern Python package manager
- **Ruff**: Lightning-fast linter and formatter
- **Black**: Code formatter
- **MyPy**: Static type checking
- **Pytest**: Testing framework
- **Pre-commit**: Git hooks for code quality

## 🔧 Development Workflow

### Setting up Development Environment

```bash
# Install development dependencies
uv sync --group dev

# Install pre-commit hooks
uv run pre-commit install

# Run tests
uv run pytest

# Run linting
uv run ruff check .
uv run ruff format .

# Type checking
uv run mypy src/
```

### Project Issues & Roadmap

This project is developed incrementally following GitHub issues:

- [x] **Issue #1**: Project Setup & Structure ✅
- [ ] **Issue #2**: Data Models (Pydantic)
- [ ] **Issue #3**: Web Scraping Engine (Crawl4AI) 
- [ ] **Issue #4**: LLM Analysis Agents (Pydantic AI)
- [ ] **Issue #5**: Database Layer (SQLAlchemy)
- [ ] **Issue #6**: Analysis Orchestration
- [ ] **Issue #7**: REST API (FastAPI)
- [ ] **Issue #8**: Testing Framework

## 📖 Usage Examples

### Basic News Analysis

```python
import asyncio
from news_analyst import AnalysisOrchestrator

async def analyze_news():
    orchestrator = AnalysisOrchestrator()
    
    # Analyze a single article
    result = await orchestrator.analyze_article(
        url="https://www.bbc.com/news/example-article"
    )
    
    print(f"Fact Check Score: {result.fact_check.confidence}")
    print(f"Sentiment: {result.sentiment.label}")
    print(f"Key Claims: {result.extracted_claims}")

# Run the analysis
asyncio.run(analyze_news())
```

### REST API Usage

```bash
# Start the API server
uv run uvicorn src.news_analyst.api.main:app --reload

# Analyze an article via API
curl -X POST "http://localhost:8000/analyze" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.bbc.com/news/example-article"}'
```

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes** and **add tests**
4. **Run the test suite**: `uv run pytest`
5. **Commit your changes**: `git commit -m 'Add amazing feature'`
6. **Push to the branch**: `git push origin feature/amazing-feature`
7. **Open a Pull Request**

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Crawl4AI](https://github.com/unclecode/crawl4ai) - For intelligent web scraping capabilities
- [Pydantic AI](https://github.com/pydantic/pydantic-ai) - For structured LLM interactions
- [FastAPI](https://fastapi.tiangolo.com/) - For the excellent API framework
- [UV](https://docs.astral.sh/uv/) - For modern Python package management

## 📞 Contact

- **Author**: Max Gaipl
- **GitHub**: [@MaxGaipl](https://github.com/MaxGaipl)
- **Project Link**: [https://github.com/MaxGaipl/ai-news-analyst](https://github.com/MaxGaipl/ai-news-analyst)

---

*Built with ❤️ and modern Python tools*