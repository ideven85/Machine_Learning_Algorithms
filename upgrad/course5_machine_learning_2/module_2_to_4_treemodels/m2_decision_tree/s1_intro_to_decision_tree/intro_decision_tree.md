Decision Tree

Welcome to the module ‘Tree Models’. In this module, you will learn about two important machine learning models: decision trees and random forests.
 
You will first learn about decision trees and then proceed to learn about random forests, which are a collection of multiple decision trees. A collection of multiple models is called an ensemble.
 
With high interpretability and an intuitive algorithm, decision trees mimic the human decision-making process and are efficient in dealing with categorical data. Unlike other algorithms, such as logistic regression and support vector machines (SVMs), decision trees do not help in finding a linear relationship between the independent variable and the target variable. However, they can be used to model highly non-linear data.
 
You can use decision trees to explain all the factors that lead to a particular decision/prediction. And so can be used in explaining certain business decisions to entrepreneurs. Decision trees form the building blocks for random forests, which are commonly used among the Kaggle community.
 
Random forests are collections of multiple trees and are considered to be one of the most efficient machine learning models. By the end of this module, you should be able to use decision trees and random forests to solve both classification and regression problems.
 
In this session:
* Introduction to decision trees
* Interpretation of decision trees
* Building decision trees
* Tree models over linear models
* Decision trees for regression problems


You have learnt some classical machine learning algorithms like linear regression, logistic regression etc. for solving both regression and classification problems. Then what do you think is the need of going ahead with these linear models. Linear models cannot handle collinearity and non linear relationships in the data well. Now here comes the role of decision trees which leverages these properties. You will learn about each of these in detail as you go ahead. 

Definition 

A decision tree, as the term suggests, uses a tree-like model to make predictions. It resembles an upside-down tree and uses a similar process that you do to make decisions in real life, i.e., by asking a series of questions to arrive at a decision. A binary tree.
 
A decision tree splits data into multiple sets of data. Each of these sets is then further split into subsets to arrive at a decision. Let’s hear from Prof. Raghavan as he explains this process in detail.

￼



As you saw in this video, a decision tree uses a natural decision-making process, i.e., it asks a series of questions in a nested if-then-else structure. On each node, you ask a question to further split the data that is held by the node. If the test passes, you move to the left; otherwise, you move to the right.
 The first and top node of a decision tree is called the root node. The arrows in a decision tree always point away from this node.
 The node that cannot be further classified or split is called the leaf node. The arrows in a decision tree always point towards this node.
 
Any node that contains descendant nodes and is not a leaf node is called the internal node.
￼
In the next segment, you will take a look at some real-life examples to understand decision trees better.

Intuition

Interpreting a decision tree is nothing but asking a series of questions - something similar to what a doctor would do when they are diagnosing their patients. The first question we asked was, "Is the age less than 54.5?". Depending on the answer, we moved to the next step where we asked whether the person is a male or a female, and so on. At the end of this line of question, lies an answer - whether the person has heart disease or not. 
 
