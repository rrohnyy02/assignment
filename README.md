# Web Application: Audio Analysis Tool

This web application utilizes Flask, Deepgram API, and OpenAI to analyze audio files in MP3 format. It offers several features to extract valuable insights from the audio content.

## Features:


### 1. Transcription with Diarization:
   - Utilizes Deepgram API for transcription.
   - Incorporates OpenAI to refine the transcription and provide accurate diarization (speaker identification).

### 2. Summary Generation:
   - Generates concise summaries based on the audio content.

### 3. Psychoanalysis:
   - Provides psychological insights for each speaker, offering an understanding of their traits and nature beyond the content's mere summary.

### 4. Ratings:
   - Presents graphical representations of ratings assigned to each speaker based on:
     - Trust
     - Empathy
     - Optimism
     - Courage
     - Charisma

### 5. Speaker Insights (Beta):
   - Provides insights into individual speakers' likes and dislikes.
   - Currently in beta stage, undergoing refinement.

## How to Use:

1. **Visit the following link:**

    -  [Audio Analysis Tool](https://rrohnyy02.pythonanywhere.com/)

2. **Upload Audio File (MP3 Only):**
   - Choose an MP3 file containing the audio content you wish to analyze.

3. **Select Desired Analysis:**
   - Choose from transcription, summary, psychoanalysis, ratings, or speaker insights.

4. **View Results:**
   - Receive detailed insights based on the selected analysis.

## Usage Instructions:

1. **Installation:**
   - Clone the [repository](https://github.com/rrohnyy02/assignment.git).
   - Install dependencies using `pip install -r requirements.txt`.

2. **Configuration:**
   - Set up Deepgram API credentials by placing api key in `.env` file.
        `Open_AI_API_KEY = your Open AI api key`

   - Ensure access to OpenAI API by placing open ai api key in `.env` file.
        `Deepgram_Token = your deepgram api key`
   

3. **Run Application:**
   - Execute `python3 app.py` to start the Flask server.

4. **Access the Web Interface:**
   - Navigate to the provided localhost address in your web browser.



## Challenges Faced:

1. **Diarization Accuracy:**
   - Deepgram API's diarization feature did not provide accurate speaker identification, leading to the need for an alternative solution.
   - Resolving this issue required exploring different options, ultimately leading to the integration of OpenAI for diarization.

2. **Hosting Limitations:**
   - Inaccessibility to Google Cloud Platform (GCP) due to issues with bank card acceptance posed challenges in hosting the website.
   - Leveraging PythonAnywhere.com for hosting was the alternative solution adopted to overcome this limitation.

3. **Response Quality from OpenAI:**
   - Obtaining accurate and reliable responses from OpenAI required significant experimentation and prompting.
   - Despite efforts to refine the prompts and adjust parameters, ensuring consistent and dependable responses remained a challenge.

4. **Variability in ChatGPT Responses:**
   - ChatGPT's responses exhibited considerable variability, making it challenging to predict and ensure consistent output.
   - Adjustments to parameters like temperature were made to mitigate this issue, but uncertainty in response quality persisted.

5. **Overall Integration Complexity:**
   - Integrating multiple APIs and services, each with its own nuances and limitations, added complexity to the development process.
   - Ensuring seamless interaction and consistent performance across these integrated components posed ongoing challenges throughout the project.


## Contributors:

- Rohan Khandelwal
- rohan.khandelwal1431@gmail.com





