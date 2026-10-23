
a = input("Enter status of Room A (Dirty/Clean): ").lower()
b = input("Enter status of Room B (Dirty/Clean): ").lower()
pos = input("Enter vacuum position (A/B): ").upper()

if pos == "A":
    if a == "dirty":
        print("Clean Room A")
        a = "clean"
    if b == "dirty":
        print("Move to Room B")
        print("Clean Room B")
        b = "clean"
else:
    if b == "dirty":
        print("Clean Room B")
        b = "clean"
    if a == "dirty":
        print("Move to Room A")
        print("Clean Room A")
        a = "clean"

print("Final status:", a, b)
