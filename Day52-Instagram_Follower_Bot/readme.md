# 100 Days of Code: Day 52 - Instagram Follower Bot

## Project Overview
**Date:** 09/23/2024

**Goal:** 
Today, I built an Instagram follower bot that takes a similar account as input and automatically follows all the people that the input account is following.

## Project Details
### 1. Technologies Used
- **Programming Language:** Python
- **Libraries/Frameworks:** Selenium
- **Tools:** WebDriver, Instagram

### 2. Day Overview 
#### Instagram Follower Bot
- **Automating Instagram Actions**: The bot was designed to log into my Instagram account, identify a similar account, and follow all the people that the specified account follows. The goal was to grow my follower base by targeting people with similar interests.

#### Setting Up the Bot
- **Selenium for Web Automation**:
  - I used Selenium to automate logging into Instagram, navigating to the target account, and extracting the list of accounts that it follows.
  - The bot then iterates over the list and automatically follows each account.

- **Challenges with Instagram Security**:
  - Instagram has strict security measures in place, so I had to ensure that the bot could handle potential CAPTCHA challenges and login security checks. This was done using Selenium to interact with the web elements directly.

- **Customizable Features**:
  - The bot allows for customization of the target account, making it easy to choose different accounts to follow people from.
  - There’s also a delay function to prevent Instagram from detecting the bot due to too many actions in a short time.

### 3. Challenges and Learning
- **Challenges Faced**:
  - Instagram’s rate limits and security measures presented a challenge. To avoid getting flagged, I had to introduce random delays between actions.
  - Managing the login process securely, including handling two-factor authentication, required additional logic in the bot.

### 4. Final Project - Instagram Follower Bot

For the final project of today, I created a bot that can automatically follow users from a similar Instagram account. The bot can now run without manual intervention and is designed to respect Instagram’s limits to avoid account suspension.

#### Objective
The objective of this project was to automate a process for growing an Instagram following by identifying and following users who follow a similar account. The bot is customizable and can target various accounts as needed.


### 5. Tomato Count

Today's lessons and project took [🍅🍅🍅🍅]
