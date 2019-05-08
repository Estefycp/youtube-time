#!/usr/bin/python3

import predictions
import data_process

def get_model_dict():
    countries = [
        'US', 'CA', 'DE', 'FR', 'GB'
    ]
    targets = [
        'like_rate', 'dislike_rate',
        'comment_rate', 'time_to_trending',
        'views'
    ]
    models = {}
    for c in countries:
        models[c] = {}
        X, y = data_process.getX_y(c, targets)
        for t in targets:
            y_tar = y[t]
            models[c][t] = predictions.get_model_scaler(X, y_tar)

    return models