scores = [85, 42, 65, 90, 72]

for s in scores:
    if s < 60:
        print(f"Score: {s},Grade: F")
    elif s < 70:
        print(f"Score: {s},Grade: C")
    elif s < 80:
        print(f"Score: {s},Grade: B")
    elif s >= 80:
        print(f"Score: {s},Grade: A")