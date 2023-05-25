# INM460_Computer_Vision_Coursework

</br></br>
•	Google Drive folder: 
https://drive.google.com/drive/folders/1907A-h5wYyQN4DaTpmTSRhFW82ofNK_a?usp=sharing
</br></br>

Data
</br>
The dataset contains 12271 training and 3068 test samples of cropped face images (100x100) with labels based on the expressed emotions (7 classes: surprise, fear, disgust, happiness, sadness, anger, neutral).  Initial analysis of the dataset showed class imbalance problem, where the distribution of classes was biased (fig. 1). A Synthetic Minority Oversampling Technique (SMOTE) was applied on the training set alone, where images for the minority classes were randomly duplicated. Even though the returned duplicate images were distorted (the image shape had to be flattened before applying augmentation) this technique showed much better accuracies compared to random oversampling technique. The purpose of applying SMOTE was to combat any possible overfitting in our chosen models by adding in more data. Validation set was created from training set to evaluate model performance and perform hyper-parameter tuning. For Support Vector Machine (SVM) k-fold cross-validation was performed where the training set was split into k smaller sets and model evaluated k consecutive times with different splits each time. For Convolutional Neural Networks (CNN), random train and validation subsets were generated (80/20 ratio) using stratify parameter in order to maintain the class distributions amongst both sets. Final distribution of the dataset: train-26723, validation-6681, test-3068. 
Implemented methods
</br></br>
This project chose three models for critical analysis and evaluation: </br>
1.	SIFT descriptors with SVM classifier 
2.	HOG descriptors with SVM classifier
3.	Convolutional Neural Network 


