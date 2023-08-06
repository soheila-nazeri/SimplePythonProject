
# Simple Python Project

This is a simple Python project that demonstrates basic usage of GitHub Actions for Continuous Integration/Continuous Deployment (CI/CD).

## Project Structure

The project consists of the following files and directories:

- `main.py`: The main Python script containing the `hello_world` function.
- `test/`: Directory containing test files.
    - `test_main.py`: Test file for the `hello_world` function.
    - `test1_main.py`: Test file for the `calculate_average` function.

## Getting Started

Follow these steps to run the project and tests locally:

1. Clone the repository:

   ```bash
   git clone https://github.com/soheila-nazeri/SimplePythonProject.git
   cd SimplePythonProject

2. python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
3. pip install -r requirements.txt

4. pytest

## GitHub Actions
This project is configured with GitHub Actions to automate testing on each push to the main branch. The workflow can be found in the .github/workflows/ci-cd.yml file.

## Contributing
If you'd like to contribute to this project, feel free to open issues or pull requests.

## License

