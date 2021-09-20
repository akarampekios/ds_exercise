# ds_exercise
# The repo contains, apart from the current README file, a docker composer
# file and two folders. Model folder contains the HALF_PLUS_TWO toy model
# and the scripts folder contains a python file for calling the tf-serving.

# Instructions for the execution of the exercise:
# Clone the repo using git command: git clone <git_url>
git clone https://github.com/akarampekios/ds_exercise.git

# Navigate to the ds_exercise created folder:
cd ds_exercise

# Use docker compose to compose based on the docker-compose.yml file:
docker-compose up -d

# Find the tf-client container and detect it's container id:
docker ps -a | grep tf-client

# Run the following command to execute the python app from the container:
docker exec -it <container_id> python /scripts/request_prediction.py
