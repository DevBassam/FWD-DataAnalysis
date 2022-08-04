# Overview
In this project, you will make use of Python to explore data related to bike share systems for three major cities in the United States—Chicago,
New York City, and Washington. You will write code to import the data and answer interesting questions about it by computing descriptive statistics.
You will also write a script that takes in raw input to create an interactive experience in the terminal to present these statistics.

# Project Details
## Bike Share Data:
  Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world.
  Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, 
  though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

  Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles.
  These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

  In this project, you will use data provided by Motivate, a bike share system provider for many major cities in the United States, 
  to uncover bike share usage patterns. You will compare the system usage between three large cities: Chicago, New York City, and Washington, DC.

## The Datasets:
  Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

  1. Start Time (e.g., 2017-01-01 00:07:57)
  2. End Time (e.g., 2017-01-01 00:20:53)
  3. Trip Duration (in seconds - e.g., 776)
  4. Start Station (e.g., Broadway & Barry Ave)
  5. End Station (e.g., Sedgwick St & North Ave)
  6. User Type (Subscriber or Customer)
  
  The Chicago and New York City files also have the following two columns:

  1. Gender
  2. Birth Year
  ![nyc-data](https://user-images.githubusercontent.com/84365449/182884314-311a1124-0443-4f47-bdf0-6cb6aabd53b3.png)

  The original files are much larger and messier, and you don't need to download them, but they can be accessed here if you'd like to see them (Chicago, New York City,
  Washington). These files had more columns and they differed in format in many cases.
  Some data wrangling has been performed to condense these files to the above core six columns to make your analysis and
  the evaluation of your Python skills more straightforward. In the Data Wrangling course that comes later in the Data Analyst Nanodegree program, 
  students learn how to wrangle the dirtiest, messiest datasets, so don't worry, you won't miss out on learning this important skill!
  
## Statistics Computed
  You will learn about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics. In this project,
  you'll write code to provide the following information:

1. Popular times of travel (i.e., occurs most often in the start time)
   <ul>
     <li>most common month
     <li>most common day of week
     <li>most common hour of day
   </ul>

2. Popular stations and trip
   <ul>
    <li> most common start station
    <li> most common end station
    <li>most common trip from start to end (i.e., most frequent combination of start station and end station)
   </ul>
3. Trip duration
  <ul>
    <li>total travel time
    <li>average travel time
  </ul>
 
4. User info
   <ul>
    <li>counts of each user type
    <li>counts of each gender (only available for NYC and Chicago)
    <li>earliest, most recent, most common year of birth (only available for NYC and Chicago)
   </ul>
  
## The Files
  To answer these questions using Python, you will need to write a Python script. To help guide your work in this project,
  a template with helper code and comments is provided in a bikeshare.py file, and you will do your scripting in there also. 
  You will need the three city dataset files too:
  1. chicago.csv
  2. new_york_city.csv
  3. washington.csv
  
All four of these files are zipped up in the Bikeshare file in the resource tab in the sidebar on the left side of this page. 
You may download and open up that zip file to do your project work on your local machine.

Some versions of this project also include a Project Workspace page in the classroom where the bikeshare.py file and the city dataset files are all included,
and you can do all your work with them there.
