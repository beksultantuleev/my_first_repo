import random
import timeit
questions = [{'Errors related to bias can be reduced by using large sample sizes': 'f'},
{'The impact of random errors can be reduced by using large sample sizes': 't'},
{'Systematic errors do not happen by pure randomness.': 't'},
{'The variance of a model measures how the expected output of a machine learning model diers from the true value of the function approximated by the model':'f'},
{'The objective of supervised learning is to find a model that reduces to zero the error between the model and the function approximated by the model. If a model A has a lower error on the training examples with respect to another model B,A  must be preferred':'f'},
{'The expected error between the label y of a data sample and the output of a supervised model f_hat(x) depends on bias or on variance, according to the weights of the model':'f'},
{'In the K-nearest-neighbours algorithm for classication, the output of a new input vector cannot be obtained as the majority of the outputs of the K-nearest vectors in memory':'f'},
{'In the K-nearest-neighbours algorithm, a long training phase is executed with the examples so that the generalization error will decrease.':'f'},
{'When applying the weighted k-nearest-neighbours algorithm for regression, the output of a new input vector is predicted depending on the output of the nearest k vectors in memory, with a weighted average giving more weight to the closest examples.':'t'},
{'Nearest neighbours algorithms can only be applied to classication problems.':'f'},
{'Precision is the proportion of true positives over the all the predictions predicted as positive by a classier':'t'},
{'Accuracy is dened as the proportion of true positives and true negatives over all the predictions made by a classier.':'t'},
{'Given a dataset of mushrooms, where edible mushrooms belong to the positive class and deadly mushrooms belong to the negative class, maximizing precision is more important than maximizing recall.':'t'},
{'Recall is the proportion of true negatives over all the elements that actually belong to the positive class':'f'},
{'Given a dataset of n tuples in m dimensions, the confusion matrix is m x m.':'f'},
{'The union of two convex sets is always convex.':'f'},
{'The function f(x)= 1 + x1 + x2 is linear.':'f'},
{'A function f(x), where x is a vector, is linear if for every scalar Alpha and Beta and every couple of vectors x and y: f(ax+By) = a*f(x)+B*f(y)':'t'},
{'A function f(x), where x is a vector, is linear if f(x+y) = f(x)+f(y).':'f'},
{'The roots of the equation x1+3x2=0 form a convex set.':'t'},
{'The intersection of two convex sets is always convex.':'t'},
{'The points satisfying the inequality 6x1 + 9x2 > 0 do not form a convex set.':'f'},
{'"Statistically signicant result" means that one can estimate probabilities of obtaining specic results, and that the probability to obtain the result by chance is less than a threshold value. Therefore the conclusion "statistically signicant or not" depends on the threshold value.':'t'},
{'For every k>0, in leave-one-out cross-validation, one of the k partitions is left out as validation data and the other partitions are used as training data.':'f'},
{'The number of data examples used for comparing different ML models greatly aects the level of statistical signicance of the results.':'t'},
{'The measurements of two phenomena are different in a statistically signicant way if one can demonstrate in a theorem that the two measurements will never be equal.':'f'},
{'A result is statistically signicant when it is obtained by democratic means, asking for the opinion of the largest possible number of experts.':'f'},
{'In stratied cross-validation, classes are balanced in both training and validation sets.':'t'},
{'In cross-validation, one repeats many train-and-test experiments, by splitting the original set of examples into two sets of different partitions (one for training and one for testing), and then maximizing the obtained result.':'f'},
{'Stratified cross-validation is useful to create learning models with more hidden layers.':'f'},
{'Given a dataset of n examples, the weights w* found by least squares methods do not define a model which is valid for all possible inputs.':'t'},
{'Given a dataset of n tuples (xi,yi) with 1<=i<=n, the signicance Si denes the importance that each xi has on the prediction of the output of some point x':'t'},
{'Given a dataset of n tuples (xi,yi) with 1<=i<=n, least squares methods are used to minimize the error sum(yi(w^T*xi-si)^2), where si is the significance of xi.':'f'},
{'Given a dataset of n tuples (xi,yi) with 1<=i<=n, let x be a point whose output needs to be predicted using Locally-Weighted Regression. The significance si can be defined as si = Exp(-(||xi-x||^2)/(Wk)), where Wk is some constant which controls the sensitivity of the model to points distant from x.':'t'},
{'Consider a dataset of n tuples in 2-dimensions (x1, x2), and let S be the covariance matrix of such dataset. Transform the dataset by multiplying x1 by a scalar alpha and obtain a dataset in 2-dimensions (alpha*x1, x2), dening S1 as the covariance matrix of the transformed dataset. Since the covariance matrix only measures how the coordinates of a set of points vary together, S=S1':'f'},
{'Given a labeled dataset in m>2 dimensions, consider the first principal component x1 and the second principal component x2 found by PCA. If the label is removed from the dataset and PCA is applied again, x1 and x2 might be different from the two principal components found before removing the label.':'f'},
{'A linear transformation L is a linear projection of vectors from a space of dimension m to a space of dimension p, where p must be lower than m':'f'},
{'The main diagonal of the covariance matrix corresponds to the variance along each input dimension.':'t'},
{'Given a dataset of centered data, the orthogonal projection found by PCA from a space of dimension m to a space of dimension p corresponds to the p eigenvectors with largest eigenvalues of the covariance matrix.':'t'},
{'Orthogonal projections from a space of dimension m to a space of dimension p are a particular type of linear transformation, which guarantees that projected data maximizes the sum of all squared pairwise distances in the m-dimensional space.':'f'},
{'The vectors x=(1,1) and y= (2,2) are collinear.':'t'},
{'The vectors x= (1,1) and y = (1,0) are orthogonal':'f'},
{'Given a labeled dataset in m>2 dimensions, consider the first principal component x1 and the second principal component x2 found by PCA. Let us define the mutual information of x1 and x2 with respect to the label y as MI(x1,y) and MI(x2,y). Since x1 explains the larger amount of variance among input dimensions, MI(x1)> MI(x2)':'f'},
{'Data should always be normalized or standardized before applying PCA, in order to remove the eect of outliers.':'f'},
{'Consider a dataset of n vectors in m dimensions. The covariance matrix is an n*m matrix.':'f'},
{'The covariance matrix measures how the coordinates of a set of points vary together, so it can only be used to detect variations along one of the dimensions of data.':'f'},
{'PCA is sensitive to outliers, because points which are far away from most of the other points contribute greatly to the sum of squared distances in the projected space':'t'},
{'In PCA, input variables are transformed into a possibly lower number of uncorrelated input variables called principal components. In ascending order, principal components take in account as much of the remaining variability of data as possible.':'t'},
{'The Euclidean distance is an appropriate similarity metric only when the range of input dimensions is similar and the same unit of measure is used.':'t'},
{'In k-means soft clustering, the batch update should be preferred with respect to the online update when the number of entities is very large':'f'},
{'The cosine similarity is not inuenced by the units of measure used to express the input dimensions of data, because it depends only on the direction of the vectors.':'t'},
{'If an internal representation of the entities to be clustered is available, dissimilarities between entities can be computed and each cluster is summarized by a prototype':'t'},
{'If only an external representation of the entities to be clustered is available, there is no information about the dissimilarities between entities.':'f'},
{'The Mahalanobis distance is an appropriate similarity metric only when the range of input dimensions is similar and the same unit of measure is used.':'f'},
{'In k-means soft clustering, each entity is assigned probabilistically to all clusters.':'t'},
{'K-means hard clustering is an iterative algorithm where, at each step, each entity is assigned to its nearest prototype. Then, the coordinates of each prototype are updated by averaging the coordinates of the entities assigned to it, and the process is repeated until some stopping criteria is met.':'t'},
{'In bottom-up clustering, at each step the most similar sets of points are merged together until a stopping criteria is met and the merging stops':'t'},
{'In top-down clustering, at each step the most similar sets of points are merged together until a stopping criteria is met and the merging stops.':'f'},
{'Clustering represents groups of similar points using prototypes, which are single points that summarize the information of observed data':'t'},
{'The shape of Voronoi cells is independent with respect to the type of distance similarity used by a clustering algorithm':'f'},
{'Clustering is a multi-objective optimization problem.':'t'},
{'Let x and y be two vectors of length n. ||x-y|| defines the Manhattan distance between x and y':'f'},
{'Clustering is a supervised learning technique':'f'},
{'The quantization error measures the error obtained by substituting the entities of each cluster with the respective prototype. Consequently, a lower quantization error implies a better clustering':'f'},
{'In k-means hard-clustering, the objective is to partition a set of entities into  disjoint subsets. Such objective is reached by minimizing the dissimilarities between the points and the prototype of each cluster, and maximizing the distances between the borders of different clusters':'t'},
{'Consider a dataset with n points in d dimensions. As a result, in least squares methods, we have to find the solution of a set of n equations in d variables':'t'},
{'If the number of different points is larger than the number of dimensions, the solution of the linear system can be found by computing the inverse of the matrix':'f'},
{'In gradient descent, if the step is less than 0.000000001 the function value will always decrease':'f'},
{'If the number of points is huge, using gradient descent is better than using the pseudo-inverse':'t'},
{'Models with too few parameters tend to produce a large variation of results if runs of training and testing are repeated (with some randomization)':'f'},
{'Models with too many parameters tend to fail because of a large bias, since they define models which might easily overt data':'f'},
{'Having few parameters contribute to the creation of flexible models because they can be easily interpreted by a human person':'f'},
{'Identifying the best model requires a compromise between bias and variance':'t'},
{'A suitable error measure on the training examples for regression models is the sum of squared errors between the known output yi and the output f_hat(xi) obtained by the models: sum(yi - f_hat(xi))^2':'t'},
{'The internal parameters (weights) of models created using supervised learning techniques define the flexibility of the models. If a model overts, a possible explanation is that the number of parameters of the model is too large given the observed data and so the model cannot properly generalize on unseen data':'t'},
{'Available data is composed by vectors of features x_vector associated to an output y, and such data is used to build a function which models the relationship between x_vector and y':'t'},
{'PCA is a supervised learning technique.':'f'},
{'Models for solving classication and regression problems are built by optimizing an objective function, which is assumed to be sufficiently smooth so that the generalization of a model built on training examples is possible':'t'},
{'In linear regression, if the number of parameters of the model is too large, learning the examples with zero errors becomes trivial, but the model will have diculties when generalizing results on unseen data':'t'},
{'An autoencoder is a multi-layer perceptron which aims at reproducing the input of the perceptron, using an intermediate encoding with less variables than the input.':'t'},
{'The following is a plausible squashing function to be applied to the result z of a scalar product to ensure a biologically-plausible output: squash(z) = 1/(1+e^(-z))':'t'},
{'Given a dataset, after a training phase an autoencoder learns a compressed representation of input data (without considering the labels). Once trained, the hidden layer of the autoencoder can be connected to an additional layer of perceptrons, in order to classify data according to the representation previously learned by the autoencoder':'t'},
{'The following function of two input variables x1 and x2: f(x1,x2)= BinaryXOR(x1, x2) can be realized using a multilayer perceptron with a single layer':'f'},
{'Consider a multilayer perceptron with bias units and 2 layers, where the first layer contains 3 perceptrons and the second layer contains 1 perceptron. With such a structure, the multilayer perceptron has 2 bias units':'f'},
{'Maximum likelihood estimation of parameters means that one maximizes the probability that the parameters of a model assume certain values, according to the evidence obtained by observed data.':'t'},
{'In autoencoders, the perceptrons in the middle layer of the neural network extract, from the original dataset, the input dimensions which are used to build a model that minimizes the difference between input data and rebuilt data':'f'},
{'The following functions of two input variables x1 and x2: f(x1,x2) = BinaryOR(x1, x2) and f(x1,x2) = BinaryAND(x1,x2) can be respectively realized with an appropriate choice of the vector w by the model m(w,x) = w^T*x.':'t'},
{'Goodness functions take measurements or decision variables as input and quantify an objective which needs to be optimized':'t'},
{'Inputs can be only numerical, qualitative measurements need to be transformed into numbers':'t'},
{'Machine learning techniques can build effective models only if abundant data is available for training and for testing':'t'},
{'Standard mathematical optimization requires the existence of goodness functions to be optimized, and the defenition of these functions usually requires an expensive effort in the real world. In many cases, this can be the most relevant effort in a "data science" project':'t'},
{'The objective of regression is to model the dependency of a real value on a set of input values.':'t'},
{'The objective of linear regression is to always guarantee zero error on the training examples':'f'},
{'If the number of input variables is 33, and one starts training from 99 examples, the parameters of the linear model obtaining zero error on the examples can always be determined':'f'},
{'If the number of input variables is 77, and one starts training from 33 different examples, the parameters of the linear model obtaining zero error on the examples can always be determined':'t'},
{'The minimum distance between a pair of clusters C,D is the distance between the nearest pair of points which respectively belong to C and D.':'t'},
{'A dendrogram can be used to identify into how many clusters the entities of a dataset should be grouped, by looking at horizontal distances between merging points':'f'},
{'The covariance matrix can be used to estimate the shape of a spheric cluster':'t'},
{'A dendrogram is a plot that can be used to visualize the order in which entities of a dataset have been merged':'t'},
{'In agglomerative clustering, at each step the most similar clusters are merged. The similarity between clusters can be measured in different ways, so at each step the most similar clusters are the ones which minimize minimum, maximum or average distance between pairs of clusters':'t'},
{'Given a cluster of points, the sample standard deviation can be used to estimate if a new unseen point belongs to the cluster with high probability or not':'t'},
{'A logistic function is used to transform the output of a linear model in the interval [0,1], so that it an be interpreted as a probability':'t'},
{'A logistic function determines the threshold according to which the output of a linear model is classied.':'f'},
{'Logistic regression can be used to solve regression problems':'f'},
{'In logistic regression, the standard sigmoid function is defined as 1/(1+e^t) with t= w^T*x, where w is a vector of weights and x is a vector of input data':'t'},
{'Filter methods are not able to identify mutual relationships between different inputs':'t'},
{'Even if the Pearson correlation coefficient between two data features is zero, it is not possible to state that such features are independent':'t'},
{'Filter methods consider different subsets of features of data to build a model, and they run training and testing for possible subsets of features in order to decide the best subset to be used':'f'},
{'If the X^2 value is computed to test the statistical independence between each input feature and the output label, the resulting X^2 values can be used to rank input features according to how probably each input feature and the output label are dependent':'t'},
{'Mutual information can be used to identify sets of features of input data which, when considered individually, do not provide any useful information in order to predict the output.':'t'},
{'The linear correlation coefficient between xi and yi may change if x values are normalized by dividing them by their standard deviation sigma>0 in the following manner: (xi)/(sigma)':'f'},
{'The entropy of a uniform probability distribution of n events is log2n.':'t'},
{'If the Pearson correlation coefficient between two data features is zero, the Mutual Information between such features is also zero':'f'},
{'The Pearson correlation coefficient measures the linear relationship between numeric data features. It is defined as the covariance of two input features divided by the product of their standard deviations; as a consequence, if the covariance is negative then also the correlation coefficient is going to be negative':'t'},
{'A possible normalization of the data consists of rescaling all input dimensions that they range is in [0,1].':'t'},
{'The linear correlation coefficient between xi and yi does not change if x values are centered by subtracting their mean value mu in the following manner: (xi - mu)':'t'},
{'In a classication problem of newspaper articles, statistical independence between class and input term means that Pr(class = c and term = t) = Pr(class = c) Pr(term = t)':'t'},
{'The use of the Chi-square test to deny statistical independence between two input dimensions means that, the larger the X^2 value, the lower is the probability that the input dimensions are truly independent':'t'},
{'Consider a dataset with n points in d dimensions. As a result, in least squares methods, we have to find the solution of a set of d equations in n variables':'f'},
{'Consider a dataset composed by n examples (xi,yi) with 1<=i<=n. The linear correlation coefficient between xi and yi may change if x values are squred.':'t'},
{'The roots of the equation x1 + x2 = 0 do not form a convex set':'f'},
{'The quantization error measure the error obtained by substituting the entities of each cluster with respective prototype. However the lower quantization error does not always imply a better clustering':'t'},
{'In k-means soft clustering, the online update should be preferred with respect to the batch update when the number of entities is very large. ':'t'},
{'An autoencoder is a multy-layer perceptron which aims at reproducing the input of the perceptron. The perceptrons in the middle layer of the neural network extract those input dimensions which can be used to build a model that minimizes the difference between input data and rebuilt data.':'f'},
{'The internal parameters (weights) of the models created using supervised learning techniques define the flexibility of the models. If a model underfits, a possible explanation is that the number of parameters of the model is too large with respect to the number of examples of the training set, and so the model cannot properly generalize on unseen data.':'f'},
{'The logistic function cannot be used as a model to solve regression problems':'f'},
{'':''},

]



