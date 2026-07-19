from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = "contacts.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS contacts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


init_db()


# Add Contact
@app.route("/contacts", methods=["POST"])
def add_contact():

    data = request.get_json()

    if not data:
        return jsonify({"error": "Data required"}), 400

    name = data.get("name")
    phone = data.get("phone")

    if not name or not phone:
        return jsonify({"error": "Name and phone are required"}), 400

    try:
        conn = get_db()

        cursor = conn.execute(
            """
            INSERT INTO contacts(name, phone)
            VALUES(?,?)
            """,
            (name, phone)
        )

        conn.commit()

        contact_id = cursor.lastrowid

        conn.close()

        return jsonify({
            "message": "Contact added successfully",
            "contact_id": contact_id
        }), 201

    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500


# View All Contacts
@app.route("/contacts", methods=["GET"])
def get_contacts():

    try:
        conn = get_db()

        contacts = conn.execute(
            "SELECT * FROM contacts"
        ).fetchall()

        conn.close()

        return jsonify([
            dict(contact)
            for contact in contacts
        ])

    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500


# Get Contact By ID
@app.route("/contacts/<int:id>", methods=["GET"])
def get_contact(id):

    try:
        conn = get_db()

        contact = conn.execute(
            "SELECT * FROM contacts WHERE id=?",
            (id,)
        ).fetchone()

        conn.close()

        if contact is None:
            return jsonify({"error": "Contact not found"}), 404

        return jsonify(dict(contact))

    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500


# Delete Contact
@app.route("/contacts/<int:id>", methods=["DELETE"])
def delete_contact(id):

    try:
        conn = get_db()

        contact = conn.execute(
            "SELECT * FROM contacts WHERE id=?",
            (id,)
        ).fetchone()

        if contact is None:
            conn.close()
            return jsonify({"error": "Contact not found"}), 404

        conn.execute(
            "DELETE FROM contacts WHERE id=?",
            (id,)
        )

        conn.commit()
        conn.close()

        return jsonify({
            "message": "Contact deleted successfully"
        })

    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)