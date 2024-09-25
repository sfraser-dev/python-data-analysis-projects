import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    men_only_df = df[df['sex'] == 'Male']
    average_age_men = round(men_only_df['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors_degree_df = df[df['education'] == 'Bachelors']
    # Calculate percentage
    percentage_bachelors = round(
        (bachelors_degree_df.shape[0] / df.shape[0]) * 100, 1
    )

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    advanced_education_levels = ['Bachelors', 'Masters', 'Doctorate']

    # Filter dataframe to only have people with advanced education
    higher_education = df[df['education'].isin(advanced_education_levels)]

    # What percentage of people without advanced education (lower education) make more than 50K?
    lower_education = df[~df['education'].isin(advanced_education_levels)]

    # Filter higher education dataframe to only include people earning more than 50K
    higher_education_rich = higher_education[higher_education['salary'] == '>50K']

    # Filter lower education dataframe to only include people earning more than 50K
    lower_education_rich = lower_education[lower_education['salary'] == '>50K']

    # Calculate percentage of people with advanced education who earn more than 50K
    higher_education_rich= round(
        (higher_education_rich.shape[0] / higher_education.shape[0]) * 100, 1
    )

    # Calculate percentage of people with lower education who earn more than 50K
    lower_education_rich= round(
        (lower_education_rich.shape[0] / lower_education.shape[0]) * 100, 1
    )

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]

    rich_percentage = num_min_workers[num_min_workers['salary'] == '>50K']
    # Calculate percentage of people who work minimum number of hours per week and have salary of >50K
    rich_percentage = round(
        (rich_percentage.shape[0] / num_min_workers.shape[0]) * 100, 1
    )

    # What country has the highest percentage of people that earn >50K?
    country_percentage_rich = (
        df[df['salary'] == '>50K'].groupby('native-country').size()
        / df.groupby('native-country').size()
    ) * 100

    # Get country with highest percentage of people earning >50K
    highest_earning_country = country_percentage_rich.idxmax()

    # Get highest percentage of people earning >50K
    highest_earning_country_percentage = round(
        country_percentage_rich.max(), 1
    )

    # Identify the most popular occupation for those who earn >50K in India.
    india_rich_df = df[
        (df['native-country'] == 'India') & (df['salary'] == '>50K')
    ]
    # Count occurrences of each occupation for Indian people who earn >50K
    occupation_counts = india_rich_df['occupation'].value_counts()
    # Find most popular occupation
    top_IN_occupation = occupation_counts.idxmax()

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
