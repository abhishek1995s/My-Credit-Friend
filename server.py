from flask import Flask,render_template,request,redirect,url_for,flash,jsonify
import requests
from flask import Flask,render_template,request,redirect,url_for,flash,jsonify
from sqlalchemy import create_engine
from  sqlalchemy.orm import sessionmaker
from database import Base,Webdata
from temp import getpin
app=Flask(__name__)
@app.route('/')
@app.route('/hello')
def helloworld():
  return render_template('lang.html')
  #return render_template('insi8_landing.html',scroll='googtrans(en|hi)')
@app.route('/category', methods=['GET', 'POST'])

def userinput():
    if request.method=='GET':
        #menuitem=MenuItem(name= request.form['name'],restaurant_id=restaurant_id)
        #session.add(menuitem)
        #sessiorequest.form['name']n.commit()
        #twitter_trends = get_twitter_trends()
        #for trend in twitter_trends:
           #twitter_search(trend['trend'])
        data= request.args.get("lang") 
        lan_selector='googtrans(en|'+data+')'
        flash("new menu item created")

        return render_template('choice.html',scroll='googtrans(en|hi)')
    #else:
        #return render_template('newmenu.html',restaurant_id=restaurant_id)  
@app.route('/selection', methods=['GET', 'POST'])
def categoryselect():
    if request.method=='GET':
        engine =create_engine('sqlite:///info.db')
        Base.metadata.bind = engine
        DBsession =sessionmaker (bind=engine)
        session=DBsession()
        #menuitem=MenuItem(name= request.form['name'],restaurant_id=restaurant_id)
        #session.add(menuitem)
        #sessiorequest.form['name']n.commit()
        #twitter_trends = get_twitter_trends()
        #for trend in twitter_trends:
           #twitter_search(trend['trend'])
        fetch_data=session.query(Webdata)
        data_list=[]
        count=0;
        selection= request.args.get("selection") 
        #lan_selector='googtrans(en|'+data+')'
        #flash("new menu item created")

        if(selection=="personal"):
            for i in fetch_data:
                y=i.personal
                t=y.split(";")
                data_list.append({'bank': i.bank_name, 'interest' : t[0],'otf' : t[1],'amount' : t[2],'tenure' : t[3]})
                count=count+1

        # if(selection=="personal"):
        #     for i in fetch_data:
        #         data_list.append({'bank': i.bank_name, 'data' : i.personal})
        # if(selection=="personal"):
        #     for i in fetch_data:
        #         data_list.append({'bank': i.bank_name, 'data' : i.personal})
        i=0
        y=[]
        return render_template('banklist.html',data_list=data_list,count=count,i=i,y=y)
@app.route('/pincode', methods=['GET', 'POST'])
def pincodeviewer():
    if request.method=='POST':

        pin= request.form['pincode']
        print(pin)
        bank=request.form['bank']
        address=getpin(pin,bank)
        return render_template('details.html',address=address,bank=bank)    

if __name__=='__main__':
    app.secret_key='super_secret_key'
    app.debug=True
    app.run(host='0.0.0.0',port=5000)
