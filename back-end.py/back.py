courses = [
    ["Motion Design After Effects", 300],
    ["Illustrator Creative Branding", 225],
    ["Photoshop Visual Storytelling", 150],
    ["Web Design Soul", 100],
    ["Color Theory & Personal Expression", 200]
]

TAX = 0.15

def calculate_price(choice):
    if 1 <= choice <= len(courses):
        name, price = courses[choice - 1]
        total = price * (1 + TAX)
        print(f"\nSelected: {name}")
        print(f"Base price: {price} SAR")
        print(f"With tax: {total:.2f} SAR")
    else:
        print("Error: number out of range.")

# Show courses
for i, (name, price) in enumerate(courses, start=1):
    print(f"{i}. {name} || Price: {price} SAR")

# Run
choice = int(input("\nEnter course number: "))
calculate_price(choice)