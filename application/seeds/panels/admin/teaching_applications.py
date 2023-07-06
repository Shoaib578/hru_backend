from application import db,app
from application.models.applications import Applications
from application.schemas.application_schema import ApplicationSchema
from application.seeds.utils import save_file,remove_file
from flask import jsonify,request

def GetAllApplications():
    applications_query = Applications.query.all()
    schema = ApplicationSchema(many=True)
    applications= schema.dump(applications_query)

    return jsonify({
        "data":applications
    })

def AcceptorRejectApplication():
    application_id = request.args.get('application_id')
    application = Applications.query.filter_by(application_id=application_id).first()
    db.session.delete(application)
    db.session.commit()
    return jsonify({
        "is_deleted": True
    })


def AddApplication():
    email = request.form.get('email')	
    resume = request.files.get('resume')

    is_saved,filename = save_file(resume,'uploads')

    if is_saved:
        new_application = Applications(resume=filename,email=email)
        db.session.add(new_application)
        db.session.commit()
        return jsonify({
            "status":"Course Has been Added Successfully",
            "is_added":True
        })
    else:
        return jsonify({
             "status":"Could not save resume",
            "is_added":False
        })