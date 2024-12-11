from transformers import AutoTokenizer
from sentence_transformers import SentenceTransformer


model_name = "sentence-transformers/all-MiniLM-L6-v2"
tokenizer = AutoTokenizer.from_pretrained(model_name)

tokenizer.save_pretrained(r"C:\Users\DELL\application\novelHack\backend\Navy\Navy\model\tokenizer")

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

model.save(r"C:\Users\DELL\application\novelHack\backend\Navy\Navy\model\embeddding_model")

