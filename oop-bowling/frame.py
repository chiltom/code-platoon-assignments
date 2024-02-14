class Frame:
        
    def __init__(self, num, score, spare=None, strike=None) -> None:
        self._num = num
        self._score = score
        self._spare = False
        self._strike = False
    
    def __str__(self) -> str:
        output = f"Frame {self.get_num}:\n\tScore: {self.get_score}\n\t"
        if self._spare:
            output += f"Spare"
        elif self._strike:
            output += f"Strike"
        return output

    def __repr__(self) -> str:
        return str(self)
    
    @property
    def get_num(self) -> int:
        return self._num
    
    @property
    def get_score(self) -> int:
        return self._score
    
    @property
    def is_spare(self) -> bool:
        return self._spare
    
    @property
    def is_strike(self) -> bool:
        return self._strike
    
    def add_score(self, num) -> None:
        self._score += num
    
    