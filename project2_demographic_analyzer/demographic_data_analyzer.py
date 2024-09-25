import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    print("\n---------- race_count:")
    print(race_count)

    # What is the average age of men?
    men_only_df = df[df['sex'] == 'Male']
    average_age_men = round(men_only_df['age'].mean(), 1)
    print("\n--------- men_only:")
    print(men_only_df)
    print(f"\n---------- average age of men: {average_age_men}")

    # What is the percentage of people who have a Bachelor's degree?
    bachelors_degree_df = df[df['education'] == 'Bachelors']
    # Calculate percentage
    percentage_bachelors = round(
        (bachelors_degree_df.shape[0] / df.shape[0]) * 100, 1
    )
    print("\n---------- bachelors_degree_df:")
    print(bachelors_degree_df)
    print(f"\n---------- percentage_bachelors: {percentage_bachelors}%")

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    advanced_education_levels = ['Bachelors', 'Masters', 'Doctorate']
    print("\n---------- advanced_education_levels:")
    print(advanced_education_levels)

    # Filter dataframe to only have people with advanced education
    higher_education = df[df['education'].isin(advanced_education_levels)]
    print("\n---------- higher_education:")
    print(higher_education)

    # What percentage of people without advanced education (lower education) make more than 50K?
    lower_education = df[~df['education'].isin(advanced_education_levels)]
    print("\n---------- lower_education:")
    print(lower_education)

    # Filter higher education dataframe to only include people earning more than 50K
    higher_education_rich = higher_education[higher_education['salary'] == '>50K']
    print("\n---------- higher_education_rich:")
    print(higher_education_rich)


    # Filter lower education dataframe to only include people earning more than 50K
    lower_education_rich = lower_education[lower_education['salary'] == '>50K']
    print("\n---------- lower_education_rich:")
    print(lower_education_rich)

    # Calculate percentage of people with advanced education who earn more than 50K
    higher_education_rich= round(
        (higher_education_rich.shape[0] / higher_education.shape[0]) * 100, 1
    )
    print(f"\n---------- higher_education_rich: {higher_education_rich}%")

    # Calculate percentage of people with lower education who earn more than 50K
    lower_education_rich= round(
        (lower_education_rich.shape[0] / lower_education.shape[0]) * 100, 1
    )
    print(f"\n---------- lower_education_rich: {lower_education_rich}%")

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    print(f"\n---------- min_work_hours: {min_work_hours} hours/week")

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    print("\n---------- num_min_workers:")
    print(num_min_workers)

    rich_percentage = num_min_workers[num_min_workers['salary'] == '>50K']
    print("\n---------- rich_percentage:")
    print(rich_percentage)
    # Calculate percentage of people who work minimum number of hours per week and have salary of >50K
    rich_percentage = round(
        (rich_percentage.shape[0] / num_min_workers.shape[0]) * 100, 1
    )
    print(f"\n---------- rich_percentage: {rich_percentage}%")

    # What country has the highest percentage of people that earn >50K?
    # Dict for results
    country_percentage_rich_dict = {}
    # Get total amount of people per country
    total_people_per_country = df.groupby('native-country').size()
    for country in df['native-country'].unique():
        # Filter people from current country
        country_data = df[df['native-country'] == country]
    
        # Count people with salary >50K in current country
        rich_people_count = country_data[country_data['salary'] == '>50K'].shape[0]
    
        # Get total amount of people in the current country
        total_people_count = total_people_per_country[country]
    
        # Divide by zero checking
        if total_people_count > 0:
            # Calculate % of rich people in the country
            percentage_rich = (rich_people_count / total_people_count) * 100
        else:
            # No people in the country
            percentage_rich = 0
    
        # Store result in dict
        country_percentage_rich_dict[country] = percentage_rich

    # Convert dict to series
    country_percentage_rich = pd.Series(country_percentage_rich_dict)
    print("\n---------- country_percentage_rich:")
    print(country_percentage_rich)

    # Get country with highest percentage of people earning >50K
    highest_earning_country = country_percentage_rich.idxmax()

    # Get highest percentage of people earning >50K
    highest_earning_country_percentage = round(
        country_percentage_rich.max(), 1
    )
    print(f"\n---------- highest_earning_country: {highest_earning_country}")

    # Identify the most popular occupation for those who earn >50K in India.
    india_rich_df = df[
        (df['native-country'] == 'India') & (df['salary'] == '>50K')
    ]
    print("\n---------- india_rich_df:")
    print(india_rich_df)

    # Count occurrences of each occupation for Indian people who earn >50K
    occupation_counts = india_rich_df['occupation'].value_counts()
    print("\n---------- occupation_counts:")
    print(occupation_counts)
    # Find most popular occupation
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
