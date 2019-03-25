import tarfile
import gzip
import shutil
import zipfile
import os

def gunzip_shutil(source_filepath, dest_filepath, block_size=65536, remove = False):
    with gzip.open(source_filepath, 'rb') as s_file, \
            open(dest_filepath, 'wb') as d_file:
        shutil.copyfileobj(s_file, d_file, block_size)
        if remove:
            os.remove(s_file)


def extract_subject_trails(dirpath, remove = False):
    gzfiles = os.listdir(dirpath + '/')
    for gzfile in gzfiles:
        gzfile_path = dirpath + '/' + gzfile
        gunzip_shutil(gzfile_path, dirpath + '/' + gzfile.replace('.gz','.rd'))
        if remove:
            os.remove(gzfile_path)

def extract_tar(tar_path, directory_to_extract_to, remove = False):
    tar = tarfile.open(tar_path, "r:gz")
    tar.extractall(directory_to_extract_to)
    tar.close()
    if remove:
        os.remove(tar_path)

def extract_dataset(dirpath, remove = False):
    targzfiles = os.listdir(dirpath)
    for targzfile in targzfiles:
        if (targzfile.endswith("tar.gz")):
            subject_tar_path =  dirpath + '/' + targzfile
            subject_dir_path = subject_tar_path.strip('tar.gz')
            extract_tar(subject_tar_path, dirpath, remove)
            extract_subject_trails(subject_dir_path, remove)

def read_trail(trail_file_path):
    with open(trail_file_path) as f:
        header = next(f)
        is_alcoholic = 0
        recording_name = header.split(' ')[1]
        if recording_name[3] == 'a':
            is_alcoholic = 1
        subject_num = recording_name[8:11]
        for _ in range(2):
            next(f)
        stim_desc = next(f).split(' ')
        stim_type = stim_desc[1] + ' ' + stim_desc[2].strip(',')
        trail_num = stim_desc[len(stim_desc) - 1].strip('\n')
        next(f)
        trail_stims = []
        channel_stims = []
        i = 1
        for line in f:
            parsed_line = line.split(' ')
            if parsed_line[0] != '#':
                stim = parsed_line[3]
                channel_stims.append(float(stim))
            else:
                trail_stims.append(channel_stims)
                channel_stims = []
        trail_stims.append(channel_stims)
    return (subject_num, trail_num, stim_type, trail_stims, is_alcoholic)

def read_all_trails(dirpath):
    subjects_dirs = os.listdir(dirpath)
    dataset = []
    for subject_dir in subjects_dirs:
        subject_dir_path = dirpath + '/' + subject_dir 
        if os.path.isdir(subject_dir_path):
            subject_trails = os.listdir(subject_dir_path)
            for subject_trail in subject_trails:
                subject_trail_path = subject_dir_path + '/' + subject_trail
                try:
                    trail_data = read_trail(subject_trail_path)
                    dataset.append(trail_data)
                except:
                    print('{} corrupted'.format(subject_trail))
    return dataset