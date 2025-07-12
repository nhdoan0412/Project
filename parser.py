import sys
import json
from utils import extract_text_from_pdf
from llm_service import extract_resume_from_text

def parse_resume(input_pdf: str, output_json: str):
    text = extract_text_from_pdf(input_pdf)
    resume = extract_resume_from_text(text)
    with open(output_json, 'w') as f:
        json.dump(resume.dict(), f, indent=2)
    print(f"✅ Resume saved to: {output_json}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python parser.py input.pdf output.json")
        sys.exit(1)

    parse_resume(sys.argv[1], sys.argv[2])
