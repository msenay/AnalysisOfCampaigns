from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd

# Load the dataset from a URL as a Pandas DataFrame
df = pd.read_csv('https://file.notion.so/f/f/0beb2d6a-43bc-4a08-b9c4-f7eb5da236b4/756ba9f3-c325-4b2f-8e11-f1f3e18c9d19/mockupinterviewdata.csv?table=block&id=bdaf1547-5f80-4252-a4bd-0e1abb8ae9b2&spaceId=0beb2d6a-43bc-4a08-b9c4-f7eb5da236b4&expirationTimestamp=1725732000000&signature=XN_rp8z4BOcBsROqz_NQpKwZrQauMo-dMiJebiUMHIg&downloadName=mockupinterviewdata.csv')


@api_view(['GET'])
def conversion_rate(request):
    """
    Calculate and return the conversion rate for each customer.

    The conversion rate is calculated as the ratio of conversions to revenue.
    The response includes:
    - The conversion rate for each customer_id.
    - The customer with the highest conversion rate.
    - The customer with the lowest conversion rate.
    """
    # Calculate the conversion rate
    df['conversion_rate'] = df['conversions'] / df['revenue']

    # Create a list of conversion rates for each customer
    conversion_rates = df[['customer_id', 'conversion_rate']].to_dict('records')

    # Find the customer with the highest and lowest conversion rates
    highest = df.loc[df['conversion_rate'].idxmax()].to_dict()
    lowest = df.loc[df['conversion_rate'].idxmin()].to_dict()

    # Return the response as JSON
    return Response({
        "conversion_rates": conversion_rates,
        "highest": highest,
        "lowest": lowest
    })


@api_view(['GET'])
def status_distribution(request):
    """
    Analyze and return the distribution of statuses across different types and categories.

    The response includes:
    - A breakdown of total revenue, total conversions, and the count of customer IDs for each combination of status, type, and category.
    - An overall summary of total revenue and conversions for each status.
    """
    # Group data by status, type, and category, and calculate aggregated sums
    status_data = df.groupby(['status', 'type', 'category']).agg(
        total_revenue=('revenue', 'sum'),
        total_conversions=('conversions', 'sum'),
        count=('customer_id', 'count')
    ).reset_index().to_dict('records')

    # Group data by status and calculate overall revenue and conversions for each status
    total_status = df.groupby('status').agg(
        total_revenue=('revenue', 'sum'),
        total_conversions=('conversions', 'sum')
    ).reset_index().to_dict('records')

    # Return the response as JSON
    return Response({
        "status_distribution": status_data,
        "total_status_analysis": total_status
    })


@api_view(['GET'])
def category_type_performance(request):
    """
    Calculate and return the performance of each category and type combination.

    The response includes:
    - Total revenue and total conversions for each combination of category and type.
    - The category and type combination with the highest conversions.
    """
    # Group data by category and type, and calculate total revenue and conversions
    performance_data = df.groupby(['category', 'type']).agg(
        total_revenue=('revenue', 'sum'),
        total_conversions=('conversions', 'sum')
    ).reset_index().to_dict('records')

    # Find the category and type combination with the highest conversions
    top_performance = df.groupby(['category', 'type']).agg(
        total_conversions=('conversions', 'sum')
    ).reset_index().sort_values(by='total_conversions', ascending=False).iloc[0].to_dict()

    # Return the response as JSON
    return Response({
        "performance": performance_data,
        "top_performance": top_performance
    })


@api_view(['GET'])
def filtered_aggregation(request):
    """
    Filter the data for type = 'CONVERSION' and return aggregated averages.

    The response includes:
    - Average revenue and average conversions for each customer where type is 'CONVERSION'.
    """
    # Filter data where type is 'CONVERSION' and group by customer_id
    conversion_data = df[df['type'] == 'CONVERSION'].groupby('customer_id').agg(
        avg_revenue=('revenue', 'mean'),
        avg_conversions=('conversions', 'mean')
    ).reset_index().to_dict('records')

    # Return the response as JSON
    return Response(conversion_data)
