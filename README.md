# GTD Classifier :

Global Terrorism Database is a open source database including information on terrorism events around world from 1970 through 2016. Here I tried to build a classifier which can predict terrorist group responsible for attack.  To download data check the reference link at bottom. 


## Dataset Creation :
To implement this first download dataset from link mentioned in  reference. For this experiment used Weka to get an insight on data. After initial data insight I removed all unnecessary columns from dataset. For this my approach was to start with minimum attirbutes and once I have reasonable accuracy, add more attributes . In this run I have only kept country, Attack type1, Weapon type 1 and  target type 1  as input features along with group name for attack. Once I removed all  column I have filtered source data and extracted target class, replaced with proper indexing number and stored in separate csv file. (Dataset Creation.py)  Total target class for this dataset are 3453.



In this implementation I used Google Colab to get better performance and quick result using hardware provided by google. In code you will find jupyter notebook for below classifiers.

## Backpropagation Run :

First classification model implemented was Backpropagation, using tensorflow. Please check code GTD_Classify.ipynb for this. In the beginning I stared with small network with one hidden layer and less number of nodes, but I was not able to get proper accuracy so I implemented with three hidden layer with 1000,2000,500 nodes respective to each layer. 

<img src="https://github.com/kartik-joshi/GTD-Classifier/blob/master/Images%20/Backpropogation_CompleteData.jpg" width="500">

As you can see in above image network is not getting trained properly. After all exhaustive run and trying different optimizer and activation I couldn't manage to get accuracy more then 50%. On test dataset samples I was getting average 45% accuracy for batch of 1000 records. 


## SVM Run :
In my previous implementation I found that in some cases SVM performs better compare to Backpropagation. So I implemented SVM using SciKit Learn.

<img src="https://github.com/kartik-joshi/GTD-Classifier/blob/master/Images%20/SVM_CompleteData.jpg" width="500">

As you can see in image with SVM with max_iteration 2000 , It managed to get 57% accuracy on test data. 
Then I checked the records distribution compare to each target class. I found that "Unknown" class has more then 79000 records. Which has created inconsistency. 

So I removed all rows with "Unknown" class as target and implemented that dataset on SVM. 

<img src="https://github.com/kartik-joshi/GTD-Classifier/blob/master/Images%20/SVM_FilteredData.jpg " width="500">

With Filtered data I managed to get 59% accuracy with max_iteration = 500.

## Observation and Analysis:
Main observation from the result is that data is not properly distributes among all the classes. There are few target class which has less then 5 records and there are few with more then 1000 records. I believe this is causing trouble for training and creating proper model. In next iteration I will try to balance data for each class by over sampling  record for class which has less data and removing records for a class which has more data. This way I will try to run both the models for balanced dataset.


## Conclusion:
To implement classifier on GTD data we have to process data and remove unnecessary columns. With SVM  you can get up to 60% accuracy. But to get more accuracy you have to perform preprocessing, like over sampling. 


## References:
**[GTD Database](http://www.start.umd.edu/gtd/)
