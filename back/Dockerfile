# Step 1: Use an official Python runtime as a parent image
FROM python:3.12

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the current directory contents into the container at /app
COPY ./back /app/back

# Step 4: Install any needed packages specified in requirements.txt
COPY ./back/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Step 5: Make port 8000 available to the world outside this container
EXPOSE 8000

# Step 6: Run the application
CMD ["uvicorn", "back.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
