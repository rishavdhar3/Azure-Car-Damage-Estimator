# Azure-Car-Damage-Estimator
This is a web application that uses AI-powered computer vision and language models to analyze images of car damage and provide detailed repair assessments and cost estimates. Users can upload photos of vehicle damage and receive a comprehensive damage report generated using Azure Cognitive Services and GPT.

---

Features
- **Image-Based Damage Analysis**: Upload clear photos of damaged vehicles for automatic detection and classification of dents, scratches, broken parts, and more.
- **AI-Powered Damage Report**: Azure OpenAI (GPT-4) generates a detailed natural language report describing the damage and recommended repairs based on Computer Vision results.
- **Cost Estimation**: The app estimates approximate repair costs using AI-driven heuristics and industry-standard repair pricing models.
- **User-Friendly Interface**: Clean and modern React frontend with intuitive image upload, real-time analysis feedback, and report display.

---

How It Works

**Frontend (React + Tailwind CSS)**

- Users upload damage photos through a responsive interface.
- The image is sent to the backend for analysis.
- The app displays the generated damage report and estimated repair costs.


**Backend (FastAPI)**

- Receives uploaded images and sends them to Azure Computer Vision API for damage detection.
- Parses and extracts damage features, then passes them to Azure OpenAI GPT-4 for detailed explanation and cost estimation.
- Returns the structured report back to the frontend.

---

**Prerequisites and Running the App**

- Python 3.10+
- Node.js 18+
- Azure subscription with Computer Vision and OpenAI GPT access keys
- Environment variables configured with your Azure keys (see .env.example)

Run the provided start_app.bat script to launch both frontend and backend servers locally.

---
