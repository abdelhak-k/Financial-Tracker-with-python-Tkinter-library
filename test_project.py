import pytest
from project import load_data, write_data, append_data

SAMPLE_DATA={'card': 100, 'savings': 200, 'cash': 300, 'expense': 50}

def test_load_data_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_data("non_existent_file.csv")

def test_write_data(tmp_path):
    file_path = tmp_path / "test_write_data.csv"
    write_data(SAMPLE_DATA, file_path)
    assert file_path.exists()

def test_append_data(tmp_path):
    file_path = tmp_path / "test_append_data.csv"
    write_data(SAMPLE_DATA, file_path)
    new_entry = {'Datetime': '2024-04-15 14:30:00', 'Transaction': 'Deposited $50 to card'}
    append_data(new_entry, file_path)
    assert file_path.exists()
