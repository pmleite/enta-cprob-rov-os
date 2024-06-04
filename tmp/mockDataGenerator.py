import json
import random
import datetime

def generate_rov_data(start_date, start_time, num_values):
  """
  Generates mock sensor data for an ROV in a JSON format.

  Args:
      start_date: The start date for the data in YYYY-MM-DD format.
      start_time: The start time for the data in HH:MM:SS format.
      num_values: The number of data points to generate.

  Returns:
      A dictionary containing the mock sensor data.
  """

  # Set the base date and time
  base_datetime = datetime.datetime.strptime(f"{start_date} {start_time}", "%Y-%m-%d %H:%M:%S")

  # Sensor data generation functions
  def water_temp():
    # Simulate water temperature between 14 and 18 degrees Celsius at 5m depth in the Azores
    return round(random.uniform(14, 18), 2)

  def ph():
    # Simulate ocean water pH between 7.8 and 8.2
    return round(random.uniform(7.8, 8.2), 2)

  def conductivity():
    # Simulate ocean water conductivity between 30 and 50 mS/cm
    return round(random.uniform(30, 50), 2)

  def sonar1_distance():
    # Simulate sonar distance readings with some variation (0.5 to 5 meters)
    return round(random.uniform(0.5, 5), 2)

  def sonar2_distance():
    # Simulate sonar distance readings with some variation (0.5 to 5 meters)
    return round(random.uniform(0.5, 5), 2)

  def gyro_xyz():
    # Simulate small fluctuations in gyro readings
    return {
      "x": round(random.gauss(0, 0.1), 2),
      "y": round(random.gauss(0, 0.1), 2),
      "z": round(random.gauss(0, 0.1), 2)
    }

  # Generate data points
  data = []
  time_delta = datetime.timedelta(seconds=1)  # Interval between data points

  for i in range(num_values):
    timestamp = base_datetime + time_delta * i
    data_point = {
      "timestamp": timestamp.strftime("%Y-%m-%dT%H:%M:%S"),
      "water_temp": water_temp(),
      "ph": ph(),
      "conductivity": conductivity(),
      "sonar1_distance": sonar1_distance(),
      "sonar2_distance": sonar2_distance(),
      "gyro": gyro_xyz()
    }
    data.append(data_point)

  return data

def main():
  # Get start date, time, and number of values from user
  start_date = input("Enter start date (YYYY-MM-DD): ")
  start_time = input("Enter start time (HH:MM:SS): ")
  num_values = int(input("Enter number of mock values to generate: "))

  # Generate data
  rov_data = generate_rov_data(start_date, start_time, num_values)

  # Write data to JSON file
  with open("rov_data.json", "w") as outfile:
    json.dump(rov_data, outfile, indent=4)

  print(f"Mock ROV data generated and saved to rov_data.json (Total values: {num_values})")

if __name__ == "__main__":
  main()
