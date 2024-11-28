class Player():

    position = "Bench Warmer"

    def __init__(self, fname, lname, batting, pitching, running, catching, throwing, position):
        self.fname = fname
        self.lname = lname
        self.batting = batting
        self.pitching = pitching
        self.running = running
        self.catching = catching
        self.throwing = throwing
        self.position = position

    def __str__(self):
        return f"Name: {self.fname} {self.lname}\nPosition: {self.position}\nBatting: {self.batting}\nPitching: {self.pitching}\nRunning: {self.running}\nCatching: {self.catching}\nThrowing: {self.throwing}"
    
    def what_is_this(self):
        print("This is object {}".format(self.fname, self.lname))