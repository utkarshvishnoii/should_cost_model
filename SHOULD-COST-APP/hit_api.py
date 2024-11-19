import requests, json
import streamlit as st

DOMAIN = st.secrets.DOMAIN
TOKEN = st.secrets.TOKEN

def trigger_jobs(matnr, vendr,unit_count, estimated_units,country,run_rate_per_hr, raw_material, raw_material_grade, uom_raw_material, rm_quantity, rm_waste_factor, pkg_list,maintenance_cost, facility_size, avg_unit_consume_per_month, man_hours, sga_percentage, margin_percentage):
    response = requests.post(
        f'https://{DOMAIN}/api/2.1/jobs/run-now',
        headers={'Authorization': f'Bearer {TOKEN}'},
        json={
            "job_id": 98298351210535,
            "job_parameters": {
                "matnr": matnr,
                "vendr": vendr,
                "unit_count": unit_count,
                "estimated_units":estimated_units,
                "country": country,
                "run_rate_per_hr": run_rate_per_hr,
                "raw_material": raw_material,
                "raw_material_grade": raw_material_grade,
                "uom_raw_material": uom_raw_material,
                "rm_quantity": rm_quantity,
                "rm_waste_factor": rm_waste_factor,
                "pkg_list": pkg_list,
                "maintenance_cost": maintenance_cost,
                "facility_size": facility_size,
                "avg_unit_consume_per_month": avg_unit_consume_per_month,
                "man_hours": man_hours,
                "sga_percentage": sga_percentage,
                "margin_percentage": margin_percentage
            },
            # "creator_user_name": "utkarsh.vishnoi@effem.com",
            # "run_as_user_name": "utkarsh.vishnoi@effem.com",
            # "run_as_owner": True,
            # "settings": {
            #     "name": "Test Job",
            #     "email_notifications": {
            #         "no_alert_for_skipped_runs": False
            #     },
            #     "webhook_notifications": {},
            #     "timeout_seconds": 0,
            #     "max_concurrent_runs": 1,
            #     "tasks": [
            #         {
            #             "task_key": "Test_job",
            #             "run_if": "ALL_SUCCESS",
            #             "notebook_task": {
            #                 "notebook_path": "/Workspace/Users/utkarsh.vishnoi@effem.com/Should Cost",
            #                 "source": "WORKSPACE"
            #             },
            #             "existing_cluster_id": "1107-104620-l7cpzjdz",
            #             "timeout_seconds": 0,
            #             "email_notifications": {},
            #             "webhook_notifications": {}
            #         }
            #     ],
            #     "format": "MULTI_TASK",
            #     "queue": {
            #         "enabled": True
            #     },
            #     "parameters": [
            #         {"name": "matnr", "default": ""},
            #         {"name": "vendr", "default": ""},
            #         {"name": "unit_count", "default": ""},
            #         {"name": "estimated_units", "default": ""},
            #         {"name": "country", "default": ""},
            #         {"name": "run_rate_per_hr", "default": ""},
            #         {"name": "raw_material", "default": ""},
            #         {"name": "raw_material_grade", "default": ""},
            #         {"name": "uom_raw_material", "default": ""},
            #         {"name": "rm_quantity", "default": ""},
            #         {"name": "rm_waste_factor", "default": ""},
            #         {"name": "pkg_list", "default": ""},
            #         {"name": "maintenance_cost", "default": ""},
            #         {"name": "facility_size", "default": ""},
            #         {"name": "avg_unit_consume_per_month", "default": ""},
            #         {"name": "man_hours", "default": ""},
            #         {"name": "sga_percentage", "default": ""},
            #         {"name": "margin_percentage", "default": ""}
            #     ]
            # },
            # "created_time": 1731497076620
        }
    )
    
    # Check response status
    if response.status_code == 200:
        print("Job triggered successfully.")
        
        response_json = json.loads(response.text)
    else:
        print(f"Failed to trigger job: {response.status_code}, {response.text}")
    
    return response_json["run_id"]
        
        


# Example call to the function
# trigger_jobs(
#     matnr=1461833,
#     vendr='BERRY GLOBAL INC',
#     unit_count=1000,
#     estimated_units=5000000,
#     country='Northern America',
#     run_rate_per_hr = 5376,
#     raw_material='Polypropylene (PP)',
#     raw_material_grade='Copolymer',
#     uom_raw_material="Grams",
#     rm_quantity=23,
#     rm_waste_factor=3,
#     pkg_list='[["Corrugated Box", "Large","2.86"],["Layer Sheets","Small","37.18"],["Pallet","Presswood","0.25"]]',
#     maintenance_cost=20,
#     facility_size=3000,
#     avg_unit_consume_per_month=103500,
#     man_hours=1.3,
#     sga_percentage=6,
#     margin_percentage=10
#     )
    