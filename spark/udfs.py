from pyspark.sql.functions import udf
from pyspark.sql.types import DoubleType

# Define a UDF to calculate the percentage difference
percent_diff_udf = udf(
    lambda new_value, old_value: round(((new_value - old_value) / old_value) * 100, 0) if old_value != 0 else None,
    DoubleType())
