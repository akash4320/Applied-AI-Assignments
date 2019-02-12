from importData import importTrainingData, importValidationData, importUnlabeled
from KNN import KNN
import json

import json
import numpy as np
import itertools

# Import the training data, validation data, and the unlabeled data
trainingLabels, trainingSamples = importTrainingData('..\\dataset1.csv')
validationLabels, validationSamples = importValidationData('..\\validation1.csv')
unlabeledSamples = importUnlabeled('..\\days.csv')

# Oddly, KNN.NeighbourWeightingStrategy.WEIGHTED_MAJORITY_VOTE seems to degrade performance a bit
options = KNN.KNNOptions(65, 2, [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], KNN.NeighbourWeightingStrategy.MAJORITY_VOTE)
predictor = KNN(options, trainingLabels, trainingSamples)
predictor.determine_best_K(validationLabels, validationSamples)
labels = predictor.predict(unlabeledSamples)

for label, sample in zip(labels, unlabeledSamples):
    print('{} should be {}'.format(sample, label))