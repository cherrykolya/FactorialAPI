class CustomDict(dict):
    """Расширение класса словаря для хранения текущего максимального ключа в аттрибуте"""

    def __init__(self, *args, **kwargs):
        self.max_key = 0
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise KeyError("Key must be integer value")

        super().__setitem__(key, value)

        if key > self.max_key:
            self.max_key = key
