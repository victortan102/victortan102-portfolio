from flask import Blueprint, render_template

software_bp = Blueprint("software", __name__, template_folder="software")


@software_bp.route("/asrea-vr-application")
def asrea_vr():
    return render_template("software/asrea-vr-application.html")


@software_bp.route("/bus-router")
def bus_router():
    return render_template("software/bus-router.html")


@software_bp.route("/caregiver-elderly-medicine-app")
def caregiver_app():
    return render_template("software/caregiver-elderly-medicine-app.html")


@software_bp.route("/chinese-idiom-game")
def idiom_game():
    return render_template("software/chinese-idiom-game.html")


@software_bp.route("/clearcare")
def clearcare():
    return render_template("software/clearcare.html")


@software_bp.route("/farm-monitoring-system")
def farm_monitoring():
    return render_template("software/farm-monitoring-system.html")


@software_bp.route("/hdb-resale-flat-analysis")
def hdb_analysis():
    return render_template("software/hdb-resale-flat-analysis.html")


@software_bp.route("/kirbyeats-food-blog")
def kirbyeats():
    return render_template("software/kirbyeats-food-blog.html")


@software_bp.route("/medimate")
def medimate():
    return render_template("software/medimate.html")


@software_bp.route("/mybudgetpal")
def mybudgetpal():
    return render_template("software/mybudgetpal.html")


@software_bp.route("/myems-employee-management-system")
def myems():
    return render_template("software/myems-employee-management-system.html")


@software_bp.route("/npng-fitness")
def npng_fitness():
    return render_template("software/npng-fitness.html")


@software_bp.route("/sme-electronics-store")
def sme_store():
    return render_template("software/sme-electronics-store.html")


@software_bp.route("/temasek-pizzas")
def temasek_pizzas():
    return render_template("software/temasek-pizzas.html")
