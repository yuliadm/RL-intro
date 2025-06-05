from flask import Flask, render_template, jsonify, request
from tetris_game import TetrisGame

app = Flask(__name__)
game = TetrisGame()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/state')
def get_state():
    return jsonify({
        'board': game.get_board(),
        'score': game.score,
        'game_over': game.game_over
    })

@app.route('/step', methods=['POST'])
def step():
    action = request.json.get('action')
    game.step(action)
    return jsonify({
        'board': game.get_board(),
        'score': game.score,
        'game_over': game.game_over
    })

@app.route('/reset')
def reset():
    game.reset()
    return jsonify({'status': 'reset'})

if __name__ == '__main__':
    app.run(debug=True)



