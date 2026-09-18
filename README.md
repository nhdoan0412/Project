# AI Resume Parser

An LLM-powered Python pipeline that converts unstructured PDF resumes into validated, structured JSON.

The project extracts text from resumes with **PyMuPDF**, sends the text through a **LangChain** prompt backed by **Google Gemini 1.5 Flash**, and validates the response with **Pydantic** models.

## Problem

Resume information is usually stored in inconsistent free-form documents. That makes downstream automation—such as candidate search, analytics, and job matching—harder because each resume uses different formatting and section names.

This project explores a structured extraction pipeline:

```text
PDF Resume
    ↓
PyMuPDF text extraction
    ↓
LangChain prompt
    ↓
Gemini 1.5 Flash
    ↓
Pydantic validation
    ↓
Structured JSON
```

## Tech Stack

- Python
- LangChain
- Google Gemini 1.5 Flash
- Pydantic
- PyMuPDF
- python-dotenv

## Current Features

- Extracts text from multi-page PDF resumes.
- Uses an LLM to map free-form resume content into structured fields.
- Validates model output with typed Pydantic schemas.
- Supports education, work experience, skills, contact information, and years of experience.
- Exposes a command-line workflow that writes the parsed result to JSON.

## Structured Output

```text
Resume
├── name
├── contact_number
├── email
├── skills[]
├── educations[]
│   ├── institution
│   ├── start_date
│   ├── end_date
│   ├── location
│   └── degree
├── work_experiences[]
│   ├── company
│   ├── start_date
│   ├── end_date
│   ├── location
│   └── role
└── YoE
```

## Repository Structure

| File | Purpose |
| --- | --- |
| `parser.py` | CLI entry point: PDF → structured JSON |
| `utils.py` | PDF text extraction using PyMuPDF |
| `llm_service.py` | LangChain + Gemini extraction pipeline |
| `models.py` | Pydantic schemas for validated output |
| `requirements.txt` | Python dependencies |
| `lru_cache.py` | LRU-cache implementation stored with the project |

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a local `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

Do not commit API keys or local environment files.

## Usage

```bash
python parser.py sample1.pdf output.json
```

The parser:

1. opens the PDF,
2. extracts text from each page,
3. invokes the Gemini/LangChain extraction chain,
4. validates the response against the `Resume` schema, and
5. saves the structured result as JSON.

## Engineering Decisions

### Typed LLM output

Pydantic provides a stable contract for downstream code instead of requiring consumers to parse arbitrary natural-language model responses.

### Low-temperature generation

Gemini is configured with a low temperature because resume parsing is primarily an information-extraction task, where consistency is more important than creativity.

### Modular pipeline

PDF extraction, LLM invocation, and schema validation are separated into different modules so each layer can evolve independently.

## Planned Improvements

- Add resume-to-job-description semantic matching.
- Add batch processing for multiple resumes and job descriptions.
- Add automated tests for malformed PDFs and incomplete model responses.
- Add an evaluation dataset for extraction accuracy.
- Add a lightweight API or web interface.

## Status

This repository currently implements the **resume parsing and structured extraction** portion of a broader resume-matching workflow. Planned functionality is listed separately rather than presented as already completed.
