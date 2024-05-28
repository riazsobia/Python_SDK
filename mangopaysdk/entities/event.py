from mangopaysdk.entities.entitybase import EntityBase


class Event (EntityBase):
    """Event entity."""
    
    def __init__(self, id = None):
        self.RessourceId = ''
        # EventType enum
        self.EventType = None
        # Unix timestamp
        self.Date = None
       
        return super().__init__(id)
    
