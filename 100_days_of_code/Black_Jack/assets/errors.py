# Store reused exceptions here.


class MethodNotImplemented(NotImplementedError):
    """Handy error class to let you know a method needs to be implemented."""
    METHOD_NOT_IMPLEMENTED = "Method not implemented"
    def __str__(self):
        return self.METHOD_NOT_IMPLEMENTED