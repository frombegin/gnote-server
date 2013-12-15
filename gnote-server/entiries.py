#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
#!/usr/bin/env python
# -*- coding: utf-8 -*-
 

MALE, FEMALE = (0, 1)

class UserInfo(object):

    def __init__(self):
        super(UserInfo, self).__init__()
        self.name = u""
        self.sex = MALE
        self.email = u""
        self.registered = False

    def __unicode__(self):
        return u"%s <%s>" % (self.__name, self.__email)

# -----------------------------------------------------------------------------

class MemberInfo(object):
    
    def __init__(self):
        super(MemberInfo, self).__init__()
        self.uid = -1
        self.name = u""
        self.isAdmin = False
        
    def __unicode__(self):
        return u"{%s}" % self.__name if self.__isAdmin else self.__name

# -----------------------------------------------------------------------------

class GroupInfo(object):
    
    def __init__(self):
        super(GroupInfo, self).__init__()
        self.name = u""
        self.description = u""
        self.tags = u""
        self.members = []
        self.creatorId = -1
        
    def __unicode__(self):
        return u"%s (%s)" % (self.__name, self.__description)
    
# -----------------------------------------------------------------------------

class Book(object):
    
    def __init__(self):
        super(Book, self).__init__()

# -----------------------------------------------------------------------------

class Note(object):
    
    def __init__(self):
        super(Note, self).__init__()

# -----------------------------------------------------------------------------

class Tag(object):
    
    def __init__(self):
        super(Tag, self).__init__()
        self.tag = u""
        self.popular = 0
        
# -----------------------------------------------------------------------------

class TagCloud(object):
    
    def __init__(self):
        super(TagCloud, self).__init__()
        self.tags = []
        
    def sortByPopular(self):
        pass
    
    def sortByLetter(self):
        pass
    
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    pass