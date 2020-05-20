import multiprocessing as mp

from script import random_answering_n_times

pool = mp.Pool(mp.cpu_count())


results = [pool.apply(random_answering_n_times, args=(
    'https://forms.gle/uk2GiApQmwv76eaG6',
    96
    ))]


pool.close()    
