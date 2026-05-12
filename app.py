from flask import Flask, render_template, request

app = Flask(__name__)

def classify_item(item):

    item = item.lower()

    if "plastic" in item:
        return "♻ Put this in the plastics recycling bin."

    elif "glass" in item:
        return "🍾 Dispose in the glass container."

    elif "metal" in item:
        return "🥫 Recycle with metals."

    elif "paper" in item or "cardboard" in item:
        return "📦 Recycle with paper/cardboard."

    else:
        return "✅ Try reusing this item before throwing it away."


@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        item = request.form["item"]

        result = classify_item(item)

    return render_template(
        "index.html",
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)