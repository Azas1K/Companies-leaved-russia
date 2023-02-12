import warnings
from datetime import datetime
import csv
from index import dictionary

warnings.filterwarnings("ignore")


head = ['Name', 'Action', 'Industry', 'Country']

def get_data():
    # print(response)
    cur_data = datetime.now().strftime('%d_%m_%Y')

    with open(file = f'data_{cur_data}.csv', mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(head)

        for i in dictionary:
            head[0] = i["name"]
            head[1] = i["description"]
            head[2] = "NaN"
            head[3] = i["country_name"]
            writer.writerow((head))


def main():
    get_data()

if __name__ == '__main__':
    main()

