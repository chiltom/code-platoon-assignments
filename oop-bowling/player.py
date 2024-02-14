class Player:
    
    def __init__(self, name) -> None:
        self._name = name
        self._score = 0
        self._frames = {}
        
    
    def __str__(self) -> str:
        return f"{self.get_name}:\n\tScore: {self.get_score}\n\tFrames Played: {len(self._frames)}\n"
    
    def __repr__(self) -> str:
        return str(self)
    
    @property
    def get_name(self) -> str:
        return self._name
    
    @property
    def get_score(self) -> int:
        return self._score
    
    @property
    def get_frames(self) -> dict:
        return self._frames
    
    @get_score.setter
    def set_score(self, num) -> None:
        self._score = num
        
    def add_frame(self, frame_inst) -> str:
        self._frames[frame_inst.get_num] = frame_inst
        self._score += frame_inst.get_score
        return frame_inst
    
    