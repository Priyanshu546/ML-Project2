# considering 60 as the batch size, 
# creating the X_train and y_train 
for i in range(60, len(train_data)): 
	x_train.append(train_data[i-60:i, 0]) 
	y_train.append(train_data[i, 0]) 

x_train, y_train = np.array(x_train),\ 
				np.array(y_train) 
X_train = np.reshape(x_train, 
					(x_train.shape[0], 
					x_train.shape[1], 1)) 
model = keras.models.Sequential() 
model.add(keras.layers.LSTM(units=64, 
							return_sequences=True, 
							input_shape 
							=(X_train.shape[1], 1))) 
model.add(keras.layers.LSTM(units=64)) 
model.add(keras.layers.Dense(128)) 
model.add(keras.layers.Dropout(0.5)) 
model.add(keras.layers.Dense(1)) 

print(model.summary()) 
from keras.metrics import RootMeanSquaredError 
model.compile(optimizer='adam', 
			loss='mae', 
			metrics=RootMeanSquaredError()) 

history = model.fit(X_train, y_train, 
					epochs=20) 
testing = ss[training - 60:, :] 
x_test = [] 
y_test = dataset[training:, :] 
for i in range(60, len(testing)): 
	x_test.append(testing[i-60:i, 0]) 

x_test = np.array(x_test) 
X_test = np.reshape(x_test, 
					(x_test.shape[0], 
					x_test.shape[1], 1)) 

pred = model.predict(X_test) 
train = microsoft[:training] 
test = microsoft[training:] 
test['Predictions'] = pred 

plt.figure(figsize=(10, 8)) 
plt.plot(train['close'], c="b") 
plt.plot(test[['close', 'Predictions']]) 
plt.title('Microsoft Stock Close Price') 
plt.ylabel("Close") 
plt.legend(['Train', 'Test', 'Predictions']) 
