#todo Imoprtant
# import tensorflow as tf
#
# single_feature_normalizer = tf.keras.layers.Normalization(axis=None)
# feature = tf.random.normal((314, 1))
# single_feature_normalizer.adapt(feature)
#
# single_feature_model = tf.keras.models.Sequential([
#     tf.keras.layers.Input(shape=(1,)),
#     single_feature_normalizer,
#     tf.keras.layers.Dense(1)
# ])
import time
from multiprocessing import Pool,Process
def f(x):
    print(x+x)
def g():
    print("Hi")
if __name__ == '__main__':
    t1 = time.perf_counter()
    with Pool(100) as p:
        p.map(f,list(range(1,1000)))
    t2 = time.perf_counter()
    p1 = Process(target=g)
    p1.start()
    p1.join()
    t3 = time.perf_counter()
    print("Process:", t3-t2)
    print("Pool:",t2-t1)


