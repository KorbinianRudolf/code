from numpy import exp, array, random, dot, tanh


class NeuralNetwork:
    def __init__(self):
        random.seed(1)
        self.weight_matrix = 2 * random.random((2, 1)) - 1

    # activation function
    def tanh(self, x):
        return tanh(x)

    def tanh_derivative(self, x):
        return 1.0 - tanh(x) ** 2

    def forward_propagation(self, inputs):
        return self.tanh(dot(inputs, self.weight_matrix))

    def train(self, train_inputs, train_outputs, num_train_iterations):
        for iteration in range(num_train_iterations):
            output = self.forward_propagation(train_inputs)

            error = train_outputs - output

            adjustment = dot(train_inputs.T, error * self.tanh_derivative(output))

            self.weight_matrix += adjustment


# Driver Code
if __name__ == '__main__':
    neural_network = NeuralNetwork()

    print('Random weights at the start of training')
    print(neural_network.weight_matrix)

    train_inputs = array([[0, 0], [0, 1], [1, 0], [1, 1]])
    train_outputs = array([[0, 1, 1, 1]]).T

    neural_network.train(train_inputs, train_outputs, 1000000)

    print('New weights after training')
    print(neural_network.weight_matrix)

    # Test the neural network with a new situation.
    print("Testing network on new examples ->")
    print(neural_network.forward_propagation(array([1, 0])))

