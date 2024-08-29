# 100 Days of Code: Day 46 - Time Travel Spotify Playlist

## Project Overview
**Date:** 8/28/2024

**Goal:** 
Today, I developed a program that allows users to create a "time travel" Spotify playlist based on a specific date by scraping the top 100 songs from the Billboard Hot 100 and then creating a Spotify playlist using the Spotify API.

## Project Details
### 1. Technologies Used
- **Programming Language:** Python
- **Libraries/Frameworks:** Beautiful Soup, Spotify API (Spotipy)
- **Tools:** PyCharm

### 2. Day Overview 
#### Input Date
- **User Input:** The user inputs a date of their choice, which represents the time they want to "travel" to in terms of music.

#### Web Scraping Billboard Hot 100
- **Scraping Process:** The program uses web scraping techniques to extract the top 100 songs from the Billboard Hot 100 chart for the specified date. This involves retrieving the song titles and artists from the Billboard website.

#### Spotify API Integration
- **Playlist Creation:** After gathering the top 100 songs, the program uses the Spotify API to search for each song on Spotify and then compiles them into a new playlist. This playlist is automatically created in the user's Spotify account, allowing them to listen to the top hits from any specific week in history.

### 3. Challenges and Learning
- **Challenges Faced:**  
  - One challenge I encountered was ensuring that each song could be found on Spotify, as not all songs from past decades may be available in the Spotify library. I had to implement error handling to manage cases where a song could not be found.

### 4. Final Project - Time Travel Spotify Playlist

For the final project, I focused on combining web scraping with API integration to create a dynamic and personalized Spotify playlist that reflects the top 100 songs from any given date.

#### Project Overview
- **Web Scraping Billboard Hot 100:** The program scrapes the top 100 songs from Billboard Hot 100 for the given date. The scraped data includes song titles and artists.
  
- **Spotify API Integration:** The program then uses the Spotify API to create a new playlist in the user's account, adding the top 100 songs from the chosen date.

#### Objective
The objective of this project was to create a fun and nostalgic experience by allowing users to explore and enjoy the music from any point in time, all packaged into a Spotify playlist.

### 5. Screenshots 

![image](https://github.com/user-attachments/assets/c7b83b29-a2e4-4fc6-b77e-1b8d3d361cd9)


### 6. Tomato Count

Today's lessons and projects took [🍅🍅🍅🍅][🍅🍅]
