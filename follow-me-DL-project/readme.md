### Follow Me Project Report
[//]: # (Image References)

[image1]: ./misc_images/FCN_model.jpg
#### FCN Model
The figure below shows the structure of my FCN model.
![alt text][image1]

#####Setup of the FCN model
The model has 5 layers: two encoder layers, one 1x1 convolution layer, and two decoder layers.
Choosing this simple model is mainly because I am not able to collect an image dataset large enough for training classic FCN or CNN models we read from those famous papers. Furthermore, in practice this model gives a decent final score.

##### Hyperparameters
learning_rate = 0.001
batch_size = 30
num_epochs = 50
steps_per_epoch = 200
validation_steps = 50
workers = 4

##### How do I improve model performance.
Initially, I collected extra data and paid special attention to all angles of the target and her close-up images. While the resulted model achieve high score in following the target and recognizing non-target people, it performs poorly in recognizing the target when she is far away. The final score is only 0.32. Then I collected more data and this time I keep drone far away from the target from all angles. The new data significantly improved the model's performance. The final score reached 0.42.
