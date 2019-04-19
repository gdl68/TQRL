class Item:
    def __init__(self, use_function=None, targeting=False, targeting_message=None, **kwargs):
        self.use_function = use_function
        self.targeting_message = targeting_message
        self.targeting = targeting
        self.function_kwargs = kwargs
