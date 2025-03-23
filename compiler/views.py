from django.shortcuts import render
import subprocess
import json
import os
import sys
#import uuid #to generatte unique IDs
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
#temporary storage (using a database for real time projects )
#RESULTS_DB = {}
def index(request):
    return render(request, 'compiler/index.html')

@csrf_exempt  # Disable CSRF protection for simplicity (not recommended in production)
def run_code(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            code = data.get("code", "")

            # Save the Python code to a temporary file
            file_path = "temp_script.py"
            with open(file_path, "w") as f:
                f.write(code)

            # Execute the Python file using subprocess
            result = subprocess.run([sys.executable, file_path], capture_output=True, text=True, timeout=5)
            
            # Remove the temporary file after execution
            if os.path.exists(file_path):
                os.remove(file_path)
            return JsonResponse({"output": result.stdout if result.stdout else result.stderr})
        except Exception as e:
            return JsonResponse({"output": str(e)}, status=500)
    return JsonResponse({"output": "Invalid request"}, status=400)