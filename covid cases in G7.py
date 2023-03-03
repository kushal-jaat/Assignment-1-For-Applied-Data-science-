import pandas as pd
import matplotlib.pyplot as plt

# defining the def function to filtring out the G7 counties


def plot_G7_countries_covid():
    G7_countries = ['Canada', 'France', 'Italy',
                    'Japan', 'UK', 'USA', 'Germany']
    df = pd.read_csv(
        "C:/Users/kusha/OneDrive/Desktop/assignment/covid_worldwide.csv")

    # filtering data for G7 countries
    df_G7 = df[df['Country'].isin(G7_countries)].copy()

    # replacing commas in population column and converting it to float
    df_G7['Total Cases'] = df_G7['Total Cases'].str.replace(',', '').astype(float)

    # print "Yes" if they are G7 countries
    for c in G7_countries:
        if c in df_G7['Country'].unique():
            print(c, "Yes")

    # ploting population of G7 countries in a pie chart
    plt.figure(figsize=(9, 7))
    plt.pie(df_G7['Total Cases'], labels=df_G7['Country'], autopct='%1.1f%%')
    plt.title('Total Covid Cases in G7 Countries')
    plt.show()


plot_G7_countries_covid()