Now, if you were a doctor, you could ask these series of questions, and depending on the answers, you can probably make an educated prediction of whether the patient has the disease or not. This prediction here will obviously be based on your past learnings and experiences of treating such patients. A decision tree does the same thing - on the training data, it checks how the patients are doing based on their different attributes (this acts as the algorithm's experience) and based on that experience, it asks the users a series of questions to predict whether a person has heart disease or not.
 
Let's now look at the other side of the tree and understand the factors leading to a heart disease.

Interpretation

it is easy to interpret a decision tree, and you can almost always identify the various factors that lead to a particular decision. In fact, trees are often underestimated in their ability to relate the predictor variables to their predictions. As a rule of thumb, if interpretability by layman is what you are looking for in a model, then decision trees should be at the top of your list.
 
In a decision tree, you start from the top (root node) and traverse left/right according to the result of the condition. Each new condition adds to the previous condition with a logical ‘and’, and you may continue to traverse further until you reach the final condition’s leaf node. A decision is the value (class/quantity) that is assigned to the leaf node.
 
Heart Disease - Decision Tree
 
￼
As depicted in the heart disease example in the image above, the leaf nodes (bottom) are labelled ‘Disease’ (indicating that the person has heart disease) or ‘No Disease’ (which means the person does not have heart disease).
 Note that the splits are effectively partitioning the data into different groups with similar chances of heart disease.
 
So, in decision trees, you can traverse the attributes backwards and identify the factors that lead to a particular decision. 
 In the heart disease example, the decision tree predicts that if the ‘age’ of a person is less than or equal to 54.5, the person is female, and her cholesterol level is less than or equal to 300, then the person will not have heart disease, i.e., young females with a cholesterol level <= 300 have a low chance of being diagnosed with heart disease.
 Similarly, there are other paths that lead to a leaf being labelled Disease/No Disease. In other words, each decision is reached via a path that can be expressed as a series of ‘if’ and logical 'and' conditions that are satisfied together. The final decisions are stored in the form of class labels in leaves.  
Comprehension - Interpreting a Decision Tree
Mithali is an incredible cricketer. She plays cricket only when the pitch is dry, and the field is well lit. Based on past observations, you also know that she doesn’t play cricket when either the pitch is wet, or the light is dim.
 
Now that you have undetstood how to interpret the end result of a decision tree, let's now learn how to actually construct this tree in the first place.
Before you proceed further, Spend some time answering the question next.

Decision Tree Construction

It involves the following steps:
1. Recursive binary splitting/partitioning the data into smaller subsets
2. Selecting the best rule from a variable/ attribute for the split
3. Applying the split based on the rules obtained from the attributes
4. Repeating the process for the subsets obtained
5. Continuing the process until the stopping criterion is reached
6. Assigning the majority class/average value as the prediction
Now, you might have many questions lingering on your mind like what is the best variable for the split, how do I know what is the stopping criterion, and so on. Don't worry, as the steps you learnt just now is just a high-level view of the tree building process. In the coming sessions, you will learn each of these processes in detail.
 
Now, the decision tree building process is a top-down approach. The top-down approach refers to the process of starting from the top with the whole data and gradually splitting the data into smaller subsets. 
 
The reason we call the process greedy is because it does not take into account what will happen in the next two or three steps. The entire structure of the tree changes with small variations in the input data. This, in turn, changes the way you split and the final decisions altogether. This means that the process is not holistic in nature, as it only aims to gain an immediate result that is derived after splitting the data at a particular node based on a certain rule of the attribute.

Summary

Let’s summarise the advantages of tree models one by one in the following order:
* Predictions made by a decision tree are easily interpretable.
* A decision tree is versatile in nature. It does not assume anything specific about the nature of the attributes in a data set. It can seamlessly handle all kinds of data such as numeric, categorical, strings, Boolean, etc.
* A decision tree is scale-invariant. It does not require normalisation, as it only has to compare the values within an attribute, and it handles multicollinearity better.
* Decision trees often give us an idea of the relative importance of the explanatory attributes that are used for prediction.
* They are highly efficient and fast algorithms.
* They can identify complex relationships and work well in certain cases where you cannot fit a single linear relationship between the target and feature variables. This is where regression with decision trees comes into the picture.
 
In regression problems, a decision tree splits the data into multiple subsets. The difference between decision tree classification and decision tree regression is that in regression, each leaf represents the average of all the values as the prediction as opposed to a class label in classification trees. For classification problems, the prediction is assigned to a leaf node using majority voting but for regression, it is done by taking the average value. This average is calculated using the following formula:
 
^yt=1Nt∑iϵDty(i), where yi’s represent the observations in a node.  
For example, suppose you are predicting the sales your company will have based on various factors such as marketing, no. of products, etc. Now, if you use a decision tree to solve this problem (the process of actually building a regression tree is covered in the next session), and if one of the leaf nodes has, say, 5 data points, 1 Cr, 1.3 Cr, 0.97 Cr, 1.22 Cr, 0.79 Cr. Now, you will just take the average of these five values which comes out to be 1.05 Cr, and that becomes your final prediction.
 
Decision tree classification is what you’ll most commonly work on. However, remember that if you get a data set where you want to perform regression, decision tree regression is also a good idea.
 
This module includes an optional demonstration on regression trees for those who want to explore and understand the process in detail.
 
Additional Readings:
* Decision Trees scikit-learn documentation
 

Decision trees are easy to interpret, as you can always traverse backwards and identify the various factors that lead to a particular decision. A decision tree requires you to perform certain tests on attributes in order to split the data into multiple partitions.
 In classification, each data point in a leaf has a class label associated with it.
 You cannot use the linear regression model to make predictions when you need to divide the data set into multiple subsets, as each subset has an independent trend corresponding to it. In such cases, you can use the decision tree model to make predictions because it can split the data into multiple subsets and assign average values as the prediction to each set independently.
