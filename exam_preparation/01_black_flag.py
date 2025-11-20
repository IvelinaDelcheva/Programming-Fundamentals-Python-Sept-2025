days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

total_plunder_gained = 0

for day in range(1, days + 1):
    total_plunder_gained += daily_plunder

    if day % 3 == 0:
        total_plunder_gained += daily_plunder * 0.5

    if day % 5 == 0:
        total_plunder_gained = total_plunder_gained * 0.7


if total_plunder_gained >= expected_plunder:
    print(f'Ahoy! {total_plunder_gained:.2f} plunder gained.')
else:
    print(f'Collected only {(total_plunder_gained * 100) / expected_plunder:.2f}% of the plunder.')
