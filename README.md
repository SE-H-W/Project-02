# CityByte Project 2

[![Test](https://github.com/rohitgeddam/CityByte/actions/workflows/django.yml/badge.svg)](https://github.com/rohitgeddam/CityByte/actions/workflows/django.yml)
[![codecov](https://codecov.io/gh/rohitgeddam/FindMyRoomie/branch/main/graph/badge.svg?token=PCOHJETYCD)](https://codecov.io/gh/rohitgeddam/FindMyRoomie)
![Code Size](https://img.shields.io/github/languages/code-size/SE-H-W/Project-02)
![Repo Size](https://img.shields.io/github/repo-size/SE-H-W/Project-02)
[![DOI](https://zenodo.org/badge/877602165.svg)](https://doi.org/10.5281/zenodo.14027838)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![GitHub issues](https://img.shields.io/github/issues/SE-H-W/Project-02)
![GitHub issues-closed](https://img.shields.io/github/issues-closed/SE-H-W/Project-02)
[![GitHub version](https://img.shields.io/github/v/release/rohitgeddam/CityByte)](https://github.com/SE-H-W/Project-02/releases)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


## Introduction
New and improved! Several new features and bug fixes were implemented to show significant improvement from Project 1.

Below are the new features and improvements we made:
1. Itinerary Creation: Users can build personalized itineraries for their trips by specifying the number of travel days, making CityByte a complete travel planner.
2. City-Specific News Page: Real-time updates on local news for each searched city, keeping users informed about events and current affairs.
3. Google Maps Integration: Each displayed spot is clickable, opening the location directly in Google Maps in a new tab, enhancing ease of use.
4. Forgot Password Feature: Improved account management with secure recovery options, ensuring smooth access to user accounts.
5. UI Enhancements: The interface is redesigned for an intuitive, visually appealing experience, making it easier for users to navigate the platform. 

## New Project
Below is the video and the changes or features we added
[<img width="1447" alt="Screenshot 2024-11-02 at 12 23 26 PM" src="https://github.com/user-attachments/assets/90a4c2b2-a7ab-4ec7-ab9d-7ac674a08c64">](https://youtu.be/an7c3hxpj3A)

[<img width="1458" alt="image" src="https://github.com/user-attachments/assets/05b3aeaf-a412-4a9f-ac42-25f1ed13f26c">](https://drive.google.com/file/d/1cxWi9nhs5HRcJ6IL6EqB4kh6kklEubK8/view?usp=drive_link)

## Old Project - In Brief
Below is the old projects:

https://drive.google.com/file/d/1sUewnnTpuXX3s8nMnpnR0WZhVM-c8L1a/view?usp=sharing

## Architecture
![2](https://user-images.githubusercontent.com/53405794/205814790-7c3f2cdc-59dc-47b6-92df-bddd8c5208df.png)

## Improvements
Improvements can be seen in the follwing load testing reportsusing the LocustIO:

### Before Caching Implementation:
100 concurrent users:
![Before_cache_100](https://user-images.githubusercontent.com/53405794/205815400-ea00d406-acef-48d5-a0b8-dd2e71da6a73.png)  
1000 concurrent users:
![Before_cache_1000](https://user-images.githubusercontent.com/53405794/205815413-6821c1e6-dc03-41da-8ed8-70267a6becbd.png)
10000 concurrent users:
![before_cache_10000](https://user-images.githubusercontent.com/53405794/205815417-a3adc3c8-2e8b-4c41-b854-fc78b781b4eb.png)

### After Caching Implementation:  
100 concurrent users:
![After_cache_100](https://user-images.githubusercontent.com/53405794/205815892-82ff37e1-0b33-45e9-bc62-967293a77848.png)

1000 concurrent users:
![Afte_cache_1000](https://user-images.githubusercontent.com/53405794/205815903-aa5d0252-af46-4ae1-be78-162be476c09c.png)

10000 concurrent users:
![after_cache_10000](https://user-images.githubusercontent.com/53405794/205815928-0610629a-3c4f-4763-b2c7-3f67fad26530.png)

Results:  
* For 10000 concurrent users, before caching there was failure when the test was performed, but for the caching scenario, the mean response time was 46000 ms. 
* For 1000 concurrent users, before caching there was mean response time of 48000 ms when the test was performed, but for the caching scenario, the mean response time was 10000 ms.

## Quick Start

#### 1. Clone the repository:  

   `[git clone https://github.com/rohitgeddam/CityByte.git](https://github.com/SE-H-W/Project-02.git)`

#### 2. Setup the virtual environment:  
    
`
    python -m venv venv
`


#### 3. Activate the virtual environment:  

    On Mac/Linux:    

`
      source venv/bin/activate
`
      
    On Windows:    
    
`
      venv\Scripts\activate
`
   

#### 4. Install required modules and libraries:  

`
    pip install -r requirements.txt
`


#### 5. Create .env file at ./CityByte using the below template.
   
```
    GEODB_X_RAPID_API_KEY=""
    GEODB_X_RAPID_API_HOST=""
    AMADEUS_API_KEY=""
    AMADEUS_API_SECRET_KEY=""
    UNSPLASH_API_KEY=""
    FOURSQUARE_API_KEY=""
    WEATHER_BIT_X_RAPID_API_KEY=""
    WEATHER_BIT_X_RAPID_API_HOST=""
    NEWSAPI_KEY=""
    GOOGLE_GEMINI_API=""
```
Create an account in the below websites to Fetch API keys and use them in the above template.  
* [GeoDB Cities API](https://rapidapi.com/wirefreethought/api/geodb-cities/details)
* [Weather API](https://rapidapi.com/weatherbit/api/weather)
* [Amadeus API](https://developers.amadeus.com/)
* [Unsplash API](https://unsplash.com/developers)
* [Foursquare API](https://location.foursquare.com/developer/)
* [Google Gemini API](https://ai.google.dev/gemini-api?gad_source=1&gclid=CjwKCAjw-JG5BhBZEiwAt7JR6xbYStbhA4cIvBvOPV2aUgrqJP37xjoj4M6G8qO8ltx6w85IYaCSTBoC0cYQAvD_BwE)
* [News API](https://newsapi.org/)

#### 6. Set-up REDIS
* Follow the instructions in [Getting Started](https://redis.io/docs/getting-started/) to Install Redis in your local environment.
* Start the Redis Server: Open a terminal and run the following command:
```
   redis-server
```
* Open another terminal to start the REDIS CLI:
```
   redis-cli
```

Now, you can run the application.
#### 7. Run the application:  
   
   ``` 
   python manage.py migrate
   python manage.py runserver
   ```
  
## After adding another field to Model
Django's way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema.

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

## Automatic tools - GitHub Actions
 
We use GitHub actions to automate tasks of linting, code coverage, build, tests, and security checks. The codes that perform these actions are stored as `.yml` files in the `.github/workflows` directory. The GitHub actions are triggered whenever something is pushed (or pulled) into the remote repository. The results of these automated tasks are shown as badges at the top of this README.md file. 

### Unit tests:

Unit test are performed everytime there is a push or pull into the repository. They are present in `/search/tests.py`. 

### Code Coverage: 

Code Coverage is an important metric that allows us to understand how much of the codebase is tested. `django.yml` performs this task. For more information about Code Coverage, please visit this [link](https://www.atlassian.com/continuous-delivery/software-testing/code-coverage). 

### Flake8 - Code Linting:

We are using Flake8 for linting and syntax checking, and it is performed by `Linting.yml`. For more information about Flake8, please visit this [link](https://medium.com/python-pandemonium/what-is-flake8-and-why-we-should-use-it-b89bd78073f2).
Use flake8 before you push code to GitHub. </br>
Config file present in `.flake8`.

```
flake8 <directory>
```

### Black - Code Formatter

We are using the Black code formatter to format our code before pushing it to GitHub. For more information about Black, please visit this [link](https://black.readthedocs.io/en/stable/).
Config file in `pyproject.toml`.

Run the line below everytime you push to GitHub.</br>
```
black --line-length 120 <filename>
```

If you prefer using Black in VSCode, you can add the below settings in your vscode settings:

```
{
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": ["--line-length", "120"],
    "python.linting.enabled": true
}
```
  
### Pre Commit Hooks for Black Code formatting and Flake8 Linting
* run  `pre-commit install`
* Now everytime you commit, Black and Flake8 will run automatically and will not allow you to push if the code standards are not met.
<img width="694" alt="Screenshot 2022-10-07 at 11 35 40 AM" src="https://user-images.githubusercontent.com/48797475/194592802-e7d7c951-9694-4260-b537-fc017a5fd06c.png">

<sub>Image from [Ji Miranda](https://ljvmiranda921.github.io/assets/png/tuts/precommit_pipeline.png).<sub>

## License
Distributed under the MIT License. See `LICENSE` for more information


## Support
Concerns with the software? Please get in touch with us via one of the methods below. We are delighted to address any queries you may have about the program.

Please contact us if you experience any problems with the program, such as problems with joining up, logging in, or any other functions.

<a href = "mailto:aramanu3@ncsu.edu">
<img width = "35px" src = "https://user-images.githubusercontent.com/73664200/194786335-12b1d3a6-b272-4896-9bd7-d615e28847f3.png"/>
</a>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

#Team Members
1. Ashwini Ramanuj: aramanu3@ncsu.edu
2. Nirmit Patel: naptel37@ncsu.edu
3. Kahaan Patel: kaptel48@ncsu.edu

# CityByte Project 1

[![DOI](https://zenodo.org/badge/541612969.svg)](https://zenodo.org/badge/latestdoi/541612969) ![](https://img.shields.io/github/license/therealppk/CityByte) ![](https://img.shields.io/github/issues/therealppk/CityByte?style=plastic) ![](https://img.shields.io/github/issues-closed-raw/therealppk/CityByte?style=plastic) ![](https://img.shields.io/github/languages/code-size/therealppk/CityByte?style=plastic) ![](https://img.shields.io/github/contributors/therealppk/CityByte?style=plastic) [![Django CI](https://github.com/therealppk/CityByte/actions/workflows/django.yml/badge.svg)](https://github.com/therealppk/CityByte/actions/workflows/django.yml)
[![codecov](https://codecov.io/gh/therealppk/CityByte/branch/main/graph/badge.svg?token=HRK9X7OI2J)](https://codecov.io/gh/therealppk/CityByte)
![](https://github.com/therealppk/CityByte/blob/main/docs/assets/code_coverage.png)


<p align="center">
  <img src="https://github.com/therealppk/citybytesrough/blob/main/CityBytes.gif" alt="animated" />
</p>

## Introduction
Moving to a new location can be a daunting endeavor, especially when you have the entire world to choose from. Finding a new home from scratch while prioritizing certain aspects might be very challenging given the variety of nations and cities. However, with the advancement of technology, information from earlier times can now be leveraged to offer a number of vital insights about a certain location. Our project succeeds in one of those objectives. We seek to present that information in our project because there are many other elements that are taken into consideration when choosing a place to reside, such as weather, temperature, entertainment options, landmark locations, education, and many more. The project is totally created using a variety of technologies, including some of the accessible APIs that are utilized to fetch real-time data.

Although this project is still in its early phases of development, it can be expanded up even further by including multiple features that can benefit society in a variety of different ways. This article offers a critical viewpoint that users can use to comprehend the project, adopt it as open source software, and add further features before releasing it to the market. The document also serves as a starting point for the project and helps developers understand the code.

The technologies listed below were used to build the entire project, and it is advised that the group of developers who take on this project in the future retain these tools on hand:

* Python3
* Django
* Pytest
* HTML
* CSS
* JavaScript
* BootStrap

Although we have used HTML, CSS and Bootstrap for the frontend logic the user can use any technologies and combine it with backend such as Angular, React etc.

## Team Members
1. Rohit Geddam: sgeddam2@ncsu.edu
2. Arun Kumar Ramesh - arames25@ncsu.edu
3. Kiron Jayesh - kjayesh@ncsu.edu
4. Sai Krishna Teja Varma - smanthe@ncsu.edu
5. Shandler Mason - samason4@ncsu.edu
