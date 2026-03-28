# agentic_ai_workflow_openai

Small Python examples that call the [OpenAI API](https://platform.openai.com/) for chat completions: a short multi-step demo and a business-sector “agentic opportunity” brainstorm.

## Prerequisites

- **Python** 3.14 or newer (see `pyproject.toml`)
- An **OpenAI API key** with access to the models used below (`gpt-4.1-nano`, `gpt-4.1-mini`)

## Setup

1. Clone or copy this repository and open a terminal in the project root.

2. Create a virtual environment and install dependencies:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install "openai>=2.30.0" "python-dotenv>=1.2.2" "ipython>=9.12.0" "markdown>=3.10.2"
   ```

   (Versions match `pyproject.toml`.)

3. Create a `.env` file in the project root:

   ```
   OPENAI_API_KEY=sk-...
   ```

   The scripts load this key via `python-dotenv`. Do not commit real keys.

## What’s included

| File | Purpose |
|------|---------|
| `main.py` | Loads the API key, runs a simple `gpt-4.1-nano` reply, then a two-step flow with `gpt-4.1-mini` (generate a hard question, then answer it). Uses `IPython.display` for Markdown output at the end—run from an environment where IPython is available (e.g. Jupyter or `ipython`). |
| `business_sector_openai.py` | Three chained chat calls with `gpt-4.1-mini`: suggest a business area, describe a pain point, then propose an agentic AI solution. |

## Run

From the project root, with `OPENAI_API_KEY` set (via `.env` or the environment):

```bash
python main.py
```

```bash
python business_sector_openai.py
```

If the API key is missing, the scripts print a short message instead of failing silently on the key check.

## Dependencies

Declared in `pyproject.toml`: `openai`, `python-dotenv`, `ipython`, `markdown`.

## License

Add a license if you publish this repository.
