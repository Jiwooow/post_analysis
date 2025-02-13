'''
This is a program renames the images by AI analyzing.

'''

import os
from transformers import CLIPProcessor, CLIPModel
from PIL import Image


###### Load the CLIP model#########
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Define potential hashtag prompts
text_prompts = [
    "FinanceMoney Tips", "Business Advice", "Online Business",
    "Systems", "Personal Development", "Productivity Tips", "Education"
]

# Analyze the image
def generate_hashtags(image_path, text_prompts):
    
    image = Image.open(image_path)

    # Process the image and text
    inputs = processor(text=text_prompts, images=image, return_tensors="pt", padding=True)
    outputs = model(**inputs)

    # Get similarity scores and find the best match
    probs = outputs.logits_per_image.softmax(dim=1)
    max_idx = probs.argmax()
    hashtags = [f"#{text_prompts[max_idx].replace(' ', '_').lower()}"]

    return hashtags


folder_path = "imgs/CodieSanchez/"

for count, filename in enumerate(os.listdir(folder_path), start=1):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(folder_path, filename)

        try:
            if "_" in filename:
                prefix, _ = filename.split("_", 1)  # Split only once at the first '_'

                # Generate new hashtags
                hashtags = generate_hashtags(image_path, text_prompts)
                new_tag = "_".join(hashtags)

                # Create the new filename
                new_filename = f"{prefix}_{new_tag}{os.path.splitext(filename)[1]}"
                new_path = os.path.join(folder_path, new_filename)

                # Rename the file
                os.rename(image_path, new_path)
                #print(f"Renamed: {filename} -> {new_filename}")
            
            else:
                # Generate hashtags for the image
                hashtags = generate_hashtags(image_path, text_prompts)
                hashtag_str = "_".join(hashtags)

                # Create the new filename
                new_filename = f"{os.path.splitext(filename)[0]}_{hashtag_str}{os.path.splitext(filename)[1]}"
                new_path = os.path.join(folder_path, new_filename)

                # Rename the file
                os.rename(image_path, new_path)
                #print(f"Renamed: {filename} -> {new_filename}")

        except Exception as e:
            print(f"Error processing {filename}: {e}")