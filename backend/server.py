# from llama_index import SimpleChatEngine
from llama_index.core.chat_engine import SimpleChatEngine
# from llama_index.llms import Gemini
from llama_index.llms.gemini import Gemini

# from llama_index import ServiceContext
from llama_index.core import ServiceContext
# from llama_index.embeddings import GeminiEmbedding
# imports
# from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import Settings


from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

GAK = os.getenv("GEMINI_API")

llm = Gemini(api_key=GAK)
embed_model = GeminiEmbedding(model_name="models/embedding-001", api_key=GAK)



Settings.llm = llm
Settings.embed_model = embed_model


# service_context = ServiceContext.from_defaults(
#     llm=llm,
#     embed_model=embed_model
# )


from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

 
# chat_engine = SimpleChatEngine.from_defaults(service_context=service_context)
chat_engine = SimpleChatEngine.from_defaults(settings=Settings)




    # Route for handling chat requests
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    prompt = data["prompt"]
    if prompt:
        prompt = data['prompt']
        response = jsonify(chat_engine.chat(prompt))
        response_data = response.get_json()
        if response_data:
            response_data = remove_asterisks(response_data)
            response = jsonify(response_data)
        return response
    # Handle other data inputs as needed
    return jsonify({"error": "Invalid request."})

# Route for deleting chat history
@app.route("/chat", methods=["DELETE"])
def delete():
    chat_engine.clear_chat()
    return jsonify({"message": "Chat history deleted."})

# Route for handling favicon request (returns empty response)
@app.route('/favicon.ico')
def favicon():
    return ''

# Route for handling root URL (returns a welcome message)
@app.route('/')
def index():
    return 'Welcome to the Career Compass Chat API!'

# Function to remove asterisks from response
def remove_asterisks(response):
    if isinstance(response, dict):
        return {key: remove_asterisks(value) for key, value in response.items()}
    elif isinstance(response, list):
        return [remove_asterisks(item) for item in response]
    elif isinstance(response, str):
        return response.replace("*", "")
    else:
        return response

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
