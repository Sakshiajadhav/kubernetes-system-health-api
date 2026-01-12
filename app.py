from flask import Flask, jsonify
import psutil

app = Flask(__name__)

CPU_THRESHOLD = 85
MEM_THRESHOLD = 85
DISK_THRESHOLD = 90


def get_system_metrics():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    status = "healthy"
    if cpu > CPU_THRESHOLD or memory > MEM_THRESHOLD or disk > DISK_THRESHOLD:
        status = "unhealthy"

    return {
        "cpu": cpu,
        "memory": memory,
        "disk": disk,
        "status": status
    }


@app.route("/health", methods=["GET"])
def health():
    return jsonify(get_system_metrics())



