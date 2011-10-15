import member as _member
import types

__all__ = [
    'AKB48',
    ]

class AKB48(object):
    def __init__(self):
        self.__members = [getattr(_member, name).info() for name in dir(_member) if isinstance(getattr(_member, name), types.ModuleType)]

    def members(self, type=None):
        if type is None:
            return self.__members 
        elif type == 'active':
            return [member for member in self.__members if member['graduate_date'] is None]
        elif type == 'graduate':
            return [member for member in self.__members if member['graduate_date'] is not None]
        else:
            raise ValueError("invalid type: %s" % type)

    def select(self, **kwargs):
        retval = []
        for member in self.__members:
            matches = True
            for k, v in kwargs.iteritems():
                if member[k] != v:
                    matches = False
            if matches:
                retval.append(member)
        return retval
