from src.data_cleaning import clean_price

def test_clean_price():
    assert clean_price("$100") == 100.0
    assert clean_price("$1,000") == 1000.0
    assert clean_price(None) == 0.0