# 100 Days of Code: Day 45 - Web Scraping with Beautiful Soup

## Project Overview
**Date:** 8/27/2024

**Goal:** 
Today, I learned about web scraping, particularly using the Beautiful Soup module in Python, which helps developers extract and parse information from websites, especially when an API is not available.

## Project Details
### 1. Technologies Used
- **Programming Language:** Python
- **Libraries/Frameworks:** Beautiful Soup
- **Tools:** PyCharm

### 2. Day Overview 
#### Introduction to Web Scraping
- **Web Scraping**: The process of extracting data from websites by parsing the underlying HTML code. This is particularly useful when a website does not provide an API for data access.

#### Using Beautiful Soup
- **Beautiful Soup**: A Python library that facilitates the extraction of data from HTML and XML files. It parses the HTML content, allowing developers to navigate the document tree and extract relevant data.

- **Basic Operations**:
  - **Parsing HTML**: I learned how to open an HTML file, read its contents, and parse it using Beautiful Soup's `html.parser`.
  - **Extracting Elements**: Various HTML elements such as titles, paragraphs, and lists can be extracted using Beautiful Soup. For example:
    - `soup.title` retrieves the title element.
    - `soup.a`, `soup.li`, and `soup.p` can be used to extract the first anchor, list item, and paragraph elements, respectively.
    - The `soup.prettify()` method is useful for printing the HTML in a more readable format.

- **CSS Selectors in Beautiful Soup**:
  - I explored how to use CSS selectors within Beautiful Soup to target specific elements:
    - **Selecting elements/tags**: `soup.select_one(selector="p a")` selects a specific element within a tag.
    - **Selecting by ID**: `soup.select_one("#name")` selects an element by its ID.
    - **Selecting by class**: `soup.select(".heading")` selects elements with a specific class.

#### Scraping a Live Website
- **Scraping Process**:
  - I practiced scraping data from a live website, specifically Hacker News. The steps included:
    - Sending a GET request to the website URL to retrieve the HTML content.
    - Parsing the HTML content with Beautiful Soup.
    - Extracting the first article’s title, link, and upvotes by targeting specific HTML tags and attributes.
    - Identifying the article with the highest number of upvotes and printing its details.

#### Legal and Ethical Considerations of Web Scraping
- **Legal Aspects**:
  - The legality of web scraping can be complex. A notable case was hiQ's legal battle with LinkedIn, where hiQ was allowed to scrape publicly available data.
  - Generally, scraping publicly available and non-copyrighted data is legal. However, scraping behind authentication or scraping for commercial purposes can be legally sensitive.

- **Ethical Practices**:
  - **Use Public APIs First**: Always prioritize using official APIs if available.
  - **Respect the Website Owner**: Avoid overwhelming a website with requests that could cause it to crash. Respect the guidelines outlined in the `robots.txt` file, which specifies which parts of the site should not be accessed by bots.
  - **User-Agent and Crawl Delay**: Adhere to the crawl delay specified in `robots.txt` and limit the scraping frequency to avoid overloading the server.


### 3. Challenges and Learning
- **Challenges Faced:**  
  - Today took me a little extra time because the HTML code underlying the Hacker News webpage has changed since the course was released. The anchor tags I was trying to scrape did not have a class anymore. I needed to use regular expressions to select for the specific anchor tags.

### 4. Final Project - Scraping and Reordering the 100 Best Movies List

For the final project, I focused on web scraping, specifically targeting the list of the 100 best movies according to Empire News. The goal was to extract the movie titles and reorder them based on specific criteria.

#### Project Overview
- **Website Scraping**: I used Beautiful Soup, a Python library, to scrape the movie titles from the Empire News website. This involved navigating the HTML structure of the webpage, identifying the elements that contained the movie titles, and extracting that data.

- **Data Extraction**:
  - **Beautiful Soup**: I parsed the HTML content using Beautiful Soup, which allowed me to easily locate and extract the movie titles from the list. The extracted data was then processed for further analysis.

- **Reordering the List**:
  - After scraping the movie titles, I reordered the list based on my chosen criteria. This could involve alphabetically sorting the titles, ranking them by release year, or any other custom order depending on the project's requirements.

#### Objective
The objective of this project was to demonstrate proficiency in web scraping techniques using Beautiful Soup, and to apply those skills in manipulating and reordering data scraped from a live website. The result was a newly ordered list of the top 100 movies, which could then be used for further analysis or presentation.


### 5. Screenshots 

![image](https://github.com/user-attachments/assets/5fa2cdfd-da0f-4495-8574-4828fde6bc9c)

### 6. Tomato Count

Today's lessons and projects took [🍅🍅🍅🍅][🍅🍅🍅🍅]

