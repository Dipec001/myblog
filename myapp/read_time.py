def calculate_reading_time(content, average_speed=200):
    # Counting words
    word_count = len(content.split())

    # Calculate estimated reading time
    estimated_time = word_count / average_speed  # minutes

    return estimated_time
