import requests, json, time
import streamlit as st

DOMAIN = st.secrets.DOMAIN
TOKEN = st.secrets.TOKEN

def get_result(run_id):
    task_id = get_task_id(run_id)
    while True:
        response = requests.get(
            f'https://{DOMAIN}/api/2.1/jobs/runs/get-output',
            headers={'Authorization': f'Bearer {TOKEN}'},
            params={"run_id": task_id} 
        )
        response_json = json.loads(response.text)  # Parse the response JSON
        
        # Check the life cycle state
        if response_json["metadata"]["state"]["life_cycle_state"] == 'RUNNING':
            time.sleep(5)  # Wait for 5 seconds and retry
        else:
            result = response_json["notebook_output"]["result"] # Return the result if not running
            break
    return result

    
def get_task_id(run_id):
        response = requests.get(
        f'https://{DOMAIN}/api/2.1/jobs/runs/get',
        headers={'Authorization': f'Bearer {TOKEN}'},
        json={
            "run_id": run_id,
        })
        
        if response.status_code == 200:
            print("fetched task_id successfully.")
            response_json = json.loads(response.text)
            task_id = response_json["tasks"][0]["run_id"]
        else:
            print(f"Failed to fetch task_id: {response.status_code}, {response.text}")
        return task_id
        
# get_result(795713180626871)