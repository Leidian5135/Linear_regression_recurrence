import numpy as np

def generate_sinusoids(dataset,sinusoid_degress):
    '''
    six(x)
    :param dataset:
    :param sinusoid_degress:
    :return:
    '''

    num_examples = dataset.shape[0]
    sinusoids = np.empty((num_examples,0))

    for degree in range(1,sinusoid_degress+1):
        sinusoid_features = np.sin(degree*dataset)
        sinusoids = np.concatenate((sinusoids,sinusoid_features),axis=1)

    return sinusoids