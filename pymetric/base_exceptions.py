
class PyMetricException(Exception):
  """base class for all PyMetric exceptions.
  """


class LengthNotEqual(PyMetricException): 
  def __init__(self, message='', errors=None):
    self.errors = errors or []
    PyMetricException.__init__(self, message)


class IllegalInput(PyMetricException):
  def __init__(self, message='', errors=None):
    self.errors = errors or []
    PyMetricException.__init__(self, message)

