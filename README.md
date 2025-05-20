# Software Architecture Assessment Tool

This tool assists in semi-automated evaluation of software architecture using LLMs. It supports quality attribute extraction, design decision extraction, sustainability dimension mapping and SIS calculation.

## Setup instructions

### Clone the repository 

```bash
git clone https://github.com/your-username/sa-automation-tool.git
cd sa-automation-tool/backend
```

### Create and Activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the backend component

```bash
uvicorn main:app --reload
```


