from flask import Blueprint
#establecer el blueprint 
dir = Blueprint('dir',__name__)

@dir.route('/getdir',methods=['GET'])
def getdata():
    return {'key':'Directivos'}

