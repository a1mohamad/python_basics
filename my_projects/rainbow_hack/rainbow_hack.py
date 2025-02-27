import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    my_input = str(input_file_name)
    my_output = str(output_file_name)
    outputs =''
    with open(my_input) as h:
        reader = csv.reader(h)
        hash_database = dict()
        for number in range(1000, 10000):
            hash_database[number] = hashlib.sha256(b'%i' %number).hexdigest()
            reverse_hash_database = {v : k for k, v in hash_database.items()}
        for row in reader:
            name = row[0]
            hashed_password = row[1]
            password = reverse_hash_database[hashed_password]
            output = '%s,%i\n' %(name, password)
            outputs += output

    w = open(my_output)
    w.write(outputs)
    w.close()


