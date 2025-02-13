## post_analysis

# Instagram Thumbnail Downloader & AI Hashtagging System #

This project automates the process of downloading Instagram post thumbnails, analyzing them using AI-powered hashtag detection, and sorting them into categorized folders based on the content. It’s an ideal tool for content creators, social media managers, and marketers who need organized visuals for reference, reposting, or inspiration.

## ✨ Features ##

✅ Automated Instagram Thumbnail Download – Fetches post thumbnails from Instagram automatically.
✅ AI-Based Hashtag Generation – Uses machine learning to analyze images and suggest relevant hashtags.
✅ Automatic Sorting – Categorizes images into folders based on detected content themes.
✅ Bulk Processing – Works with multiple Instagram posts efficiently.

## 🚀 How to Use ##

1️⃣ Install Dependencies
Ensure you have Python installed, then install the required packages:

  pip install -r requirements.txt

2️⃣ Install ChromeDriver
Since Selenium is used for automation, you need ChromeDriver installed and compatible with your Chrome version.
* Download it from: ChromeDriver Downloads
* Place it in your system PATH or inside the project folder.

3️⃣ Set Up the Script
Place your target Instagram post URLs in a file (e.g., input_urls.txt).
Run the script to start downloading and categorizing thumbnails.

4️⃣ Run the Program
  python main.py

The script will:

  * Download the thumbnails from Instagram using Selenium.
  * Analyze the images using AI.
  * Assign relevant hashtags.
  * Sort them into categorized folders.

📂 Folder Structure
After running the script, your files will be organized like this:
```
  /sorted_thumbnails/
     ├── travel/
     ├── food/
     ├── fashion/
     ├── fitness/
     ├── tech/
     └── misc/
```

Each folder contains images that match the category.

## ⚙️ Customization ##

You can modify:

Categories: Add/remove categories based on your needs.
Hashtagging Model: Train the AI model for better accuracy.
File Naming Rules: Customize file names for better organization.

## 📌 Notes ##

This script does not bypass Instagram’s security policies. It only downloads publicly accessible images.
You may need to log in or use API-based methods for private accounts.

## 🛠️ Future Enhancements ##

🔹 Improve hashtag accuracy with a more advanced AI model.
🔹 Add support for video thumbnails.
🔹 Implement a web-based interface for easier use.

## 🤝 Contributions ##
Feel free to submit pull requests to improve this tool!
Let me know if you'd like any changes! 🚀
