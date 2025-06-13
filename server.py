import requests
from flask import Flask, request, jsonify
from readability import Document
from markdownify import markdownify as md

app = Flask(__name__)

@app.route('/simplify', methods=['POST'])
def simplify_article():
    data = request.get_json()
    if not data or 'url' not in data:
        return jsonify({"error": "URL not provided"}), 400

    url = data['url']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
    }

    try:
        print(f"1. Fetching article from: {url}")
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        print("2. Extracting clean article content using Readability...")
        doc = Document(response.text)

        article_title = doc.title()
        clean_html = doc.summary() 

        print(f"   -> Successfully extracted article: '{article_title}'")
        print("3. Converting clean HTML to Markdown using Markdownify...")
        markdown_content = md(clean_html, heading_style="ATX")
        final_output = f"# {article_title}\n\n{markdown_content}"

        print("\nSuccess! Article processed.")
        
        return jsonify({"simplified_text": final_output})

    except requests.exceptions.RequestException as e:
        print(f"\nError: Could not fetch the URL. Details: {e}")
        return jsonify({"error": f"Could not fetch the URL: {e}"}), 500
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        return jsonify({"error": f"An unexpected error occurred: {e}"}), 500

if __name__ == '__main__':
    # Runs on http://127.0.0.1:5000
    app.run(port=5000, debug=True)

