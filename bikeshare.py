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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Please input the name of the city to analyze - can be either chicago, new york city or washington:').lower()
    while not city in ['chicago', 'new york city', 'washington']:
        print('Please input a valid city which can either be chicago, new york city or washington')
        city = input('Please input the name of the city to analyze - can be either chicago, new york city or washington:').lower()
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Please input the name of the month to filter by, or "all" to apply no month filter:').lower()
    while not month in ['all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']:
        print('Please input a valid month name to filter by, or "all"')
        month = input('Please input the name of the month to filter by, or "all" to apply no month filter:').lower()
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day= input('Please input the name of the day of week to filter by, or "all" to apply no day filter:').lower()
    while not day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        print('Please input a valid day name to filter by, or "all"')
        day= input('Please input the name of the day of week to filter by, or "all" to apply no day filter:').lower()
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
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Frequent Month:', popular_month)
   
    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day= df['day_of_week'].mode()[0]
    print('\nMost Frequent Day of the Week:', popular_day)
    
    # TO DO: display the most common start hour
    df['hour'] =df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('\nMost Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Frequent Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('\nMost Frequent End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start and End Station']= 'Start: ' + df['Start Station'] + ', End: ' + df['End Station']
    popular_start_and_end_station = df['Start and End Station'].mode()[0]
    print('\nMost Frequent Combination of Start and End Station:', popular_start_and_end_station)  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The Total Travel Time amounted to:', total_travel_time, 'seconds')
 
    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print('\nThe Mean Travel Time is:', avg_travel_time, 'seconds')
    
    #display the shortest travel time
    shortest_travel_time = df['Trip Duration'].min()
    print('\nThe Shortest Travel Time is:', shortest_travel_time, 'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types, '\n')

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print(gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('\nThe earliest year of birth is:', int(df['Birth Year'].min()))
        print('\nThe most recent year of birth is:', int(df['Birth Year'].max()))
        print('\nThe most common year of birth is:', int(df['Birth Year'].mode()[0]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    i=0
    raw_dat= input('\nDo you want to see raw data? Enter yes or no.\n').lower()
    while raw_dat =='yes':
        print(df.iloc[:i+5])
        i+=5
        raw_dat= input('\nDo you want to see raw data? Enter yes or no.\n').lower()
                  
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Goodbye!, Hope to see you again')
            break


if __name__ == "__main__":
	main()
