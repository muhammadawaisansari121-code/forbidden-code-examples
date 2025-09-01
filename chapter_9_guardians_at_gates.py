# compliance_gate.py
import sys
import os

def check_dependencies():
    # Example rule: Ensure vulnerable libraries are not used
    disallowed_libs = ["apache_struts", "insecure_lib"]
    # Get absolute path of requirements.txt in the same folder as script
    req_file = os.path.join(os.path.dirname(__file__), "requirements.txt")
    
    if not os.path.exists(req_file):
        print(f"WARNING: {req_file} not found. Skipping dependency check.")
        return
    
    with open(req_file, "r") as f:
        for line in f:
            for lib in disallowed_libs:
                if lib in line.lower():
                    print(f"ERROR: Disallowed dependency detected -> {lib}")
                    sys.exit(1)

def check_for_sensitive_data():
    # Example rule: Prevent hardcoded credentials
    app_file = os.path.join(os.path.dirname(__file__), "app.py")
    
    if not os.path.exists(app_file):
        print(f"WARNING: {app_file} not found. Skipping sensitive data check.")
        return
    
    with open(app_file, "r") as f:
        for i, line in enumerate(f):
            if "password=" in line.lower():
                print(f"ERROR: Hardcoded credential at line {i+1}")
                sys.exit(1)

if __name__ == "__main__":
    check_dependencies()
    check_for_sensitive_data()
    print("Compliance checks passed. Proceeding to deployment.")
