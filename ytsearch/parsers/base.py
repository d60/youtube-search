class BaseParser:
    def __init__(self, data, renderer_name, repr_attr) -> None:
        self.data = data[renderer_name]
        self.__repr_attr = repr_attr

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} {self.__repr_attr}="{getattr(self, self.__repr_attr)}">'
