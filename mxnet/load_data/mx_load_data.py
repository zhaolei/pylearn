import mxnet as mx

ita = mx.io.CSVIter(
    data_csv = './dat.csv',
    data_shape =(2,),
    label_csv = './lab.csv',
    label_shape = (1,), 
    batch_size=1
    )

print(ita)

data_iter = mx.io.CSVIter(data_csv='./lab.csv', data_shape=(1,), batch_size=1)
print(data_iter)

data_iter = mx.io.CSVIter(data_csv='./dat.csv', data_shape=(2,), batch_size=1)
print(data_iter)

data_iter = mx.io.CSVIter(data_csv='./dat.csv', data_shape=(2,), label_csv='./lab.csv', label_shape=(1,), batch_size=1)
print(data_iter)
