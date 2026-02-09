import re

def clean_output(text: str) -> str:
    """
    Cleans unnecessary extra spaces and fixes formatting.
    """
    # Remove extra spaces
    text = re.sub(r'\n\s*\n', '\n\n', text)
    text = text.strip()
    return text


def format_as_markdown(text: str) -> str:
    """
    Ensures headline and sections are properly formatted.
    """
    lines = text.split("\n")

    formatted_lines = []

    for i, line in enumerate(lines):
        # Make first line a headline
        if i == 0 and line.strip():
            formatted_lines.append(f"## {line.strip()}")
        else:
            formatted_lines.append(line)

    return "\n".join(formatted_lines)
