from flask import Flask, render_template
import fdb

app = Flask(__name__)

host = 'localhost'
database = r'C:\Users\Aluno\Desktop\Projeto\BANCO.FDB'
user = 'SYSDBA'
password = 'sysdba'

con = fdb.connect(host=host, database=database, user=user, password=password)

@app.route('/')
def index():
    cursor = con.cursor()
    cursor.execute("select id_livros, autor, titulo, ano_publicacao from livros")
    livros = cursor.fetchall()
    cursor.close()

    return render.template('livros.html', livros=livros)

if __name__ == '__main__':
    app.run(debug=True)

