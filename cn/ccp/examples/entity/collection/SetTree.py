class SetTree:
    def __init__(self, key: str, values: list):
        """
            key set to one of these values 'ANY,KNOWN,UNKNOWN,VALUE';With more details, 'ANY' includes 'KNOWN' and
            'UNKNOWN' ,then 'KNOWN' includes 'VALUE','VALUE' includes fid of items('values')
        :param key:
        :param values:
        """
        super().__init__()
        self.key = key  # type:str
        self.values = values  # type:list
