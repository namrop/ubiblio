#!/usr/bin/env python3
import argparse
import sqlite3
import os
from passlib.handlers.sha2_crypt import sha512_crypt as crypto

# Configuration
DB_PATH = '/app/data/ubiblio.db'

def reset_password(username, password):
    if not os.path.exists(DB_PATH):
        print(f"❌ Error: Database not found at {DB_PATH}")
        return

    print(f"🔄 Generating high-entropy hash for '{username}'...")
    new_hash = crypto.hash(password)

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("UPDATE users SET passhash = ? WHERE username = ?", (new_hash, username))

        if cursor.rowcount > 0:
            conn.commit()
            print(f"✅ Success: Password for '{username}' has been reset.")
        else:
            print(f"⚠️  Warning: User '{username}' not found in the database.")

        conn.close()
    except Exception as e:
        print(f"❌ Database error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="uBiblio Password Reset Utility")
    parser.add_argument("-u", "--user", required=True, help="Username to reset")
    parser.add_argument("-p", "--password", required=True, help="New password for the user")
    
    args = parser.parse_args()
    reset_password(args.user, args.password)
