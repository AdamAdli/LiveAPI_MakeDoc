# http://remotescripts.blogspot.com

from . import LiveAPI_MakeDoc

def create_instance(c_instance):
    """ Creates and returns the script """
    return LiveAPI_MakeDoc.MakeDocSurface(c_instance)