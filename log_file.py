#Log file Analyzer

from collections import Counter
import re

def analyze_log(file_path):
    log_levels = Counter()
    error_messages = Counter()
    total_lines = 0

    # Pattern to detect log levels
    level_pattern = re.compile(r'\b(INFO|DEBUG|WARNING|ERROR|CRITICAL)\b')

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            total_lines += 1

            # Count log levels
            match = level_pattern.search(line)
            if match:
                log_levels[match.group()] += 1

            # Store error messages
            if "ERROR" in line or "CRITICAL" in line:
                error_messages[line.strip()] += 1

    print("=" * 50)
    print("LOG FILE ANALYSIS REPORT")
    print("=" * 50)
    print(f"Total Log Entries: {total_lines}\n")

    print("Log Level Counts:")
    for level, count in log_levels.items():
        print(f"  {level:<10}: {count}")

    print("\nTop Error Messages:")
    if error_messages:
        for msg, count in error_messages.most_common(10):
            print(f"({count} times) {msg}")
    else:
        print("No errors found.")

    print("=" * 50)


if __name__ == "__main__":
    file_path = input("Enter log file path: ")
    analyze_log(file_path)
    
    
#nano app.log
#ls
#python3 log_file.py
#app.log