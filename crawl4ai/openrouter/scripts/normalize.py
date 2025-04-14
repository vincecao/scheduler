import os
import json
import re


def parse_models(file_path, seen_models):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    models = []

    for line in lines:
        # Use regex to extract the model details
        match = re.match(
            r"\[([^\]]+)\]\(([^)]+)\)`([^`]+)`\s*\|\s*([\d,]+)", line.strip()
        )
        if match:
            name = match.group(1)
            url = match.group(2)
            model = match.group(3)
            token_context = match.group(4)

            # Safely convert token_context to integer, handling commas
            try:
                token_context_int = int(
                    token_context.replace(",", "")
                )  # Remove commas for large numbers
            except ValueError:
                token_context_int = 0  # Default value if conversion fails

            # Determine usage based on model name
            usage = "free" if ":free" in model else "paid"

            # Check for duplicates
            if model not in seen_models:
                seen_models.add(model)
                models.append(
                    {
                        "model": model,
                        "name": name,
                        "url": url,
                        "tokenContext": token_context_int,
                        "usage": usage,
                    }
                )

    return models


def main():
    # Define paths to the input files
    free_models_path = os.path.join("crawl4ai", "openrouter", "raw", "free-models")
    top_models_path = os.path.join("crawl4ai", "openrouter", "raw", "top-models")

    # Initialize a set to track seen models across all files
    seen_models = set()

    # Parse the models
    free_models = parse_models(free_models_path, seen_models)
    top_models = parse_models(top_models_path, seen_models)

    # Combine the models
    all_models = free_models + top_models

    # Ensure the output directory exists
    output_dir = os.path.join("crawl4ai", "openrouter", "db")
    os.makedirs(output_dir, exist_ok=True)

    # Write the combined models to a JSON file
    output_path = os.path.join(output_dir, "models.json")
    with open(output_path, "w", encoding="utf-8") as output_file:
        json.dump(all_models, output_file, indent=2)

    print(f"Models have been normalized and saved to {output_path}")
    print(f"Total unique models: {len(all_models)}")


if __name__ == "__main__":
    main()