import sys
import os
import shutil
from pathlib import Path
from unittest.mock import patch, MagicMock
import logging

import pytest
sys.path.append(str(Path(__file__).resolve().parents[1]))

from main import create_directory, generate_qr_code, is_valid_url, QR_DIRECTORY, setup_logging, main


@pytest.fixture(scope="function")
def temp_qr_dir(tmp_path):
    """Fixture to create and clean up a temporary QR directory."""
    qr_dir = tmp_path / QR_DIRECTORY
    qr_dir.mkdir(parents=True, exist_ok=True)
    yield qr_dir
    shutil.rmtree(tmp_path, ignore_errors=True)


def test_create_directory(temp_qr_dir):
    """Ensure directory creation works."""
    test_dir = temp_qr_dir / "new_folder"
    create_directory(test_dir)
    assert test_dir.exists() and test_dir.is_dir()


def test_valid_url():
    """Test that a valid URL passes validation."""
    assert is_valid_url("https://www.google.com") is True


def test_invalid_url(caplog):
    """Test that invalid URLs are caught."""
    result = is_valid_url("invalid-url")
    assert result is False
    assert any("Invalid URL" in msg for msg in caplog.messages)


def test_generate_qr_code_creates_file(temp_qr_dir):
    """Test that QR code image file is generated successfully."""
    qr_file = temp_qr_dir / "test_qr.png"
    generate_qr_code("https://example.com", qr_file)
    assert qr_file.exists() and qr_file.stat().st_size > 0


def test_generate_qr_code_invalid_url(temp_qr_dir):
    """Test that invalid URL does not create a file."""
    qr_file = temp_qr_dir / "invalid_qr.png"
    generate_qr_code("invalid-url", qr_file)
    assert not qr_file.exists()


def test_setup_logging():
    """Test that setup_logging configures logging correctly."""
    with patch('logging.basicConfig') as mock_basic_config:
        setup_logging()
        mock_basic_config.assert_called_once()
        args, kwargs = mock_basic_config.call_args
        assert kwargs['level'] == logging.INFO
        assert 'format' in kwargs
        assert 'handlers' in kwargs


def test_create_directory_exception(temp_qr_dir, caplog):
    """Test create_directory exception handling."""
    with patch('pathlib.Path.mkdir', side_effect=PermissionError("Permission denied")):
        with pytest.raises(SystemExit):
            create_directory(temp_qr_dir / "test")
        assert any("Failed to create directory" in msg for msg in caplog.messages)


def test_generate_qr_code_exception(temp_qr_dir, caplog):
    """Test generate_qr_code exception handling during QR code creation."""
    qr_file = temp_qr_dir / "test_qr.png"
    
    # Mock qrcode.QRCode to raise an exception
    with patch('qrcode.QRCode', side_effect=Exception("QR code creation error")):
        generate_qr_code("https://example.com", qr_file)
        assert any("An error occurred while generating or saving the QR code" in msg for msg in caplog.messages)


@patch('sys.argv', ['main.py', '--url', 'https://test.com'])
def test_main_function(temp_qr_dir):
    """Test the main function execution."""
    with patch('main.Path.cwd') as mock_cwd, \
         patch('main.create_directory') as mock_create_dir, \
         patch('main.generate_qr_code') as mock_generate_qr, \
         patch('main.setup_logging') as mock_setup_logging:
        
        mock_cwd.return_value = temp_qr_dir.parent
        main()
        
        mock_setup_logging.assert_called_once()
        mock_create_dir.assert_called_once()
        mock_generate_qr.assert_called_once()


@patch('sys.argv', ['main.py'])  
def test_main_with_default_url(temp_qr_dir):
    """Test main function with default URL argument."""
    with patch('main.Path.cwd') as mock_cwd, \
         patch('main.create_directory') as mock_create_dir, \
         patch('main.generate_qr_code') as mock_generate_qr, \
         patch('main.setup_logging') as mock_setup_logging:
        
        mock_cwd.return_value = temp_qr_dir.parent
        main()
        
        # Verify all functions were called
        mock_setup_logging.assert_called_once()
        mock_create_dir.assert_called_once()
        mock_generate_qr.assert_called_once()
        
        # Check that generate_qr_code was called with default URL
        args, kwargs = mock_generate_qr.call_args
        assert args[0] == 'https://github.com/kaw393939'  # default URL
