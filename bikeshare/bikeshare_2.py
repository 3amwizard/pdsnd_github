import time
import pandas as pd
import numpy as np
# it seems we didn't need numpy for this bit of code but it here as the template included it
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
    print('Hello! Let\'s explore some US bikeshare data!\n')
    day = 'all'
    month = 'all'
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = str(input('Please enter a city, chicago, new york city or washington:\n').casefold())
    while city not in ('chicago', 'new york city', 'washington'):
        print('please enter a valid city name as listed')
        city = str(input('Please enter a city, chicago, new york city or washington:\n').casefold())

    # get user input for month (all, january, february, ... , june)
    check = str(input('Would you like to filter by day, month or both?\n').casefold())
    while check not in ('month', 'day', 'both'):
        check = str(input('Would you like to filter by day, month or both?').casefold())

    if check == 'both':
        month = str(input('Please enter a date january, february, march, april, may, june:\n').casefold())
        while month not in ('january, february, march, april, may, june'):
            print('please enter a valid month')
            month = str(input('Please enter a date january, february, march, april, may, june:\n').casefold())

    # get user input for day of week (all, monday, tuesday, ... sunday)
        day = str(input('Please enter a day of the week, sunday, monday, tuesday, wednesday, thursday, friday, saturday:\n').casefold())
        while day not in ('sunday, monday, tuesday, wednesday, thursday, friday, saturday'):
            print('please enter a valid day')
            day = str(input('Please enter a day of the week, sunday, monday, tuesday, wednesday, thursday, friday, saturday:\n').casefold())


    elif check == 'month':
        month = str(input('Please enter a date january, february, march, april, may, june:\n').casefold())
        while month not in ('january, february, march, april, may, june'):
            print('please enter a valid month')
            month = str(input('Please enter a date january, february, march, april, may, june:\n').casefold())

    else:
        day = str(input('Please enter a day of the week, sunday, monday, tuesday, wednesday, thursday, friday, saturday:\n').casefold())
        while day not in ('sunday, monday, tuesday, wednesday, thursday, friday, saturday'):
            print('please enter a valid day')
            day = str(input('Please enter a day of the week, sunday, monday, tuesday, wednesday, thursday, friday, saturday:\n').casefold())


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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_int = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month_int]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        day_int = days.index(day) + 1
            # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day_int]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('The most common month is month:\n', df['month'].mode()[0])

    # display the most common day of week
    print('The most common day of the week is day:\n', df['day_of_week'].mode()[0])

    # display the most common start hour
    print('The most common hour to start is the:\n', df['Start Time'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most popular start station is:\n', df['Start Station'].mode()[0])

    # display most commonly used end station
    print('The most popular end station is:\n', df['Start Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    print('The most popular combination of start and stop station is:\n', df.groupby(['Start Station', 'End Station']).size().nlargest(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time is\n:', df['Trip Duration'].sum(),'seconds')

    # display mean travel time
    print('The mean travel time is\n:', df['Trip Duration'].mean(), 'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('The user count breakdown is:', df['User Type'].value_counts())

    # Display counts of gender
    if city == 'washington':
        print('This dataframe has no gender data')
    else:
        print('The gender count is:', df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
    if city == 'washington':
        print('This dataframe has no birth year data data')
    else:
        print('The earliest birth year is:', df['Birth Year'].min())
        print('The most recent birth year is:', df['Birth Year'].max())
        print('The most common year of birth is:', df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(city):
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # Loading of raw data 5 rows at a time using the index
    raw_data = str(input('Would you like to view the raw data?\n Y/N:').upper())
    while raw_data not in ('Y','N'):
        print('Please enter a valid response.')
        raw_data = str(input('Would you like to view the raw data?\n Y/N:').upper())

    if raw_data == 'Y':
        i = 0
        while raw_data == 'Y':
            # Using iloc to load 5 rows, starting at the current index
            print(df.iloc[[i,i+1,i+2,i+3,i+4]])
            raw_data = str(input('Would you like to view more raw data?\n Y/N:').upper())
            while raw_data not in ('Y', 'N'):
                print('Please enter a valid response.')
                raw_data = str(input('Would you like to view more raw data?\n Y/N:').upper())
            # if the user wants to load more data, push the index up by 5 places to load the next 5 rows
            i=i+5


def main():
    city, month, day = get_filters()
    df = load_data(city, month, day)
    print(df)

    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df,city)
    raw_data(city)

    restart = str(input('\nWould you like to restart? Y/N:\n').upper())
    while restart not in ('Y', 'N'):
        print('Please enter a valid response.')
        restart = str(input('\nWould you like to restart? Y/N:\n').upper())

    if restart == 'Y':
        main()
    else:
        print('Thank you for your time')

main()
