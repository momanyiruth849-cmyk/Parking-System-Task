from flask import Flask

app = Flask(__name__)

slots = []
for i in range(1, 21):
    slots.append({
        "slot_number": i,
        "is_occupied": False
    })

# Mark a few as occupied so the display isn't all green
slots[2]["is_occupied"] = True
slots[5]["is_occupied"] = True
slots[9]["is_occupied"] = True

def slot_grid_html():
    html = ""
    for slot in slots:
        color = "occupied" if slot["is_occupied"] else "free"
        html += f'<div class="slot {color}">{slot["slot_number"]}</div>'
    return html

@app.route("/")
def home():
    available = sum(1 for s in slots if not s["is_occupied"])
    return f"""
    <html><head><title>Parking System</title>
    <style>
    body {{ font-family: Arial; text-align: center; background: #f4f4f4; padding: 20px; }}
    .grid {{ display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; max-width: 500px; margin: 20px auto; }}
    .slot {{ padding: 20px 0; border-radius: 8px; color: white; font-weight: bold; }}
    .free {{ background-color: #2ecc71; }}
    .occupied {{ background-color: #e74c3c; }}
    </style></head>
    <body>
    <h1>Parking System</h1>
    <p>Available slots: {available} out of 20</p>
    <div class="grid">{slot_grid_html()}</div>
    <p>Green = Available &nbsp;&nbsp; Red = Occupied</p>
    </body></html>
    """

if __name__ == "__main__":
    app.run(debug=True)
    