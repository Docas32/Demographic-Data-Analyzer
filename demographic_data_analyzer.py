import pandas as pd



def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')



    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.



    race_count = df.race.value_counts()

    # What is the average age of men?
    average_age_men = df.loc[df['sex'] == "Male"]
    average_age_men = average_age_men['age'].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    education = df[df['education'] == 'Bachelors'].count()
    education = education['education']
    percentage_bachelors = (education / df['education'].count() * 100).round(1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = None
    lower_education = None

    # percentage with salary >50K
    degrees = ['Bachelors', 'Masters', 'Doctorate']

    high_pay = []
    high_ed = []

    for i in degrees:
        higher_education = df[(df['education'] == i)].count()
        education = df[(df['education'] == i) & (df['salary'] == '>50K')].count()
        education = education['education']
        high_pay.append(education)
        high_ed.append(higher_education['education'])

    higher_education_rich = (sum(high_pay)/sum(high_ed)*100).round(1)

    lower_degrees = ['HS-grad', '11th', '9th', 'Some-college', 'Assoc-acdm', 'Assoc-voc',
               '7th-8th', '12th', 'Prof-school', '5th-6th', '10th', 'Preschool',
               '1st-4th']

    lowered_high_pay = []
    lower_ed = []

    for i in lower_degrees:
        lower_education = df[(df['education'] == i)].count()
        education = df[(df['education'] == i) & (df['salary'] == '>50K')].count()
        education = education['education']
        lowered_high_pay.append(education)
        lower_ed.append(lower_education['education'])
    lower_education_rich = (sum(lowered_high_pay)/sum(lower_ed)*100).round(1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = None

    one_hour = df[df['hours-per-week'] == min_work_hours]
    one_hour = one_hour['hours-per-week'].count()
    one_hour

    one_hour_50k = df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')]
    one_hour_50k = one_hour_50k['hours-per-week'].count()

    rich_percentage = (one_hour_50k/ one_hour) * 100

    # What country has the highest percentage of people that earn >50K?
    highCounts = df[df.salary == ">50K"].groupby(['native-country']).count().salary
    highCounts
    totalCounts = df['native-country'].value_counts()
    result = highCounts / totalCounts * 100
    highest_earning_country = result.idxmax()
    highest_earning_country_percentage = round(result.max(),1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == "India") & (df['salary']==">50K")].occupation.value_counts().idxmax()

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
