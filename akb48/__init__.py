# encoding: utf-8
"""
This module contains the sole class named :class:`AKB48`.
"""

import member as _member
import types

__all__ = [
    'AKB48',
    ]

class AKB48(object):
    """
    This class handles queries against AKB48's members.

    Synopsys:

    >>> a48 = AKB48()
    >>> a48.members()
    (list of all the AKB48 members)
    >>> a48.members('active')
    (list of all the AKB48 members who are not graduated)
    >>> a48.members('graduate')
    (list of all the AKB48 members who are graduated)
    >>> a48.select(team='A', _class=7)
    (select all of the AKB48 members who belongs to team A and class 7)
    """
    def __init__(self):
        """Constructor"""
        self.__members = [getattr(_member, name).info() for name in dir(_member) if isinstance(getattr(_member, name), types.ModuleType)]

    def members(self, type=None):
        """
        Queries members against the AKB48 member database.

        :param type: which type of members to filter out

            'active'
               return only active members
            'graduate'
               return only graduate members
        """
        if type is None:
            return self.__members 
        elif type == 'active':
            return [member for member in self.__members if member['graduate_date'] is None]
        elif type == 'graduate':
            return [member for member in self.__members if member['graduate_date'] is not None]
        else:
            raise ValueError("invalid type: %s" % type)

    def select(self, **kwargs):
        """
        Queries members against the AKB48 member database in detail.

        Note that this method only takes keyword arguments.

        :param type: filter by member type

            'active'
               return only active members
            'graduate'
               return only graduate members

        :param _class: filter by member class
        :param team: filter by the team where members belong
        :param family_name_en: filter by the romaji representation of the members' family name
        :param first_name_en: filter by the romaji representation of the members' first name
        :param family_name_kana: filter by the hiragana representation of the members' family name
        :param first_name_kana: filter by the hiragana representation of the members' first name
        :param birthday: filter by birthday
        :param graduate_date: filter by graduate date
        :param hometown: filter by the name of the home town
        :param nick: filter by nickname
        """
        retval = []
        type = kwargs.get('type')
        if type is not None:
            del kwargs['type']
        klass = kwargs.get('_class')
        if klass is not None:
            del kwargs['_class']
            kwargs['class'] = klass
        for member in self.__members:
            matches = True
            for k, v in kwargs.iteritems():
                matches = matches and member[k] == v
            if type is not None:
                if type == 'active':
                    matches = matches and member['graduate_date'] is None
                elif type == 'graduate':
                    matches = matches and member['graduate_date'] is not None
            if matches:
                retval.append(member)
        return retval
