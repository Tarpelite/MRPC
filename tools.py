import csv
import time
in_path = "share/"
out_path = "small_data/"


def sample_data(sample_rate):
    train_path =  "train.csv"
    paths  = ["train.csv", "dev.csv", "test.csv"]
    for file_path in paths:
        with open(in_path + file_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter="\t")
            lines = []
            for line in reader:
                lines.append(line)
        sample_len = int(len(lines)*sample_rate)
        out_lines = lines[:sample_len]
        with open(out_path + file_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f, delimiter = "\t")
            for line in out_lines:
                writer.writerow(line)
        if file_path == "dev.csv":
            with open(out_path + "aus_dev.label.csv", "w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                out_lines = [[x[1]] for x in out_lines]
                for line in out_lines:
                    writer.writerow(line)
in_path = "paranmt/"
out_path = "split_data/"

def split_data(slice_num):
    data_path = "para-nmt-50m.txt"
    with open(in_path + data_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        lines = []
        for line in reader:
            lines.append(line)
    lines_len = len(lines)
    sample_len = lines_len // slice_num
    i = 0
    cnt = 0
    while i < lines_len - slice_num:
        data = lines[i:i+sample_len]
        print("writing line:{0}/{1}".format(str(i), str(i+sample_len)))
        start_time = time.time()
        with open(out_path + data_path + "." +str(cnt), "w+", encoding="utf-8", newline="") as f:
            writer = csv.writer(f, delimiter="\t")
            for line in data:
                writer.writerow(line)
        end_time = time.time()
        i += sample_len
        cnt += 1
        print("cost time:", end_time-start_time)
    data = lines[i-sample_len:]
    print("writing line:{0}/{1}".format(str(i), str(i+sample_len)))
    with open(out_path + data_path + "." +str(cnt), "w+", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter="\t")
        for line in data:
            writer.writerow(line)
    print("finish")


if __name__ == "__main__":
    split_data(8)
