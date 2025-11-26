from flask import Flask, request, jsonify
from rag import retrieve_chunk
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    print("Received data:", data)  # Debug print

    question = data.get("question")
    if not question:
        print("❌ No question received")
        return jsonify({"error": "Missing question"}), 400

    print("📥 Processing question:", question)

    retrieved_chunks = retrieve_chunk(question)

    parsed_results = []
    for chunk in retrieved_chunks:
        try:
            lines = chunk.split("\n")
            parsed_results.append({
            "title": lines[0].replace("Title :", "").strip(),
            "type": lines[1].replace("Type :", "").strip(),
            "provider": lines[2].replace("Provider:", "").strip(),
            "topics": lines[3].replace("Topics:", "").strip().split(", "),
            "summary": lines[4].replace("Summary:", "").strip(),
            "link": lines[5].replace("Link:", "").strip()
        })
        except Exception as e :
            print("Error parsing chunk :", e)
    print("Parsed results:", parsed_results)  # debug
    return jsonify({"answer": parsed_results})
if __name__ == "__main__":
    app.run(debug=True)