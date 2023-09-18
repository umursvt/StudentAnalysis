import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()
sns.set_palette('colorblind')


data = pd.read_csv('data.csv')


data_copy = data.copy()

# Check if it is Erkek
men = data_copy[data_copy['Cinsiyet'] == 'Erkek']
woman = data_copy[data_copy['Cinsiyet'] == 'Kadın']


# ANAYSING MAN
men['Ortalama'] = men[['Fizik', 'Kimya', 'Biyoloji', 'Matematik']].mean(axis=1)
men_avr = pd.DataFrame(
    {'Öğrenci Adı': men['Öğrenci Adı'], 'Ortalama': men['Ortalama']})

success_man = men_avr[men_avr['Ortalama'] > 88]


# CHARTS MEN
plt.figure(figsize=(6, 5))
plt.bar(
    x=success_man['Öğrenci Adı'],
    height=success_man['Ortalama'],
    color=['red', 'green', 'blue', 'yellow', 'magenta',
           'purple', 'orange', 'lightblue', 'black']
)
plt.xticks(rotation=45)
plt.title('SUCCESSFUL MAN')
plt.show()

# ANALYSING WOMAN
woman['Ortalama'] = woman[['Fizik', 'Kimya',
                           'Biyoloji', 'Matematik']].mean(axis=1)
woman_avr = pd.DataFrame(
    {'Öğrenci Adı': woman['Öğrenci Adı'], 'Ortalama': woman['Ortalama']})

success_woman = woman_avr[woman_avr['Ortalama'] > 88]


# CHART WOMEN
plt.figure(figsize=(6, 5))
plt.bar(
    x=success_woman['Öğrenci Adı'],
    height=success_woman['Ortalama'],
    color=['red', 'green', 'blue', 'yellow', 'magenta',
           'purple', 'orange', 'lightblue', 'black']
)
plt.xticks(rotation=45)
plt.title('SUCCESSFULL WOMAN')
plt.ylabel('Score')
plt.show()

success_size_kind = pd.DataFrame(
    {'Başarılı Erkek': [len(success_man)], 'Başarılı Kadın': [len(success_woman)]})

print(success_size_kind.iloc[0])


plt.pie(success_size_kind.iloc[0],
        labels=success_size_kind.columns,
        autopct='%.2f%%',
        textprops={
            'color': 'w',
            'size': 'x-large',
            'fontweight': 'bold'
})
plt.legend()
plt.title("Başarılı Erkek ve Başarılı Kadın Dağılımı",
          fontsize=20, color='black')
plt.show()
