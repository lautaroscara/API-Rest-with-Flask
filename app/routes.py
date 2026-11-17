from flask import request, jsonify
from app import app, mysql

#List products
@app.route('/products',methods = ['GET'])
def list_products():
    cursor = mysql.connection.cursor() #Create the cursor
    cursor.execute('SELECT * FROM productos') #Execute SQL command with the cursor
    data = cursor.fetchall() #Recover all results and save them
    cursor.close() #Close the cursor to free resources
    return jsonify(data) #Return the data in JSON format

#Find a product
@app.route('/products/<int:codigo>', methods = ['GET'])
def get_product(codigo):
    cursor = mysql.connection.cursor() #Create the cursor
    cursor.execute('SELECT * FROM productos WHERE codigo = %s', (codigo,)) #Execute SQL command with the cursor
    data = cursor.fetchall() #Recover all results and save them
    cursor.close() #Close the cursor to free resources
    if not data:
        return jsonify({'message':'ERROR. Product does not exist'}), 404
    return jsonify(data[0]) #Return the data in JSON format

#Create product
@app.route('/products', methods = ['POST'])
def create_product():
    try:
        codigo = request.json['codigo']
        descrip = request.json['descrip']
        stock = request.json['stock']
        precio = request.json['precio']
        sector = request.json['sector']
        marca = request.json['marca']
        foto = request.json['foto']
    except KeyError as e:
        return jsonify({'message': f'ERROR. Missing field: {e.args[0]}'}), 400
    #Above take all data required on request's body
    
    try:
        codigo = int(codigo)
        stock = int(stock)
        precio = float(precio)
        descrip = str(descrip)
        sector = str(sector)
        marca = str(marca)
        foto = str(foto)
    except(TypeError, ValueError):
        return jsonify({'message':'ERROR. Some resource is incorrect'}), 400
    #Above try to convert those parameters in integers
    
    cursor = mysql.connection.cursor() #Create the cursor

    cursor.execute('SELECT * FROM productos WHERE codigo = %s', (codigo,))#Check if product exist
    data = cursor.fetchall()
    if not data:
        cursor.execute( 'INSERT INTO productos (codigo, descrip, stock, precio, sector, marca, foto) '
                        'VALUES (%s, %s, %s, %s, %s, %s, %s)',
                        (codigo, descrip, stock, precio, sector, marca, foto)) #Execute SQL command with the cursor
        mysql.connection.commit() #Save all changes on DB
        cursor.close() #Close the cursor to free resources
        return jsonify(({'message':'Product created'})),201 #Return a message to notify the creation and a HTTP state 201
    else:
        cursor.close() #Close the cursor to free resources
        return jsonify({'message': 'ERROR. Product already exists'}), 409 #Return a message to notify the existense of another same product

#Update product
@app.route('/products/<int:codigo>', methods = ['PUT'])
def update_product(codigo):
    try:
        descrip = request.json['descrip']
        stock = request.json['stock']
        precio = request.json['precio']
        sector = request.json['sector']
        marca = request.json['marca']
        foto = request.json['foto']
    except KeyError as e:
        return jsonify({'message': f'ERROR. Missing field: {e.args[0]}'}), 400
    #Above, take all data required on request's body
    
    try:
        codigo = int(codigo)
        stock = int(stock)
        precio = float(precio)
        descrip = str(descrip)
        sector = str(sector)
        marca = str(marca)
        foto = str(foto)
    except(TypeError, ValueError):
        return jsonify({'message':'ERROR. Some resource is incorrect'}), 400
    #Above try to convert those parameters in integers
    cursor = mysql.connection.cursor() #Create the cursor
    cursor.execute('SELECT * FROM productos WHERE codigo = %s', (codigo,))#Check if product exist
    data = cursor.fetchall()
    if not data:
        cursor.close()
        return jsonify({'message': 'ERROR. Product does not exist'}), 404
    cursor.execute('UPDATE productos SET descrip = %s, stock = %s, precio = %s, sector = %s, marca = %s, foto = %s WHERE codigo = %s', (descrip, stock, precio, sector, marca, foto, codigo)) #Execute SQL command with the cursor
    mysql.connection.commit() #Save all changes on DB
    cursor.close() #Close the cursor to free resources
    return jsonify({'message':'Product updated'}) #Return a message to notify the update

#Delete a product
@app.route('/products/<int:codigo>', methods = ['DELETE'])
def delete_product(codigo):
    cursor = mysql.connection.cursor() #Create the cursor
    cursor.execute('DELETE FROM productos WHERE codigo = %s', (codigo,)) #Execute SQL command with the cursor
    deleted = cursor.rowcount
    mysql.connection.commit() #Save all changes on DB
    cursor.close() #Close the cursor to free resources
    if deleted == 0:
        return jsonify({'message':'ERROR. Product does not exist'}), 404
    return jsonify({'message':'Product deleted'}) #Return a message to notify the update
