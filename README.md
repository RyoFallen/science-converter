# Science Converter

A small command-line tool for converting between physical units. It supports
**length**, **mass** and **temperature** conversions and ships with an
automated test-suite that runs in a GitHub Actions CI pipeline.

## Features

- Length: `mm`, `cm`, `m`, `km`, `in`, `ft`, `mi`
- Mass: `mg`, `g`, `kg`, `t`, `oz`, `lb`
- Temperature: `C`, `F`, `K`

## Usage

```bash
python -m src.cli length 10 km mi
python -m src.cli temperature 100 C F
python -m src.cli mass 5 kg lb
```

## Running the tests

```bash
pip install -r requirements.txt
pytest -v
```

## Continuous Integration

Every push and pull request triggers the workflow in
[`.github/workflows/main.yml`](.github/workflows/main.yml), which boots an
`ubuntu-latest` runner and executes the test-suite with `pytest`.

## Project layout

```
science-converter/
├── src/
│   ├── converter.py   # core conversion logic (length, mass, temperature)
│   └── cli.py         # command-line interface
├── tests/
│   └── test_converter.py
└── .github/workflows/main.yml
```
