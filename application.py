from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)


@app.route("/search_manga", methods=["GET"])
def search_manga():
    title = request.args.get("title")
    with open("data/data.csv", "r") as f:
        for line in f:
            data_arr = line.strip().split(",")
            manga_title = data_arr[0]
            if manga_title == title:
                return jsonify({
                    "title": data_arr[0],
                    "author": data_arr[1],
                    "genre": data_arr[2],
                    "price": data_arr[3],
                    "quantity": data_arr[4]
                })
    return jsonify({"error": "Manga not found"}), 404

@app.route("/search_manga_by_genre", methods=["GET"])
def search_manga_by_genre():
    genre = request.args.get("genre")
    results = []
    with open("data/data.csv", "r") as f:
        for line in f:
            data_arr = line.strip().split(",")
            manga_genre = data_arr[2]
            if manga_genre == genre:
                results.append({"title": data_arr[0], "author": data_arr[1], "genre": data_arr[2], "price": data_arr[3], "quantity": data_arr[4]})
    if results:
        return jsonify(results)
    else:
        return jsonify({"error": "No manga found for the specified genre"}), 404

@app.route("/add_manga", methods=["POST"])
def add_manga():
    data = request.json
    title = data.get("title")
    author = data.get("author")
    genre = data.get("genre")
    price = data.get("price")
    quantity = int(data.get("quantity"))

    updated_lines = []
    manga_found = False

    with open("data/data.csv", "r") as f:
        for line in f:
            data_arr = line.strip().split(",")
            manga_title = data_arr[0]
            if manga_title == title:
                manga_found = True
                data_arr[1] = author
                data_arr[2] = genre
                data_arr[3] = price
                data_arr[4] = str(quantity)
                updated_lines.append(",".join(data_arr))
            else:
                updated_lines.append(line.strip())

    if not manga_found:
        with open("data/data.csv", "a") as f:
            f.write(f"{title},{author},{genre},{price},{quantity}\n")
    else:
        with open("data/data.csv", "w") as f:
            for line in updated_lines:
                f.write(line + "\n")

    return jsonify({"message": "Manga added or updated successfully"}), 201

@app.route('/record_manga_sold', methods=['POST'])
def record_manga_sold():
    data = request.json
    title = data.get('title')
    quantity_sold = int(data.get('quantity'))

    updated_lines = []
    manga_found = False

    with open('data/data.csv', 'r') as f:
        for line in f:
            data_arr = line.strip().split(',')
            manga_title = data_arr[0]
            if manga_title == title:
                manga_found = True
                current_quantity = int(data_arr[4])
                new_quantity = current_quantity - quantity_sold
                data_arr[4] = str(new_quantity)
                updated_lines.append(','.join(data_arr))
            else:
                updated_lines.append(line.strip())

    if not manga_found:
        return jsonify({"error": "Manga not found"}), 404

    with open('data/data.csv', 'w') as f:
        for line in updated_lines:
            f.write(line + '\n')

    return jsonify({"message": "Manga sold record updated successfully"}), 200

@app.route('/')
def serve_main():
    return send_from_directory(directory='.', path='main.html')

if __name__ == '__main__':
    app.run(debug=True)
