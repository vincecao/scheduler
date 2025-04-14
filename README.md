# Scheduler

A repository that automates scheduling tasks using GitHub Actions.

## Usage

This repository performs the following tasks:

1. **Fetching OpenRouter Models Weekly**:
   - The workflow fetches the latest free and paid models from OpenRouter every Sunday.
   - The normalized model list is available at [`crawl4ai/openrouter/db/models.json`](crawl4ai/openrouter/db/models.json).

2. **Fetching NBC News Daily**:
   - The workflow fetches daily news from NBC News.
   - The fetch history can be accessed at [`path/to/fetch/history`](path/to/fetch/history).

For more details, check the respective workflows and output files.

## Testing

``` bash
act -W .github/workflows/crawl4ai-weekly-open-router-options.yml -j scrape-and-process
```