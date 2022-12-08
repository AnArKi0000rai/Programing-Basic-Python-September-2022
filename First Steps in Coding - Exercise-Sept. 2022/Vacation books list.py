count_sheets = int(input())
count_sheets_per_hour = int(input())
count_days_for_reading = int(input())

total_count_pages_for_reading = count_sheets / count_sheets_per_hour

total_hours_for_reading = total_count_pages_for_reading // count_days_for_reading

print(total_hours_for_reading)
