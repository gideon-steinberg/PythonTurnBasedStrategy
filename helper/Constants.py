class Constants:
    
    @staticmethod
    def DEFAULT_BOARD_HEIGHT():
        return 12
    
    @staticmethod
    def DEFAULT_BOARD_WIDTH():
        return 20
    
    @staticmethod
    def DEFAULT_FRAME_WIDTH():
        return Constants.DEFAULT_BOARD_WIDTH() * Constants.DEFAULT_SPRITE_WIDTH()
        
    @staticmethod
    def DEFAULT_FRAME_HEIGHT():
        return Constants.DEFAULT_BOARD_HEIGHT() * Constants.DEFAULT_SPRITE_HEIGHT()
        
    @staticmethod
    def DEFAULT_SPRITE_WIDTH():
        return 50
    
    @staticmethod
    def DEFAULT_SPRITE_HEIGHT():
        return 40