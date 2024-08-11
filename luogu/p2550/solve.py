#!/usr/bin/env python3
def lottery_result():
    # Read the number of tickets
    n = int(input())
    
    # Read the winning numbers
    winning_numbers = set(map(int, input().split()))
    
    # Initialize a list to hold the count for each prize level
    prize_counts = [0] * 7  # [特等奖, 一等奖, 二等奖, 三等奖, 四等奖, 五等奖, 六等奖]
    
    # Process each ticket
    for _ in range(n):
        ticket_numbers = set(map(int, input().split()))
        # Calculate the number of matching numbers
        match_count = len(ticket_numbers & winning_numbers)
        # Update the corresponding prize count
        if match_count > 0:  # Only count matches of at least 1 number
            prize_counts[7 - match_count] += 1
    
    # Output the results
    print(" ".join(map(str, prize_counts)))

# Example usage:
lottery_result()

