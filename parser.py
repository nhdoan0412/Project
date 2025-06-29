import json
import sys
from utils import extract_text_from_pdf
from llm_service import extract_resume_from_text


def parse_resume(pdf_path: str, output_path: str):
    text = extract_text_from_pdf(pdf_path)
    structured_resume = extract_resume_from_text(text)

    with open(output_path, 'w') as out:
        json.dump(structured_resume.dict(), out, indent=2)

    print(f"Resume parsed successfully! Output saved to: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python parser.py input_resume.pdf output_resume.json")
        sys.exit(1)

    parse_resume(sys.argv[1], sys.argv[2])

