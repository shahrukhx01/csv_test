class CSVReader:
    def __init__(self, path, header_first, extension='csv'):
        self.header_first = header_first
        self.path = path
    
    def read_file(self):
        read_index = 1
        if self.header_first:
            read_index = 0
        print(read_index)
        f = open('{}'.format(self.path))
        return f.readlines()[read_index:]

   

class Merger:
    def __init__(self, data_path, write_after=1, target_file='target.csv',  ):
        self.write_after = write_after
        self.target_file = target_file
        self.data_path = data_path 
        self.buffer = list()

    def merge(self):
        for i in range(100000):
            if i%self.write_after == 0 and i > 0:
                self.write_files()

            else:
                print('{}/{}.csv'.format(self.data_path,i))
                lines = CSVReader(header_first= (i==0), path = '{}/{}.csv'.format(self.data_path,i)).read_file()
                self.buffer.append(lines)
     
    def write_files(self):
        f = open('{}/{}'.format(self.data_path, self.target_file), 'a+')

        while(len(self.buffer)>0):
            chunk = self.buffer.pop()
            f.write(''.join(chunk)) ## this operation slows down things

        f.close()


def main():
    csvmerger = Merger(data_path= '/Users/shahrukh/Desktop/csv_test-main/data')
    csvmerger.merge()
    
if __name__ == "__main__":
    main()
                
            
                






