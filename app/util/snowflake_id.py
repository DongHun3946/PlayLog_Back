from snowflake import SnowflakeGenerator


def generate_snowflake_id():
    gen = SnowflakeGenerator(1)
    new_id = next(gen)

    return new_id
