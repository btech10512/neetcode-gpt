class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        x = init
        if(iterations == 0):
            return init
        while iterations > 0:
            x = x - learning_rate*2*x
            # print(x_new,end=" ")
            iterations -= 1
            # x = x_new
            
        return round(x,5)
        pass
