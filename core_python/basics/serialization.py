import h5py


def writing_file_with_h5():
    with h5py.File("test1.hdf5", "w") as file:
        dataset = file.create_dataset("test_dataset", (100,))
    return dataset


def reading_wih_h5py(file_name):
    pass


def main():
    data = writing_file_with_h5()
    print(type(data))
    print(data[:10])


if __name__ == "__main__":
    main()
