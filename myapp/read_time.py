import math

def calculate_reading_time(content, average_speed=200):
    # Counting words
    word_count = len(content.split())

    # Calculate estimated reading time and round up to the nearest whole number
    rounded_time = math.ceil(word_count / average_speed)

    return rounded_time
