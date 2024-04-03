# test_formatColumn.py
import pytest
import pandas as pd
from dataframe_formatter.formatColumn import formatColumn
def test_formatColumn_valid_values():
    # Create a sample DataFrame
    data = {'Name': ['John Doe', 'Jane Smith', 'Mike Johnson'],
            'Type': ['SUV', 'Convertible', 'Sedan']}
    df = pd.DataFrame(data)

    # Define valid values for the 'Type' column
    valid_types = ['SUV', 'Convertible', 'Sedan']

    # Format the 'Type' column
    formatted_df = formatColumn(df, 'Type', valid_types)

    # Assert that the 'Type' column only contains valid values
    assert all(value in valid_types for value in formatted_df['Type'])

def test_formatColumn_invalid_values():
    # Create a sample DataFrame with invalid values
    data = {'Name': ['John Doe', 'Jane Smith', 'Mike Johnson'],
            'Type': ['SUV', 'Convertible', 'InvalidType']}
    df = pd.DataFrame(data)

    # Define valid values for the 'Type' column
    valid_types = ['SUV', 'Convertible', 'Sedan']

    # Format the 'Type' column
    formatted_df = formatColumn(df, 'Type', valid_types)

    # Assert that the 'Type' column contains only valid or corrected values
    assert all(value in valid_types for value in formatted_df['Type'] if pd.notna(value))

if __name__ == '__main__':
    pytest.main()