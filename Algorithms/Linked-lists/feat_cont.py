def feature_contribution(data, m, model):
    """Computes feature contribution for attributes in the model
    """
    phi = np.zeros(data.shape[1])
    X = data[data.id <= 100]

    for num in range(1, m):
        feat_sample = X[X.columns.to_series().sample(10)]
        x = X.sample()
        w = data.sample()

        for feat in feat_sample.columns:

            preceding = []
            for col in feat_sample.columns:
                if col == feat:
                    break
                preceding.append(col)
            b1_pre = preceding += [feat]
            b2_suc = [feat] += succeeding
            succeeding = [col for col in feat_sample.columns if col not in preceding and col != feat]

            b1 = pd.merge(x[b1_pre], w[succeeding], left_index=True, right_index=True)
            b2 = pd.merge(x[preceding], w[b2_suc], left_index=True, right_index=True)

            phi += model(b1) - model(b2)

    phi = phi / m

    return phi


hvPlot(pd.DataFrame({'index': indices,
                     


                    'contribution': feature_contribution}).sort_values(by='contribution',
                                                                       ascending=False)[:25]).bar(x="index",
                                                                                                  y="contribution",
                                                                                                  invert=True,
                                                                                                  height=500)
