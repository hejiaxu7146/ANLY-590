## Jiaxu He
## ANLY-590
## Final Project Proposal


## 1. Introduction

As the main part of the connection between customers and sellers, reviews have given a lot of information and been used in a lot of ways. However, the classification of the reviews has been a topic for long time, not only because it can show the positive or negative attitude, but also it can determine the mistaken reviews. Meanwhile, the quality of the reviews varies significantly. While poor reviews do not provide accurate information and useful advice, high quality reviews received a lot of agreements overtimes and proved useful information not only for other customers, but also for the sellers to improve or keep working. In that way, getting the quality and fresh review provides important commercial value to business. On the other way, knowing which review are the fresh and quality one helps customers to gain insights into the services and products.


## 2. Team

Jiaxu He,   jh2045@georgetown.edu


## 3. Objectives

* The ultimate goal of this project is to determine the quality and the class from any reviews. 
* While this project will play with data, and try to predict the accuracy rate from it, and find the optimal key from it.


* The expected end result is to get high prediction accuracy model that can determine the class of the review and whether it is useful.


* The unique part of this idea is to build the model not base on one sources, but at least on two resources. (Yelp and Amazon) Also, the two resources are two complete different topics, shopping and food. Other than that, it will compare with the models that build base on each individual resource. I believe since they are all reviews about their thoughts and attitude, it must have something in common as I dig more into the texts. So is for other sources reviews.


## 4. Data

* At least two data sources will be used in this project. Amazon and Yelp. The dataset are from kaggle and google doc that people shared on line.
* https://www.kaggle.com/yelp-dataset/yelp-dataset/version/4
* https://www.kaggle.com/datafiniti/consumer-reviews-of-amazon-products
* https://www.kaggle.com/snap/amazon-fine-food-reviews
* https://drive.google.com/drive/u/0/folders/0Bz8a_Dbh9Qhbfll6bVpmNUtUcFdjYmF2SEpmZUZUcVNiMUw1TWN6RDV3a0JHT3kxLVhVR2M


* The datasets have different format and dimensionalities. Take one dataset as for example:

| review_id   |    user_id      |business_id | stars | date | text | useful| funny | cool |
|----------|:-------------:|:------:|:------:|:------:|:------:|:------:|:------:|------:|
|  vkVSCC7xljjrAI4UGfnKEQ | bv2nCi5Qv5vroFiqKGopiw | AEx2SYEUJmTxVVB18LlCwA |  5 | 2016-05-28 | Super simple place but amazing nonetheless. It...| 0   |   0  |   0 |
|  n6QzIUObkYshz4dz2QRJTw | bv2nCi5Qv5vroFiqKGopiw | VR6GpWIda3SfvPC-lg9H3w |  5 | 2016-05-28 | Small unassuming place that changes their menu...   |   0   |   0   |  0 |
|  MV3CcKScW05u5LVfF6ok0g | bv2nCi5Qv5vroFiqKGopiw | CKC0-MOWMqoeWf6s-szl8g |  5 | 2016-05-28 | Lester's is located in a beautiful neighborhoo...  |   0    |  0  |   0 |
|  IXvOzsEMYtiJI0CARmj77Q | bv2nCi5Qv5vroFiqKGopiw | ACFtxLv8pGrrxMm6EgjreA |  4 | 2016-05-28 | Love coming here. Yes the place always needs t... | 0    |  0  |   0 |
|  L_9BTb55X0GDtThi6GlZ6w | bv2nCi5Qv5vroFiqKGopiw | s2I_Ni76bjJNK9yG60iD-Q |  4 | 2016-05-28 | Had their chocolate almond croissant and it wa... |0   |   0  |   0 |

* The number of the data in each dataset is different, while Yelp has around 5000000, and Amazon has around 20000.


* All the dataset will be cleaned and only keep text, stars, and useful for the further using.


* The possible limitations could be the dataset involve some junk reviews, the reviews that does not make any sense. Also, maybe one data source dataset is way larger than the others. I got around 5261668 reviews from Yelp, while other resources are significantly less than that. 


* The area that could be improved is to get more data from other sources in different topics areas, maybe include movie and weather etc... And also, to clean the data in the same format and keep all sources into similar data amount.


* The current data source is appropriate because it has so many users, and a lot of people rely on them. Yelp is used every day to help people choosing appropriate restaurants. Amazon reviews also helped a lot of people to take insights of the product include myself.


## 5. Assessment Metrics

* The loss function I will use is categorical cross entroy. Because comparing with other metrics, the categorical cross entropy is more fittable for multiclass classfication where each example belongs to a single class.


* The baseline datasets will a part of Amazon reviews and a part of Yelp reviews combines. I will choose the appropriate number to evaluate the model performance since the datasets I got right now is really really huge. 


* The models that I will use as baseline is logistic regression and simple neural network. Since logistic regression has been used in the area for a long time, it is a good method to just compare with the work that neural networks will do. Also, building simple neural network is just to set a baseline for other neural networks performances. In the end, I will also provide matrix to show the prediction results.


* The state of art in this field has a lot of different answers. Middle of this year, A universal language models claims to be the state of art in text classification. It used transfer learning method that can be applied to any task in NLP, and introduce techniques that are key for fine-tuning a language model. their method significantly outperforms the state-of-the-art on six text classification tasks, reducing the error by 18-24% on the majority of datasets. Furthermore, with only 100 labeled examples, it matches the performance of training from scratch on 100x more data. Comparing with that, my method seems to take a starting insight to try to learn in this field. 


## 6. Approach

* The approaches I that I going to start is logistic regression and simple neural network models. That helps me to build a baseline to test and compare my results since they are efficient in most areas regardless the prediction rates. Then, I will try convolutional neural networks since it has been improved increasing classify accuracy rates in a lot of areas. This the main part of the project, to build the CNN for the classification. After that, I will use some pre-trained models available online to compare the results. Then, maybe I will try a pre-trained recurrent neural network, which is another class of artificial neural network that the connections. The limitation that I may face is dataset is too large, and the cost (time and money if running on platform like AWS) seems big. Also, hyperparameter optimization could be a problem. 


* To train my model, I will try train it uses both cloud provider or local computers. The limitation of using cloud provider is too expensive since I got large dataset, and also operation system is hard to use and lack of flexibility. On the other hand, train the model locally could take a really time if it does not have good GPU or CPU.


* The API that I am going to use are Tensorflow and Keras. While keras Supports both convolutional networks and recurrent networks, as well as combinations of the two, also Runs seamlessly on CPU and GPU. And Tensorflow for high performance numerical computation. Its flexible architecture allows easy deployment of computation across a variety of platforms (CPUs, GPUs, TPUs).


* Yes, it is supervised problem. So, the input will be any text that represent a person's review for something. And the output will be the probabilities that belongs to each class ( Stars from 1 to 5), and the probabilities that the review is actually useful or not useful.
