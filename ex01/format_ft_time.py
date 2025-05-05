import time 
from datetime import datetime
def main():

    current = time.time()

    formatted_scds = f"{current:,.4f}"

    scientific_notation = f"{current:.2e}"

    month_day = datetime.now().strftime("%b %-d %Y")

    print(f"Seconds since January 1, 1970: {formatted_scds} or {scientific_notation} in scientific notation")
    print(f"{month_day}")
if __name__ == "__main__":
    main()
