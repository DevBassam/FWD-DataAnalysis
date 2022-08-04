import pandas as pd
import numby as np
import time

CITY_DATA = {'ch':'chicago.csv', 'ny':'new_york_city.csv', 'wa':'washington.csv'}
months_list = ['January', 'February', 'March', 'April', 'May', 'June']
days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
def get_filters():
    print('***** You are using Bike Share Programe *****')
    print('***************** Welcom *******************')
    print(' ')
    print("Let's begin......:) ")
    print('-'*25)
    # get user input for city (chicago, new york city, washington)
    while True:
        city = input('Please, Choose a city to show its data....["ch" for chicago, "ny" for New York, "wa" for Washington]').lower()
        if city in CITY_DATA: break
        else: print('Invalid Choice, Please try again...')

    # Select which filter that user want...
    filter_list = ['month', 'day', 'both', 'none']
    while True:
        filter = input('Which filter U want to select...[month, day, both, none]..?').lower()
        if filter in filter_list: break
        else: print('Invalid Choice, Sorry try again :(')

    # get user input for filter by  month , day or both
    if filter == 'month' or filter == 'both':
        while True:
            month = input('Please, Select a month...[January, February, March, April, May, June]').title()
            if month in months_list: break
            else: print('Ivalid Choice...Select anthor one, Please')

    if filter == 'day' or filter == 'both':
        while True:
            day = input('Please, Select a day...[Friday, Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday]').title()
            if day in days_list: break
            else: print('Invalid Choice, Plesae try again....')

    if filter == 'none':
        month = 'all'
        day = 'all'
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        month = months_list.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month = df['month'].mode()[0]
    print('The most common month is: {}'.format(months_list[month-1]))

    # display the most common day of week
    day = df['day_of_week'].mode()[0]
    print('The most common day of week is: {}'.format(day))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common start hour is: {}'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most station used to start trips is: {}'.format(common_start_station))

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most station used at the end of trips is: {}'.format(common_end_station))

    # display most frequent combination of start station and end station trip
    common_trip = df['Start Station'] + ' to ' + df['End Station']
    print('The most common route is: {}'.format(popular_trip.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_duration = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).sum()
    days =  total_travel_duration.days
    hours = total_travel_duration.seconds // (60*60)
    minutes = total_travel_duration.seconds % (60*60) // 60
    seconds = total_travel_duration.seconds % (60*60) % 60
    print(f'Total travel time is: {days} days {hours} hours {minutes} minutes {seconds} seconds')

    # display mean travel time
    average_travel_duration = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).mean()
    days =  average_travel_duration.days
    hours = average_travel_duration.seconds // (60*60)
    minutes = average_travel_duration.seconds % (60*60) // 60
    seconds = average_travel_duration.seconds % (60*60) % 60
    print(f'Average travel time is: {days} days {hours} hours {minutes} minutes {seconds} seconds')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # display counts of user types
    print(df['User Type'].value_counts())

    # display counts of gender
    if 'Gender' in(df.columns):
        print(df['Gender'].value_counts())

    # display earliest, most recent, and most common year of birth
    if 'Birth Year' in(df.columns):
        year = df['Birth Year'].fillna(0).astype('int64')
        print('Earliest birth year is: {}'.format(year.min()))
        print('The most recent is: {}'.format(year.max()))
        print('The most comon birth year is:{}'.format(year.mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Ask the user if he wants to display the raw data and print 5 rows at time"""
    raw = input('Would you like to diplay 5 rows of data?\n')
    if raw.lower() == 'yes':
        count = 0
        while True:
            print(df.iloc[count: count+5])
            count += 5
            ask = input('Do U want to show the next 5 rows.....?')
            if ask.lower() != 'yes':
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
