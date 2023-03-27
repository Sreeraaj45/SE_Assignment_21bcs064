import unittest
from unittest.mock import MagicMock
import mysql.connector

class TestSubmitForm(unittest.TestCase):

    def setUp(self):
        # Create a mock connection to use during testing
        self.conn = MagicMock(spec=mysql.connector.connection.MySQLConnection)
        mysql.connector.connect = MagicMock(return_value=self.conn)

        # Create a mock cursor to use during testing
        self.cur = MagicMock(spec=mysql.connector.cursor.MySQLCursor)
        self.conn.cursor = MagicMock(return_value=self.cur)

        # Create a dictionary to hold test data
        self.test_data = {
            'name': 'Test Artist',
            'art_type': 'Test Art Type',
            'description': 'Test Description'
        }

    def test_submit_form(self):
        # Call the submit_form function with test data
        submit_form(self.test_data['name'], self.test_data['art_type'], self.test_data['description'])

        # Check that the cursor executed the expected query with the expected parameters
        expected_query = "INSERT INTO artists (name, art_type, description) VALUES (%s, %s, %s)"
        expected_params = (self.test_data['name'], self.test_data['art_type'], self.test_data['description'])
        self.cur.execute.assert_called_once_with(expected_query, expected_params)

        # Check that the connection was committed
        self.conn.commit.assert_called_once()

        # Check that the success label was updated
        self.assertEqual(success_label.cget('text'), 'Form submitted successfully!')

if __name__ == '__main__':
    unittest.main()
