# Step 1: Use an official node image as a parent image
FROM node:18-slim

# Step 2: Set the working directory to /app
WORKDIR /app

# Step 3: Copy package.json and package-lock.json
COPY package*.json ./

# Step 4: Install the dependencies
RUN npm install

# Step 5: Copy the rest of the application code
COPY . .

# Step 6: Build the app
RUN npm run build

# Step 8: Expose port 3000
EXPOSE 3000

# Step 9: Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
