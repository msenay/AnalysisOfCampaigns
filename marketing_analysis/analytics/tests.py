from django.test import SimpleTestCase
from rest_framework.test import APIClient
from rest_framework import status


class CampaignAnalysisTests(SimpleTestCase):
    """
    Test cases for the Campaign Analysis API endpoints.
    These tests are designed to ensure that the API endpoints return the correct
    data structures and HTTP status codes without requiring a database.
    """

    def setUp(self):
        """
        Set up the API client to be used in all test cases.
        This client simulates requests to the API endpoints.
        """
        self.client = APIClient()

    def test_conversion_rate(self):
        """
        Test the /api/conversion-rate/ endpoint.

        This test checks that:
        - The endpoint returns a 200 OK status.
        - The response includes 'conversion_rates', 'highest', and 'lowest' keys.
        - The data contains non-empty conversion rates.
        """
        response = self.client.get('/api/conversion-rate/')
        # Ensure the response status is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Parse the JSON response
        data = response.json()

        # Ensure necessary keys are in the response
        self.assertIn("conversion_rates", data)
        self.assertIn("highest", data)
        self.assertIn("lowest", data)

        # Check that the conversion rates are not empty
        self.assertGreater(len(data["conversion_rates"]), 0)
        self.assertIsInstance(data["highest"], dict)
        self.assertIsInstance(data["lowest"], dict)

    def test_status_distribution(self):
        """
        Test the /api/status-distribution/ endpoint.

        This test checks that:
        - The endpoint returns a 200 OK status.
        - The response contains 'status_distribution' and 'total_status_analysis'.
        - The response data for status distribution is non-empty.
        """
        response = self.client.get('/api/status-distribution/')
        # Ensure the response status is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Parse the JSON response
        data = response.json()

        # Ensure necessary keys are in the response
        self.assertIn("status_distribution", data)
        self.assertIn("total_status_analysis", data)

        # Check that the status distribution data is not empty
        self.assertGreater(len(data["status_distribution"]), 0)
        self.assertGreater(len(data["total_status_analysis"]), 0)

    def test_category_type_performance(self):
        """
        Test the /api/category-type-performance/ endpoint.

        This test checks that:
        - The endpoint returns a 200 OK status.
        - The response includes 'performance' and 'top_performance' keys.
        - The response data for category-type performance is non-empty.
        """
        response = self.client.get('/api/category-type-performance/')
        # Ensure the response status is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Parse the JSON response
        data = response.json()

        # Ensure necessary keys are in the response
        self.assertIn("performance", data)
        self.assertIn("top_performance", data)

        # Check that the performance data is not empty
        self.assertGreater(len(data["performance"]), 0)
        self.assertIsInstance(data["top_performance"], dict)

    def test_filtered_aggregation(self):
        """
        Test the /api/filtered-aggregation/ endpoint.

        This test checks that:
        - The endpoint returns a 200 OK status.
        - The response contains the expected keys for revenue and conversions.
        - The response data is a list and contains non-empty entries.
        """
        response = self.client.get('/api/filtered-aggregation/')
        # Ensure the response status is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Parse the JSON response
        data = response.json()

        # Ensure the response data is not empty and is a list
        self.assertGreater(len(data), 0)
        self.assertIsInstance(data, list)

        # Ensure the keys 'avg_revenue' and 'avg_conversions' are in the first entry
        self.assertIn("avg_revenue", data[0])
        self.assertIn("avg_conversions", data[0])
