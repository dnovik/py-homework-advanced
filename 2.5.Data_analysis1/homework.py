import pandas as pd


def get_data_by_year(year_list):

    df_list = list()

    for year in year_list:
        file_path = f'names\yob{year}.txt'
        df = pd.read_csv(file_path, names=['Name', 'Gender', 'Qty'])
        df['Year'] = year
        df_list.append(df)
    
    return pd.concat(df_list)


def count_top3(year_list):

    df = get_data_by_year(year_list)
    top_3 = df.sort_values(by='Qty', ascending=False)

    return top_3.head(3)['Name'].to_list()


def count_dynamics(year_list):

    df = get_data_by_year(year_list)
    df_grouped = df.groupby(
        by=['Gender', 'Year']
    ).agg({
        'Name' : 'count'
    })

    df_grouped = df_grouped.reset_index()

    result = dict()
    female_names = df_grouped[df_grouped['Gender'] == 'F']['Name'].to_list()
    male_names = df_grouped[df_grouped['Gender'] == 'M']['Name'].to_list()
    result['F'] = female_names
    result['M'] = male_names

    return result

if __name__ == "__main__":
    # получаем топ-3 имен за указанные года
    count_top3([1900, 1950, 2000])

    # получаем динамику за указанные года
    count_dynamics([1900, 1950, 2000])
