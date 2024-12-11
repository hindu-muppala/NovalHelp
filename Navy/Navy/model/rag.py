
import faiss
import re
import numpy as np


def query_logs(path, query, model):

    surv_ = []
    a = []
    with open(path) as file:
        for line in file:
            y = line.strip()
            if y == "```":
                if a == []:
                    a.append('')
                else:
                    surv_.append(''.join(a[2:]))
                    a = []
            else:
                a.append(line.strip() +' ')

    embeddings = model.encode(surv_)
    embedding_dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(embedding_dim)
    index.add(np.array(embeddings))

    query_text = query
    query_embedding = model.encode([query_text])
    distances, indices = index.search(np.array(query_embedding), 10)
    
    threshold_distance = distances[0][0]  

    threshold_distance = threshold_distance*(1.1)
    k = sum(d <= threshold_distance for d in distances[0])  
 
    result = []
    pattern = r"Date:\s*(.*?)\s*Time:\s*(.*?)\s*Location:\s*(.*?)\s*Report:\s*(.*)"

# Find all matches in the input string

    c = 0
 

    for i, idx in enumerate(indices[0]):
       match = re.search(pattern, surv_[idx], re.DOTALL)
       if match:
        date = match.group(1).strip()
        time = match.group(2).strip()
        location = match.group(3).strip()
        report = match.group(4).strip()
        result.append(
            {
                'Date': date,
                'Time': time,
                'Location':location,
                'Report': report
            }

        )
        c += 1
        if c==k:
            break
    
    
    return result