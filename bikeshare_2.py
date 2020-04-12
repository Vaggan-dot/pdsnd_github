import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city', 'washington']
    while True:
        city = input('Would you like to see data for Chicago, New York City or Washington?' ).lower()
        if city in cities:
            break
        else :
            print("Oh, we don't have data for the city you asked for. Please try again.")

    # get user input for month (all, january, february, ... , june)

    months = ['january','february','march','april', 'may','june','all']
    while True:
        month = input('Which month? January, February, March, April, May, June.').lower()
        if month in months:
            break
        else :
            print("Oh, we don't have data for the city you asked for. Please try again.")



    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = input('Last question! Which day are you interested in? You can choose to see data for all days by typing all.').lower()
        if day in days:
            break
        else :
            print("Oh, we don't have any data for the city you asked for. Please try again.")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    #load csv files

    #extract month & day
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    #search for how to filter DataFrame
    if month != 'all' :
        month_index = df['month'] == month
        df = df[month_index]

    if day != 'all' :
        day_index = df['day_of_week'] == day.title()
        df = df[day_index]

        #find a function that returns day of week in string, not number

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print(df['month'])

    # display the most common month
    most_common_month = df['month'].value_counts().index[0]
    print("The most common month is: ", most_common_month)

    # display the most common day of week
    most_common_day = df['day_of_week'].value_counts().index[0]
    print("The most common day is: ", most_common_day)

    # display the most common start hour
    most_common_hour = df['hour'].value_counts().index[0]
    print("The most common hour is: ", most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().index[0]
    print("The most commonly used start station is: ", most_common_start_station)

    # display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().index[0]
    print("The most commonly used end station is: ", most_common_end_station)

    # display most frequent combination of start station and end station trip
    df['route'] = df['End Station'] + '-' + df['Start Station']
    print(df['route'].value_counts().index[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time :", total_travel)


    # display mean travel time
    total_travel = df['Trip Duration'].mean()
    print("Total travel time :", total_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_counts = df['User Type'].value_counts()
    print("Counts of user types:", user_counts)

    if city == 'washington' :
        print('Apologies we don\'t have gender and birth year data for Washington.')
    else :
        gender_counts = df['Gender'].value_counts()
        print("Counts of gender:", gender_counts)

        # Display earliest, most recent, and most common year of birth
        birth_year = df['Birth Year']

        most_common_year = birth_year.value_counts().index[0]
        print("The most common birth year:", most_common_year)

        most_recent = birth_year.max()
        print("The most recent birth year:", most_recent)

        earliest_year = birth_year.min()
        print("The most earliest birth year:", earliest_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:

        city, month, day = get_filters()
        df = load_data(city, month, day)


        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)


        count = 0
        display = input('Would you like to see the first 5 rows of the data? Please write Yes or no.')
        while display != 'no' :
            print(df.iloc[count : count + 5])
            count = count + 5
            display = input('Would you like to see the next 5 rows of the data? Please write Yes or no.')

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
             break

if __name__ == "__main__":
	main()
