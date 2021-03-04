from tensorflow import keras

model = keras.Sequential([keras.layers.Dense(units = 1, input_shape=[1])])

model.compile(optimizer='sgd', loss='mean_squared_error')

xs = [1, 2, 3]
ys = [2, 4, 6]

model.fit(xs, ys, epochs=1000)

print(model.predict([7]))