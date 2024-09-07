from flask import request, jsonify
from app import app, mysql

#List products
@app.route('/productos', methods = ['GET'])
def list_products():
    cursor = mysql.connection.cursor() #Create the cursor
    cursor.execute('SELECT * FROM productos') #Execute SQL command with the cursor
    data = cursor.fetchall() #Recover all results and save them
    cursor.close() #Close the cursor to free resourses
    return jsonify(data) #Return the data in JSON format

#Find a product
@app.route('/productos/<int:codigo>', methods = ['GET'])
def get_product(codigo):
    cursor = mysql.connection.cursor() #Create the cursor
    cursor.execute('SELECT * FROM productos WHERE codigo = %s', (codigo,)) #Execute SQL command with the cursor
    data = cursor.fetchall() #Recover all results and save them
    cursor.close() #Close the cursor to free resourses
    return jsonify(data) #Return the data in JSON format

#Creat product
@app.route('/productos', methods = ['POST'])
def create_product():
    codigo = request.json['codigo']
    descrip = request.json['descrip']
    stock = request.json['stock']
    precio = request.json['precio']
    sector = request.json['sector']
    marca = request.json['marca']
    foto = request.json['foto']
    #Above take all data required on request's body
    
    try:
        codigo = int(codigo)
        sotck = int(stock)
        precio = int(precio)
        descrip = str(descrip)
        sector = str(sector)
        marca = str(marca)
        foto = str(foto)
    except(TypeError, ValueError):
        return jsonify({'message':'ERROR. Some resourse is incorrect'})
    #Above try to convert those parametres in integers
    
    cursor = mysql.connection.cursor() #Create the cursor
    cursor.execute("INSERT INTO productos (codigo, descrip, stock, precio, sector, marca, foto) VALUES ({}, '{}', {}, {}, '{}', '{}', '{}')".format( 
                   codigo, descrip, stock, precio, sector, marca, foto)) #Execute SQL command with the cursor
    mysql.connection.commit() #Save all changes on DB
    cursor.close() #Close the cursor to free resourses
    return jsonify(({'Message':'User created'}), 201) #Return a message to notify the creation and a HTTP state 201

#Update product
@app.route('/productos/<int:codigo>', methods = ['PUT'])
def update_product(codigo):
    cursor = mysql.connection.cursor() #Create the cursor
    descrip = request.json['descrip']
    stock = request.json['stock']
    precio = request.json['precio']
    sector = request.json['sector']
    marca = request.json['marca']
    foto = request.json['foto']
    #Above, take all data required on request's body
    
    try:
        codigo = int(codigo)
        sotck = int(stock)
        precio = int(precio)
        descrip = str(descrip)
        sector = str(sector)
        marca = str(marca)
        foto = str(foto)
    except(TypeError, ValueError):
        return jsonify({'message':'ERROR. Some resourse is incorrect'})
    #Above try to convert those parametres in integers
    
    cursor.execute('UPDATE productos SET descrip = %s, stock = %s, precio = %s, sector = %s, marca = %s, foto = %s WHERE codigo = %s', (descrip, stock, precio, sector, marca, foto, codigo)) #Execute SQL command with the cursor
    mysql.connection.commit() #Save all changes on DB
    cursor.close() #Close the cursor to free resourses
    return jsonify({'Message':'User updated'}) #Return a message to notify the update

#Delete a product
@app.route('/productos/<int:codigo>', methods = ['DELETE'])
def delete_product(codigo):
    cursor = mysql.connection.cursor() #Create the cursor
    cursor.execute('DELETE FROM productos WHERE codigo = %s', (codigo,)) #Execute SQL command with the cursor
    mysql.connection.commit() #Save all changes on DB
    cursor.close() #Close the cursor to free resourses
    return jsonify({'Message':'User deleated'}) #Return a message to notify the update
