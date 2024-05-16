![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

# LLMGIpy

Large Language Model Genetic Improvement Python (LLMGIpy) is a software that allows you to evaluate the Python code generation of some LLMs and test the improvements of the code after applying Genetic Improvement.

## Included LLMs

- Gemma1.1 2B and 7B
- LLaMA2 7B and 13B
- LLaMA3 8B
- CodeLLaMA 7B and 13B
- CodeGemma 7B
- Mistral 7B
- ChatGPT and GPT4

Note that for Hugging Face models you need a (free) token and for OpenAI models you need to pay.

## Usage

Clone this repository, move to the folder

```
git clone https://github.com/dravalico/LLMGIpy
cd LLMGIpy
```

Create a conda environment from `environment.yml`

```
conda env create -f environment.yml
conda activate llmgipy
```

Move to `src` folder and run

```
python main.py --help
```
