Social Media Data Analysis Project
----------------------------------

1. Install the required Python modules:
   pip install -r requirements.txt

2. Set up API credentials:
   - Create a `.env` file in the root directory.
   - Add your API keys/tokens:
     TWITTER_BEARER_TOKEN=your_bearer_token
     INSTAGRAM_ACCESS_TOKEN=your_access_token
     FACEBOOK_ACCESS_TOKEN=your_access_token

3. Run the project:
   python main.py

4. Outputs:
   - Fetched data will be saved in the `data/` folder.
   - Sentiment analysis and top tags/users will be saved in the `outputs/` folder.
   - Visualizations will be saved in the `visuals/` folder.