def runtest(questions):
    random.shuffle(questions)
    right = 0
    wrong = 0
    skipped = 0
    mode = input('Please select mode: "exam" (exam simulation, u have 45 min), "hard" (33 qn), "survivor" (110+ qns)>>> ')
    if mode.lower() == 'exam':
        questions = questions[:55]
    elif mode.lower() == 'hard':
        questions = questions[:33]
    elif mode.lower() == 'survivor':
        resure = input('\n\tWARNING!!!\n \nYou are about to start the test in survivor mode! \nIn this mode every skipped qn is -1 point!\n \n\tAre  you sure?? \n \ntype "YES" (yes, bring it on!!) or "NO" (no, I want my Mommy!)>>> ')
        if resure.lower() == 'yes':
            questions = questions[:len(questions)]
        else:
            return '\n\tMommy is here, try again\n'
        print('\n\tMay the knowledge be with you...\n')
    else:
        return 'Smth is wrong! Try again'
    print('\n   Answer the qns with "t" (true), "f"(false) or press Enter to skip\n')
    start = timeit.default_timer()
    for dictionary in questions:
        for qn in dictionary: 
            answer = input(qn + '>>> ')
            if answer.lower() == 'true':
                answer = 't'
            elif answer.lower() == 'false':
                answer = 'f'
            if answer.lower() == dictionary.get(qn):
                right+=1
                print('\n\tCorrect! \n')
            elif answer == '':
                skipped +=1
                print('\n\tSkipped! \n') 
            else:
                wrong+=1
                print('\n\tIncorrect! \n')
    stop = timeit.default_timer() 
    if mode.lower() == 'survivor':
        return '\n_____________________\nRESULTS\n\nYour score is: {} point(s). \n\tRight ones {}. Wrong ones {}. Skipped ones {}. Overal qns {}. \n\tTIME {:.2f} minutes. \n\tMode "{}"'.format(right-wrong-skipped, right, wrong, skipped, len(questions), (stop-start)/60, mode)
    else:
        return '\n_____________________\nRESULTS\n\nYour score is: {} point(s). \n\tRight ones {}. Wrong ones {}. Skipped ones {}. Overal qns {}. \n\tTIME {:.2f} minutes. \n\tMode "{}"'.format(right-wrong, right, wrong, skipped, len(questions), (stop-start)/60, mode)

print(runtest(questions))



