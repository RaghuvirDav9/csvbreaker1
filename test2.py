from multiprocessing import Pool
from multiprocessing import Process
import csv


# this function creates a file and append data that it gets as an argummnts
def break_1(chunk, count):
    with open('demofile1_' + str(count) + '.csv', 'at', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', lineterminator='\n', quoting=csv.QUOTE_ALL)
        writer.writerow(header)
        for row in chunk:
            writer.writerow(row)
    print(count)


# ehis function initiates process to make a new file from the chunk
def process_chunk(chunk, count):
    print('len:' + str(len(chunk)))
    # with Pool() as p:
    Process(target=break_1(chunk, count))


# it creates chunks from the reader and pass it as argument to next function
def break_csv():
    count = 0
    for i, line in enumerate(csv_reader):
        if i % chunksize == 0 and i > 0:
            count = count + 1
            process_chunk(chunk, count)
            del chunk[:]
            chunk.append(line)
        else:
            chunk.append(line)
    count = count + 1
    process_chunk(chunk, count)


# main function to initiate program
if __name__ == '__main__':
    with open('demo_file.csv', 'tr', encoding='utf-8') as file:
        csv_reader = csv.reader(file, delimiter=',', quoting=csv.QUOTE_ALL)
        header = next(csv_reader)
        print(header)
        chunk, chunksize = [], 1000000
        break_csv()
    print('done')
