# Introduction

Welcome to the Test Suites for Generative AI Prompt Testing project! This repository offers a comprehensive testing framework designed to evaluate the performance and behavior of various Generative AI models using prompt-based test cases. By supporting multiple AI clients—including Ollama, OpenAI, Anthropic, and Amazon Bedrock—this project provides a unified approach to testing, ensuring consistency and reliability across different models and platforms.


# Motivation

As Generative AI models become increasingly integral to applications ranging from chatbots to content generation, ensuring their correctness, reliability, and ethical compliance is more important than ever. Traditional software engineering employs testing strategies like Test-Driven Development (TDD) and Behavior-Driven Development (BDD) to validate code functionality. However, testing AI models introduces unique challenges:

- **Probabilistic Outputs:** AI models may produce different outputs for the same input due to their stochastic nature.
- **Complexity of Language Understanding:** Evaluating the correctness of natural language outputs can be subjective and context-dependent.
- **Diverse Scenarios:** Models must be tested across a wide range of prompts to ensure robustness and handle edge cases.

This project was created to address these challenges by:

- **Providing a Systematic Testing Framework:** Automate the evaluation of AI model outputs against expected results.
- **Supporting Multiple AI Clients:** Facilitate testing across different AI models and APIs without the need for separate testing tools.
    - **Supported AI Clients**:
        - [Ollama](https://ollama.com/)
        - [OpenAI](https://openai.com/index/openai-api/)
        - [Anthropic](https://www.anthropic.com/api)
        - [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/)
    - Support for **more AI Clients to come**. If you like support for any AI API endpoints, please put in a **Feature Request** on GitHub
- **Enhancing Model Reliability:** Identify inconsistencies, biases, or unwanted behaviors in AI model responses.
- **Streamlining Development Workflow:** Integrate testing into the development pipeline, promoting best practices in AI model deployment.

By leveraging this testing suite, developers and researchers can ensure that their Generative AI models meet the desired performance standards and behave as intended in various scenarios.

Whether you're developing a new AI application or maintaining an existing one, this project aims to make the testing process more efficient and effective. We welcome contributions and feedback from the community to improve and expand this testing framework.


# User Guide


## Pre-requisites
- Python 3.12.x
- PIP or Poetry package manager
- Access to at least one API enpoint:
    - [Ollama](https://ollama.com/) installed and running
    - Access to [OpenAI](https://openai.com/index/openai-api/) API Key
    - Access to [Anthropic](https://www.anthropic.com/api) API Key

> If you like support for other API endpoints, please put in a **Feature Request** on GitHub


## Step 1: Clone the repo from GitHub
```bash
git clone https://github.com/joelee/GenAI-Prompt-Test-Suites.git
```

## Step 2: Update the API keys in `.env` file

Create a `.env` file, example below:

```ini
OLLAMA_API_URL='http://localhost:11434/api/generate'
OPENAI_API_KEY="Your-OpenAI-api-key-here"
ANTHROPIC_API_KEY="Your-Anthropic-api-key-here"
```

> See `.env.sample` file for example


## Step 3: Define models and test cases
Edit the `config.yaml` file for your Models and Test Cases.

`config.yaml` is self explainatory. There are two sections for the **API Clients** and **Test Cases**.

### API Clients
- `model`: Name of the AI Model
- `type`: Type of API Client, currently supporting:
    - `ollama`: Ollama API
    - `openai`: OpenAI (ChatGPT) API
    - `anthropic`: Anthropic (Claude) API
    - `bedrock`: Amazon Bedrock
- `max_tokens`: Maximum Tokens
- `temperature`: Temperature
- `system_prompt`: Optional System Prompt
- `disabled`: If `true` will exclude this client

#### Example
```yaml
clients:
  # Anthropic Claude 3 Haiko model
  - model: claude-3-haiku-20240307
    type: anthropic
    max_tokens: 1000
    temperature: 0
    system_prompt: You are Claude 3 Haiku, an AI assistant.
    disabled: false
```

### Test Cases
- `name`: The name of the Test Case
- `prompt`: User prompt for the Test Case
- `expected_substrings`: Expected text in the response
- `forbidden_substrings`: Forbidden text in the response

#### Example
```yaml
test_cases:
  - name: "Strawberry test"
    prompt: "Count how many Rs are there in the word straberry"
    expected_substrings:
      - three
      - "3"
    forbidden_substrings:
      - two
      - "2"      
```


## Step 4: Install required packages

### PIP
```bash
pip install -r requirements.txt
```

### Poetry
```bash
poetry install
```

## Step 5: Run tests


### PIP
```bash
python src/main.py
```

### Poetry
```bash
poetry run
```

