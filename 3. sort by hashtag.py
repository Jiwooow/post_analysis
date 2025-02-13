'''
This program sort the hashtagged images into different category folders.

'''



import os
import shutil
import re

# Paths
input_folder = "imgs/hormozi"  # Folder containing all influencer images
output_folder = "imgs/dataset"  # Base folder where hashtag folders will be created

# Hashtags to generate folders
text_prompts = [
    "FinanceMoney Tips", "Business Advice", "Online Business",
    "Systems", "Personal Development", "Productivity Tips", "Education"
]

# Normalize hashtags: Replace spaces with underscores and convert to lowercase
normalized_hashtags = {
    f"#{hashtag.lower().replace(' ', '_')}": hashtag.replace(" ", "_")
    for hashtag in text_prompts
}


# Create folders for each hashtag
for normalized, folder_name in normalized_hashtags.items():
    hashtag_folder = os.path.join(output_folder, folder_name)
    if not os.path.exists(hashtag_folder):
        os.makedirs(hashtag_folder)

# Function to sort files into folders named after hashtags
def sort_files_by_hashtags():
    for file in os.listdir(input_folder):
        if file.endswith(('.jpg', '.jpeg', '.png')):  # Check for image files
            file_path = os.path.join(input_folder, file)
            
            # Extract hashtag from the filename
            match = re.search(r"#\w+", file)
            if match:
                file_hashtag = match.group(0).lower()  # Normalize hashtag to lowercase
                
                # Check if the extracted hashtag matches any of the normalized hashtags
                if file_hashtag in normalized_hashtags:
                    target_folder = os.path.join(output_folder, normalized_hashtags[file_hashtag])
                    shutil.move(file_path, os.path.join(target_folder, file))
                    print(f"Moved {file} to {target_folder}")
                else:
                    print(f"No matching folder for hashtag: {file_hashtag} in file: {file}")
            else:
                print(f"No hashtag found in file: {file}")

# Run the sorting function
sort_files_by_hashtags()