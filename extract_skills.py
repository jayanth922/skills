import torch
from transformers import DistilBertTokenizer, DistilBertForTokenClassification

# Initialize model and tokenizer
def initialize_model(model_path, num_labels=2):
    tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
    model = DistilBertForTokenClassification.from_pretrained(
        'distilbert-base-uncased',
        num_labels=num_labels
    )
    model.load_state_dict(torch.load(model_path))
    model.eval()
    return model, tokenizer

# Global model and tokenizer
model, tokenizer = initialize_model("model_final.pt")

def extract_skills_from_job(job):
    """Extract skills from a single job description."""
    description = job.get("description", "")
    if not description.strip():
        print("DEBUG: Empty job description found!")
        return []

    try:
        # Tokenize input
        inputs = tokenizer(
            description,
            truncation=True,
            padding='max_length',
            max_length=512,
            return_tensors='pt'
        )
        
        # Get predictions
        with torch.no_grad():
            outputs = model(**inputs)
            predictions = torch.argmax(outputs.logits, dim=2)
        
        # Convert predictions to skills
        tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])
        skills = []
        current_skill = []
        
        for token, pred in zip(tokens, predictions[0]):
            if pred == 1:
                if token.startswith('##'):
                    current_skill.append(token[2:])
                else:
                    if current_skill:
                        skills.append(''.join(current_skill))
                        current_skill = []
                    current_skill.append(token)
        
        if current_skill:
            skills.append(''.join(current_skill))
            
        return skills
        
    except Exception as e:
        print(f"DEBUG: Error processing job description: {e}")
        return []

def extract_skills_from_jobs(jobs):
    """Extract skills from a list of job descriptions."""
    all_skills = []
    for job in jobs:
        description = job.get("description", "")
        if not description.strip():
            print("DEBUG: Skipping job with empty description.")
            continue
        all_skills.extend(extract_skills_from_job(job))
    return all_skills
