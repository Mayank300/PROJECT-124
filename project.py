from flask import Flask, jsonify, request
app = Flask(__name__)

contactList = [{ 
    'id': 1,
    'name': 'Mayank',
    'contact': 1111111111,
    'done': False
},
{ 
    'id': 2,
    'name': 'Arthy Mam',
    'contact': 2222222222,
    'done': False
},
{ 
    'id': 3,
    'name': 'WhiteHatJr Mentor',
    'contact': 3333333333,
    'done': False
}]

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/add-data', methods=['POST'])
def addTask():
    if not request.json:
        return jsonify(
            {
                'status': 'error',
                'message': 'data not found!'
            },
            400
        )

    contact = {
        'id': contactList[-1]['id'] + 1,
        'Name': request.json['name'],
        'contact': request.json.get('contact', ""),
        'done': False
    }

    contactList.append(contact)

    return jsonify({
        'message': 'Contact added succesfully!',
        'status': 'success'
    })


@app.route('/get-data')
def getTask():
    return jsonify({
        'data': contactList
    })

if (__name__ == '__main__' ):
    app.run(debug=True)