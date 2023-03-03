import pandas as pd
import matplotlib.pyplot as plt

# creeating a def function to filter out the dog's


def plot_dog_lifespan():
    df = pd.read_csv(
        "C:/Users/kusha/OneDrive/Desktop/assignment/dogbreeddetail1.csv")
    dog_names = ['Golden Retriever', 'Dachshund',
                 'Labrador Retriever', 'Great Dane']
    # filtering dataframe for the dog names
    df_filtered = df[df['Name'].isin(dog_names)]
    # creating bar graph for maximum and minimum life of dog
    fig, ax = plt.subplots()
    ax.bar(df_filtered['Name'], df_filtered['max_life_expectancy'],
           label='Max Life', color='blue')
    ax.bar(df_filtered['Name'], df_filtered['min_life_expectancy'],
           label='Min Life', color='green')
    ax.set_xlabel('Dog Name')
    ax.set_ylabel('Life Span of dog (years)')
    ax.set_title('Life Span of dog')
    ax.legend()
    plt.show()


# calling the plot_dog_lifespan()
plot_dog_lifespan()
