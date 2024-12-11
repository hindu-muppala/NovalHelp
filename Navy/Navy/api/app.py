# app.py
from flask import Flask, render_template, request, jsonify
from sentence_transformers import SentenceTransformer
from model.rag import query_logs

# set up the model
log_path = r'C:\Users\DELL\application\novelHack\backend\Navy\novelHack_Data\novelHack\maritime-dataset-surveillance-logs_01-15.md'
app = Flask(__name__)


#tokenizer = AutoTokenizer.from_pretrained(r"C:\Users\DELL\application\novelHack\backend\Navy\Navy\model\tokenizer")
model = SentenceTransformer(r"C:\Users\DELL\application\novelHack\backend\Navy\Navy\model\embeddding_model")
@app.route('/')
def map_view():
    # Data to be passed to the template
    data = [
        {
            "time": "2024-10-25T12:00:00Z",
            "latitude": 37.7749,
            "longitude": -122.4194,
            "text": "San Francisco",
            "object": "Location A"
        },
        {
            "time": "2024-10-25T15:30:00Z",
            "latitude": 34.0522,
            "longitude": -118.2437,
            "text": "Los Angeles",
            "object": "Location B"
        },
    ]
    return render_template('map.html', data=data)

@app.route('/log')
def get_log():

    query = "report"

    return query_logs(log_path, query, model)

@app.route('/logCustom')  
def get_logcustom():
    query = request.args.get('query')
    return query_logs(log_path, query, model)
    
    

if __name__ == '__main__':
    app.run(debug=True)
