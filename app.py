from flask import Flask, render_template 
import pickle

best_df = pickle.load(open('best_df.pkl', 'rb'))

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",
                            book_name = list(best_df['Book-Title'].values),
                            author = list(best_df['Book-Author'].values),
                            image = list(best_df['Image-URL-S'].values),
                            votes = list(best_df['num_ratings'].values),
                            rating = list(best_df['avg_ratings'].values)
                           )

if __name__ == '__main__':
    app.run(debug = True)
        
        