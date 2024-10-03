import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    # Get a Series containing the counts of unique values using value_counts()
    race_count = df['race'].value_counts()
    print("\n---------- race_count:")
    print(race_count)

    # What is the average age of men?
    # Create boolean mask Series for males
    male_mask_series = df['sex'] == 'Male'
    print("\n---------- male_mask:")
    print(male_mask_series)
    # Use male_mask to filter the DF returning new DF with only males
    men_only_df = df[male_mask_series]
    print("\n---------- men_only_df:")
    print(men_only_df)

    # Calculate average age of men to one decimal place
    average_age_men = round(men_only_df['age'].mean(), 1)
    print(f"\n---------- average age of men: {average_age_men}")

    # What is the percentage of people who have a Bachelor's degree?
    # Create boolean mask Series for people with Bachelors degree
    bachelors_degree_series = df['education'] == 'Bachelors'
    # Use bachelors_degree_series to filter the DF returning new DF with only people with Bachelors degree
    bachelors_degree_df = df[bachelors_degree_series]

    # Calculate percentage (of people with Bachelors degree to one decimal place)
    # Number of bachelors_degree_df rows (.shape[0]) divided by total number of rows
    percentage_bachelors = round(
        (bachelors_degree_df.shape[0] / df.shape[0]) * 100, 1
    )
    print("\n---------- bachelors_degree_df:")
    print(bachelors_degree_df)
    print(f"\n---------- percentage_bachelors: {percentage_bachelors}%")

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # List of advanced education levels
    advanced_education_levels = ['Bachelors', 'Masters', 'Doctorate']  # list of strings
    print("\n---------- advanced_education_levels:")
    print(advanced_education_levels)

    # Filter dataframe to only have people with advanced education
    # Access 'education' column
    education_column = df['education']
    # Create boolean mask for people with advanced education levels
    higher_education_mask = education_column.isin(advanced_education_levels)  # is series element in the list?
    # Use boolean mask to filter the DF
    higher_education = df[higher_education_mask]
    print("\n---------- higher_education:")
    print(higher_education)

    # Filter higher education dataframe to only include people earning more than 50K
    # Access salary column for the higher education DF
    salary_column = higher_education['salary']
    # Create boolean mask for salaries >50K
    rich_salary_mask = salary_column == '>50K'
    # Use boolean mask to filter the higher education DF for those earning >50K
    higher_education_rich = higher_education[rich_salary_mask]
    print("\n---------- higher_education_rich:")
    print(higher_education_rich)

    # Calculate percentage of people with advanced education who earn more than 50K
    # Number of higher_education_rich rows (.shape[0]) divided by total number of higher_education rows 
    higher_education_rich= round(
        (higher_education_rich.shape[0] / higher_education.shape[0]) * 100, 1
    )
    print(f"\n---------- higher_education_rich: {higher_education_rich}%")

    # What percentage of people without advanced education (lower education) make more than 50K?
    # Access education column
    education_column = df['education']
    # Create boolean mask for people with lower education levels
    lower_education_mask = ~education_column.isin(advanced_education_levels)
    # Use the boolean mask to filter the DataFrame for lower education levels
    lower_education = df[lower_education_mask]
    print("\n---------- lower_education:")
    print(lower_education)

    # Filter lower education dataframe to only include people earning more than 50K
    # Create a boolean mask for salaries >50K then use it to filter the lower education DF
    lower_education_rich = lower_education[lower_education['salary'] == '>50K']
    print("\n---------- lower_education_rich:")
    print(lower_education_rich)

    # Calculate percentage of people with lower education who earn more than 50K
    # Number of lower_education_rich rows (.shape[0]) divided by total number of lower_education rows
    lower_education_rich= round(
        (lower_education_rich.shape[0] / lower_education.shape[0]) * 100, 1
    )
    print(f"\n---------- lower_education_rich: {lower_education_rich}%")

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    # Get the minimum value of the 'hours-per-week' column
    min_work_hours = df['hours-per-week'].min()
    print(f"\n---------- min_work_hours: {min_work_hours} hours/week")

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    # Filter people who work minimum number of hours per week
    # Create boolean mask for people who work the min no of hours per week then use it to filter the DF
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    print("\n---------- num_min_workers:")
    print(num_min_workers)

    # Filter people who work minimum number of hours per week and have salary of >50K
    # Create boolean mask for people who work the min no of hours per week and have salary >50K then use it to filter the DF
    rich_percentage = num_min_workers[num_min_workers['salary'] == '>50K']
    print("\n---------- rich_percentage:")
    print(rich_percentage)
    # Calculate percentage of people who work minimum number of hours per week and have salary of >50K
    # Number of rich_percentage rows (.shape[0]) divided by total number of people who work min hours per
    rich_percentage = round(
        (rich_percentage.shape[0] / num_min_workers.shape[0]) * 100, 1
    )
    print(f"\n---------- rich_percentage: {rich_percentage}%")

    # What country has the highest percentage of people that earn >50K?
    # Dict for results
    country_percentage_rich_dict = {}
    # Get total amount of people per country, group by 'native-country' and then get size of each group
    total_people_per_country = df.groupby('native-country').size()
    # Loop through unique countries
    for country in df['native-country'].unique():
        # Create boolean mask for current country
        country_filter = df['native-country'] == country
        #print("\n---------- country_filter:")
        #print(country_filter)
        # Use boolean mask to filter the DF for the current country
        country_data = df[country_filter]
        #print("\n---------- country_data:")
        #print(country_data)
    
        # Count people with salary >50K in current country
        # Create boolean mask for people with salary >50K (for current country)
        salary_filter = country_data['salary'] == '>50K'
        #print("\n---------- salary_filter:")
        #print(salary_filter)
        # Get data for people with salary >50K
        # Use boolean mask to filter the DF (for current country)
        filtered_data = country_data[salary_filter]
        #print("\n---------- filtered_data:")
        #print(filtered_data)
        # Get number of rows in filtered_data (using .shape[0])
        rich_people_count = filtered_data.shape[0]
        #print(f"\n---------- rich_people_count: {rich_people_count}")
    
        # Get total amount of people in the current country
        total_people_count = total_people_per_country[country]
    
        # Calc percentages (with divide by zero checking)
        if total_people_count > 0:
            # Calculate % of rich people in the country
            percentage_rich = (rich_people_count / total_people_count) * 100
        else:
            # There are no people in the country
            percentage_rich = 0
    
        # Store result in dict
        country_percentage_rich_dict[country] = percentage_rich

    # Convert dict to Series
    country_percentage_rich = pd.Series(country_percentage_rich_dict)
    print("\n---------- country_percentage_rich:")
    print(country_percentage_rich)

    # Get country with highest percentage of people earning >50K
    # Note: idxmax() returns the index of the first occurrence of the maximum value
    highest_earning_country = country_percentage_rich.idxmax()

    # Get highest percentage of people earning >50K
    highest_earning_country_percentage = round(
        country_percentage_rich.max(), 1
    )
    print(f"\n---------- highest_earning_country: {highest_earning_country}")

    # Identify the most popular occupation for those who earn >50K in India.
    # Filter by India and >50k
    india_rich_df = df[
        (df['native-country'] == 'India') & (df['salary'] == '>50K')
    ]
    print("\n---------- india_rich_df:")
    print(india_rich_df)

    # Count occurrences of each occupation for Indian people who earn >50K
    # Note: value_counts() counts the unique values in a col and return them as a Series in descending order of frequency
    occupation_counts = india_rich_df['occupation'].value_counts()
    print("\n---------- occupation_counts:")
    print(occupation_counts)
    # Find most popular occupation
    # Note: idxmax() returns the index of the first occurrence of the maximum value
    # Note: Series only have a row index, so idxmax() returns the row index
    # Note: DFs have row and column index, idxmax() returns the row index
    top_IN_occupation = occupation_counts.idxmax()
    print(f"\n---------- top_IN_occupation: {top_IN_occupation}")

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
