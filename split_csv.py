import os

def split_csv(input_file, output_dir, chunk_size=10000):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file, 'r') as infile:
        # uncomment this if the csv contain header
        # header = infile.readline().strip()
        chunk_num = 1
        while True:
            output_file = os.path.join(output_dir, f"part_{chunk_num}.csv")
            with open(output_file, 'w') as outfile:
                for _ in range(chunk_size):
                    line = infile.readline().strip()
                    if not line:
                        break
                    outfile.write(line + '\n')
                else:
                    chunk_num += 1
                    continue
                break

if __name__ == "__main__":
    input_file = "path to the csv file"
    output_dir = "output_csv"
    chunk_size = 10000
    split_csv(input_file, output_dir, chunk_size)
