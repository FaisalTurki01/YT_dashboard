# 3blue1brown YouTube Analytics Dashboard

This Streamlit app provides an interactive dashboard for analyzing and visualizing YouTube channel statistics for the [3blue1brown](https://www.youtube.com/c/3blue1brown) channel. The app collects data using the YouTube API and performs data engineering to extract information about views, likes, comments, and upload date for each video on the channel.

## Usage

To start the app, run the following command in your terminal:


streamlit run app.py


This will launch the app in your default web browser. You can interact with the app by selecting different options from the sidebar on the left.

The app provides the following features:

- *Overview*: A summary of the channel's statistics, including the number of videos, total views, total likes, total comments, and average views per video.
- *Videos*: A  table of all the videos on the channel, with columns for the video title, upload date, views, likes, comments, and engagement.
- *Views over time*: A line chart showing the channel's views over time.
- *Top 5 videos by engagement*: A bar chart showing the Top 5 videos by engagement.
- *Performance Dashboard*: a Dashboard showing the changes on the channel over 6 months period.

## Contributing

Contributions are welcome! If you would like to contribute to the project, please follow these steps:

1. Fork the repository and clone it to your local machine.
2. Create a new branch for your changes: `git checkout -b my-new-branch`
3. Make your changes and commit them: `git commit -m "Add some feature"`
4. Push your changes to your fork: `git push origin my-new-branch`
5. Create a pull request from your fork to the `main` branch of the original repository.

Please make sure your code follows the PEP 8 style guide and includes unit tests where appropriate.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
