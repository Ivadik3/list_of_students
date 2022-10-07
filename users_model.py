



class User():
    NOT_DEFINED = ""

    def __init__(self,name,gender,password):
        self.ID = User.NOT_DEFINED
        self.Name = name
        self.Gender = gender
        self.class_ = User.NOT_DEFINED
        self.Seat = User.NOT_DEFINED
        self.Club = User.NOT_DEFINED
        self.Persona = User.NOT_DEFINED
        self.Crush = User.NOT_DEFINED
        self.BreastSize = User.NOT_DEFINED
        self.Strength = User.NOT_DEFINED
        self.Hairstyle = User.NOT_DEFINED
        self.Color = User.NOT_DEFINED
        self.Eyes = User.NOT_DEFINED
        self.EyeType = User.NOT_DEFINED
        self.Stockings = User.NOT_DEFINED
        self.Accessory = User.NOT_DEFINED
        self.ScheduleTime = User.NOT_DEFINED
        self.ScheduleDestination = User.NOT_DEFINED
        self.ScheduleAction = User.NOT_DEFINED
        self.Info = User.NOT_DEFINED 
        self.Password = password
        self.Image =User.NOT_DEFINED

    def set_attributes(self,dict1):
        for key,val in dict1.items():
            setattr(self,key,val)

    