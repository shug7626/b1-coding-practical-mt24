class PDController:
    def __init__(self, controller, error = 0):
        self.Kp = controller[0]
        self.Kd = controller[1]
        self.prev_error = error
    
    def calculate_control(self, reference, position):
        error = reference - position
        derivative = (error - self.prev_error)
        control_out = (self.Kp * error) + (self.Kd * derivative)

        self.prev_error = error
        return control_out
