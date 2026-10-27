import os
import kagglehub

def import_datasets():
    data_dir = os.path.join(os.curdir,'data')
    kagglehub.dataset_download("bryanpark/jit-dataset",path='je.test', output_dir = data_dir)
    kagglehub.dataset_download("bryanpark/jit-dataset",path='je.train', output_dir = data_dir)


if __name__ == '__main__':
    import_datasets()