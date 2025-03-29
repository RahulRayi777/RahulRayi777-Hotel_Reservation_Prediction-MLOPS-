# 🔥 Line-by-Line Explanation with Example
dockerfile

FROM python:slim
🎯 Example:
Imagine you want to bake a cake.
You need a basic kitchen → This is the kitchen setup.
Here, we are saying:
"Start with a small, clean Python kitchen (slim version) to cook."

dockerfile
Copy
Edit
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
🎯 Example:
You tell your kitchen helper: "Don’t write extra messy files (.pyc), and whatever you cook, show me immediately."

dockerfile
Copy
Edit
WORKDIR /app
🎯 Example:
"Work inside the /app folder."
Like telling the helper:
"Go to the kitchen room, not the living room."

dockerfile
Copy
Edit
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
🎯 Example:
You tell your helper:
"Before cooking, go to the market, buy one important ingredient libgomp1, clean up after shopping, and don’t bring extra items."
This file is needed by LightGBM (which is like an important tool in your kitchen).

dockerfile
.
🎯 Example:
"Bring all your recipe books & ingredients from your home (your project folder) to the kitchen (container)."

dockerfile

RUN pip install --no-cache-dir -e .
🎯 Example:
"Read the recipe book (requirements.txt) and bring all the spices, flour, sugar (Python packages)."
pip install installs all required libraries.

dockerfile

RUN python pipeline/training_pipeline.py
🎯 Example:
"Before serving food, bake the cake."
Here, you are training your Machine Learning model so that it's ready to use when your app runs.

dockerfile
Copy
Edit
EXPOSE 5000
🎯 Example:
"Open the kitchen door at Gate No. 5000, so customers (users) can come in."
You are opening port 5000 because your Flask app will run there.

dockerfile
Copy
Edit
CMD ["python", "application.py"]
🎯 Example:
"Finally, start serving the cake (start your app)."
This command says:
"When the container starts, run the application.py file and start the server"

  