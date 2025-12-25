#!/bin/bash

# Configuration
SOURCE_DIR="/opt/sol/data/ubiblio"
BACKUP_DIR="/opt/sol/backups/ubiblio"
TIMESTAMP=$(date +"%Y-%m-%d_%H%M%S")
BACKUP_NAME="ubiblio_backup_$TIMESTAMP.tar.gz"

# Create backup
echo "📦 Starting backup of uBiblio data..."
tar -czf "$BACKUP_DIR/$BACKUP_NAME" -C "$SOURCE_DIR" .

# Keep only the last 7 days of backups to save space
find "$BACKUP_DIR" -type f -mtime +7 -name "*.tar.gz" -delete

echo "✅ Backup complete: $BACKUP_NAME"
