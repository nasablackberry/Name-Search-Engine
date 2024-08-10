from flask import Flask, request, render_template, redirect, url_for
from dict import name_dict
from search_algo import search_names_with_jaccard

app = Flask(__name__)

def search_query(query, name_dict):
    # Convert the query to lowercase to make the search case-insensitive
    query = query.lower()
    # Find matching names
    results = [name for name in name_dict.keys() if query in name.lower()]
    return results

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    query = None
    if request.method == 'POST':
        query = request.form['query']
        results = search_names_with_jaccard(query, name_dict)
        results = search_query(query, name_dict)
    return render_template('index.html', results=results, query=query)

@app.route('/dictionary', methods=['GET', 'POST'])
def dictionary():
    names=[]
    if request.method == 'POST':
        if 'add_name' in request.form:
            name = request.form['name']
            description = request.form['description']
            if name and description:
                name_dict[name] = description
                names.append(name)
        elif 'delete_name' in request.form:
            name = request.form['name']
            if name in name_dict:
                del name_dict[name]
                if name in names:
                    names.remove(name)
                else:
                    pass
        return redirect(url_for('dictionary'))
    return render_template('dictionary.html', name_dict=name_dict)

if __name__ == '__main__':
    app.run(debug=True)
