from flask import Flask, jsonify
import psutil
import os

app = Flask(__name__)

CPU_THRESHOLD = float(os.getenv('CPU_THRESHOLD', '85'))
MEM_THRESHOLD = float(os.getenv('MEMORY_THRESHOLD', '85'))
DISK_THRESHOLD = float(os.getenv('DISK_THRESHOLD', '90'))


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


@app.route("/metrics", methods=["GET"])
def metrics():
    data = get_system_metrics()
    return jsonify({
        "cpu_percent": data["cpu"],
        "memory_percent": data["memory"],
        "disk_percent": data["disk"],
        "cpu_threshold": CPU_THRESHOLD,
        "memory_threshold": MEM_THRESHOLD,
        "disk_threshold": DISK_THRESHOLD
    })


@app.route("/ready", methods=["GET"])
def ready():
    return jsonify({"ready": True}), 200


@app.route("/live", methods=["GET"])
def live():
    return jsonify({"alive": True}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

























# from flask import Flask, jsonify
# import psutil
# import os 

# app = Flask(__name__)

# CPU_THRESHOLD = float(os.getenv('CPU_THRESHOLD', '85'))
# MEM_THRESHOLD = float(os.getenv('MEMORY_THRESHOLD', '85'))
# DISK_THRESHOLD = float(os.getenv('DISK_THRESHOLD', '90'))


# def get_system_metrics():
#     cpu = psutil.cpu_percent(interval=1)
#     memory = psutil.virtual_memory().percent
#     disk = psutil.disk_usage("/").percent

#     status = "healthy"
#     if cpu > CPU_THRESHOLD or memory > MEM_THRESHOLD or disk > DISK_THRESHOLD:
#         status = "unhealthy"

#     return {
#         "cpu": cpu,
#         "memory": memory,
#         "disk": disk,
#         "status": status
#     }


# @app.route("/health", methods=["GET"])
# def health():
#     return jsonify(get_system_metrics())



