import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('events.csv')
#x = df.visit_date.unique()
#the most activity:
def make_month(row): #first number means half of month(1 - 1st half, 2nd half), second number means month
    if row[0] == '0' or int(row[0:2]) <= 15:
        a = '1' + row[4]
    else:
        a = '2' + row[4]
    return a
df['visit_date'] = df['visit_date'].apply(make_month)
df['user_reg_date'] = df['user_reg_date'].apply(make_month)
print(df['user_reg_date'].value_counts())


#patterns for people, who is still learning or isnt learning
temp = df[(df['visit_date'] == '12') | (df['visit_date'] == '22')]['URL_visited'].value_counts()
famous_sites = temp.head(10)
print(famous_sites)
famous_sites.plot(kind='pie', y=None, autopct='%1.0f%%')
plt.savefig('famous_sites_notLearn.png')
plt.show()

temp = df[((df['user_reg_date'] == '12') | (df['user_reg_date'] == '22')) & ((df['visit_date'] == '23') | (df['visit_date'] == '14'))]['URL_visited'].value_counts()
famous_sites = temp.head(10)
print(famous_sites)
famous_sites.plot(kind='pie', y=None, autopct='%1.0f%%')
plt.savefig('famous_sites_stillLearn.png')
plt.show()
