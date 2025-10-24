# QR Code Generator Application

A Dockerized Python application that generates QR codes from URLs with comprehensive testing and CI/CD pipeline.

## Project Overview

This application generates QR codes from URLs and saves them as PNG files. It includes environment configuration, comprehensive testing, and automated deployment through Docker and GitHub Actions.

## QR Code Examples

### My GitHub Repository
![Github Repo](qr_codes/QRCode_20251023235448.png "My QR Code Link")

### My DockerHub Image
![Docker QR Image](qr_codes/QRCode_20251023234730.png "My QR code Link")

## Features

- **URL Validation**: Validates URLs before generating QR codes
- **Configurable Colors**: Environment-based color configuration for QR codes
- **Docker Support**: Fully containerized application with Docker Compose
- **Comprehensive Testing**: 98% test coverage with pytest
- **CI/CD Pipeline**: Automated testing and deployment with GitHub Actions
- **Error Handling**: Robust error handling and logging

## Testing & Coverage

### Test Coverage Achievement ✅
- **Target Coverage**: 80%
- **Achieved Coverage**: **98%** (Exceeded target!)
- **Total Tests**: 10 comprehensive test cases
- **All Tests**: ✅ PASSING

### Test Coverage Includes:
- ✅ URL validation (valid and invalid URLs)
- ✅ QR code file generation
- ✅ Directory creation and error handling
- ✅ Logging configuration
- ✅ Exception handling in QR code generation
- ✅ Main function execution flow
- ✅ Command-line argument parsing

### Running Tests

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests with coverage report
pytest --cov=main --cov-report=term-missing -v

# Run tests with HTML coverage report
pytest --cov=main --cov-report=html -v
```

## GitHub Actions CI/CD Pipeline

### Automated Workflow Features:
- ✅ **Continuous Integration**: Automatic testing on push/PR to main branch
- ✅ **Multi-Python Support**: Tests against Python 3.10.12
- ✅ **Docker Integration**: Builds and pushes Docker images to DockerHub
- ✅ **Security Scanning**: Trivy security scanning for Docker images
- ✅ **Caching**: Optimized with dependency caching for faster builds
- ✅ **Multi-platform Support**: Linux AMD64 and ARM64 architectures

### Pipeline Stages:
1. **Test Stage**: Runs pytest with coverage requirements
2. **Build & Deploy**: Creates and pushes Docker images
3. **Security Check**: Scans for vulnerabilities

## Docker Usage

### Using Docker Compose (Recommended)

```bash
# Build and run with default URL
docker-compose up --build

# Run with custom URL
docker-compose run --rm qr_code_app --url https://www.example.com
```

### Using Docker Directly

```bash
# Build the image
docker build -t qr-code-generator .

# Run with custom URL
docker run -v $(pwd)/qr_codes:/app/qr_codes qr-code-generator --url https://www.google.com
```

## Environment Configuration

The application supports environment-based configuration:

- `QR_CODE_DIR`: Directory for saving QR codes (default: `qr_codes`)
- `FILL_COLOR`: QR code fill color (default: `red`)
- `BACK_COLOR`: QR code background color (default: `white`)

## Project Structure

```
├── main.py                 # Main application code
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker container configuration
├── docker-compose.yml     # Docker Compose setup
├── tests/
│   └── test_main.py       # Comprehensive test suite (98% coverage)
├── .github/
│   └── workflows/
│       └── tests.yml      # CI/CD pipeline configuration
├── qr_codes/              # Generated QR code output directory
└── readme.md              # This documentation
```

## Development Setup

### Local Development

```bash
# Clone the repository
git clone <repository-url>
cd module7_is601

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py --url https://www.example.com

# Run tests
pytest -v
```

## Quality Assurance

### Code Quality Metrics:
- ✅ **98% Test Coverage** (Target: 80% - Exceeded by 18%)
- ✅ **10 Comprehensive Test Cases**
- ✅ **Error Handling Coverage**
- ✅ **Exception Path Testing**
- ✅ **Integration Testing**

### Security Features:
- ✅ Non-root user in Docker container
- ✅ Automated security scanning with Trivy
- ✅ Input validation for URLs
- ✅ Secure file operations

## Achievements & Highlights

🎯 **Target Achievement**: Successfully exceeded 80% test coverage requirement, achieving **98% coverage**

🚀 **CI/CD Pipeline**: Implemented comprehensive GitHub Actions workflow with automated testing, Docker deployment, and security scanning

🔧 **Containerization**: Fully Dockerized application with multi-platform support and optimized build process

🧪 **Testing Excellence**: Comprehensive test suite covering all critical paths including error handling and edge cases

## Future Enhancements

- [ ] Add support for different QR code formats (SVG, PDF)
- [ ] Implement batch URL processing
- [ ] Add web interface for QR code generation
- [ ] Enhanced configuration options
- [ ] Performance metrics and monitoring
