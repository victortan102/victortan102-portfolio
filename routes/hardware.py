from flask import Blueprint, render_template

hardware_bp = Blueprint("hardware", __name__, template_folder="hardware")


@hardware_bp.route("/homedefender-raspberrypi")
def homedefender():
    return render_template("homedefender-raspberrypi.html")


@hardware_bp.route("/robotic-car")
def robotic_car():
    return render_template("robotic-car.html")


@hardware_bp.route("/smart-aquaponics-system")
def smart_aquaponics():
    return render_template("smart-aquaponics-system.html")


@hardware_bp.route("/smart-water-heater")
def smart_water_heater():
    return render_template("smart-water-heater.html")


@hardware_bp.route("/tinycircuits-language-translation-device")
def translation_device():
    return render_template("tinycircuits-language-translation-device.html")
