import os
from flask import Blueprint, render_template, request, redirect, url_for
import mysql.connector

main_bp = Blueprint('main', __name__)

def conectar():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        port=int(os.getenv('DB_PORT', 3306))
    )
    
@main_bp.route('/')
def codigo():
    return render_template('index.html')


@main_bp.route('/acessar-ou-criar', methods=['POST'])
def acessar_ou_criar():
    central = request.form.get('cd_central', '').strip().upper()
    
    if not central:
        return redirect(url_for('main.codigo'))
    
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM centrais WHERE cd_central = %s", (central,))
    existe = cursor.fetchone()
    
    if not existe:
        cursor.execute("INSERT INTO centrais (cd_central) VALUES (%s)", (central,))
        conn.commit()
    
        id_central = cursor.lastrowid

        cursor.execute(
            "INSERT INTO notas (id_central, titulo, texto) VALUES (%s, %s, %s)",
            (id_central, 'Bem-vindo!', 'Esta é sua primeira nota.')
        )
        conn.commit()
            
    cursor.close()
    conn.close()
    
    return redirect(url_for('main.central', central=central))


@main_bp.route('/<central>')
def central(central):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM centrais WHERE cd_central = %s", (central,))
    dados_central = cursor.fetchone()
    
    if not dados_central:
        cursor.close()
        conn.close()
        return redirect(url_for('main.codigo'))
        
    cursor.execute("SELECT * FROM notas WHERE id_central = %s ORDER BY data_criacao DESC", (dados_central['id'],))
    notas = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return render_template('central.html', cd=central, central_info=dados_central, notas=notas)

@main_bp.route('/<central>/nota/cadastrar', methods=['POST'])
def cadastrar_nota(central):
    titulo = request.form.get('titulo')
    texto = request.form.get('texto')
        
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT id FROM centrais WHERE cd_central = %s", (central,))
    dados_central = cursor.fetchone()
    
    if dados_central:
        query = "INSERT INTO notas (id_central, titulo, texto) VALUES (%s, %s, %s)"
        cursor.execute(query, (dados_central['id'], titulo, texto))
        conn.commit()
        
        id_nova_nota = cursor.lastrowid
        
        cursor.close()
        conn.close()
        
        return redirect(url_for('main.central', central=central, nota=id_nova_nota))
            
    cursor.close()
    conn.close()
    return redirect(url_for('main.central', central=central))

@main_bp.route('/<central>/<int:nota>')
def nota(central, nota):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM notas WHERE id = %s", (nota,))
    dados_nota = cursor.fetchone()
    
    cursor.close()
    conn.close()
        
    return render_template('nota.html', cd=central, nota=dados_nota)

@main_bp.route('/<central>/nota/atualizar/<int:id_nota>', methods=['POST'])
def atualizar_nota(central, id_nota):
    titulo = request.form.get('titulo')
    texto = request.form.get('texto')
        
    conn = conectar()
    cursor = conn.cursor()
    
    query = "UPDATE notas SET titulo = %s, texto = %s WHERE id = %s"
    cursor.execute(query, (titulo, texto, id_nota))
    conn.commit()
        
    cursor.close()
    conn.close()
        
    return redirect(url_for('main.central', central=central, nota=id_nota))

@main_bp.route('/<central>/nota/nova')
def nova_nota(central):
    return render_template('nota.html', cd=central, nota=None)

@main_bp.route('/central/deletar/<int:id>')
def deletar_central(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM centrais WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('main.codigo'))

@main_bp.route('/<central>/nota/deletar/<int:id_nota>')
def deletar_nota(central, id_nota):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notas WHERE id = %s", (id_nota,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('main.central', central=central))