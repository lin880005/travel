from pymongo import MongoClient



def read_db(dic,day="星期一"):
    client = MongoClient('mongodb+srv://patrick:lin880005@travel.pdv2hg5.mongodb.net/') #username,password改成自己的
    db = client.travel
    col = db.all_city
    query = {"行政區":dic,day: 1}
    results = list(col.find(query))
    return results


