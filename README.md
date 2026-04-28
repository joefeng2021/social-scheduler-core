# Social Scheduler Core

Cross‑platform social media scheduler core library.

## Overview

This library provides a unified interface for scheduling and publishing content across multiple social media platforms (Twitter/X, Mastodon, LinkedIn, etc.). It is designed as the core engine for a content‑creator automation tool.

## Features

- **Twitter/X API v2 wrapper** – post tweets, read timelines, retrieve user tweets
- **Modular design** – easy to add new platform adapters
- **Environment‑based configuration** – store API keys securely
- **Ready for PyPI** – packaged as a standard Python library

## Installation

```bash
pip install social-scheduler-core
```

Or from source:

```bash
git clone https://github.com/joefeng2021/social-scheduler-core.git
cd social-scheduler-core
pip install -e .
```

## Quick Start

1. **Set up Twitter API credentials**

   Create a `.env` file (copy from `.env.example`):

   ```bash
   cp .env.example .env
   ```

   Then edit `.env` and add your Twitter Bearer Token.

2. **Post a tweet**

   ```python
   from social_scheduler_core.twitter_client import TwitterClient

   client = TwitterClient()
   response = client.tweet("Hello from Social Scheduler Core!")
   print(f"Tweet posted: {response['id']}")
   ```

## Development

### Project Structure

```
src/social_scheduler_core/
├── __init__.py
├── twitter_client.py   # Twitter/X API wrapper
└── (more platform clients to come)
```

### Running Tests

```bash
pytest tests/
```

## Roadmap

- [x] Create GitHub repository and basic project structure
- [ ] Implement Twitter/X API v2 wrapper (in progress)
- [ ] Add Mastodon API support
- [ ] Add LinkedIn API support
- [ ] Implement scheduling queue with Celery
- [ ] Build web dashboard (FastAPI + React)

## License

MIT
