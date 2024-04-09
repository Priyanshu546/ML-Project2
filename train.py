# prepare the training set samples 
msft_close = microsoft.filter(['close']) 
dataset = msft_close.values 
training = int(np.ceil(len(dataset) *. 95))
