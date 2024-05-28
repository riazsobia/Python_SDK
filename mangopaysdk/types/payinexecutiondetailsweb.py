from mangopaysdk.types.payinexecutiondetails import PayInExecutionDetails


class PayInExecutionDetailsWeb (PayInExecutionDetails):
    """ Class represents Web type for execution option in PayIn entity."""

    def __init__(self):
        # URL format expected
        self.RedirectURL = None
        self.ReturnURL = None
        self.TemplateURL = None

        self.Culture = ''
        # Mode3DSType { DEFAULT, FORCE }
        self.SecureMode = None

    def GetReadOnlyProperties(self):
        properties = super().GetReadOnlyProperties()
        properties.append('RedirectURL' )        
        return properties