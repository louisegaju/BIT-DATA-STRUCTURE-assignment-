#project 34:Taxi Trip Summaries
print("Project 34:TAXI TRIP SUMMARIES")
#INTEGER
print("INTEGER-TAXI TRIP ")
trip_distances = [12,8,15,20]
total_distance =sum(trip_distances)
print(f"Total distance: {total_distance}")
average_distances=total_distance/len(trip_distances)
print(f"Average distance: {average_distances}")
min_distances=min(trip_distances)
print(f"Minimum distance: {min_distances}")
max_distances=max(trip_distances)
print(f"Maximum distances: {max_distances}")
#STRINGS
print("STRINGS-TAXI TRIP")
total_distance_report = f"Total distance: {total_distance}"
average_distance_report = f"Average distance: {average_distances}"
print("Summary Reports:")
print(total_distance_report)
print(average_distance_report)
#BOOLEANS
print("BOOLEANS-TAXI TRIP")
threshold=12
if average_distances > threshold and max_distances > 18:
  print("status:Above standard")
else:
  print("status:Below standard")
  #LISTS
print("LISTS-TAXI TRIP")
print("original trip:",trip_distances)
#Add new trip
trip_distances.append(25)
print("update trip:",trip_distances)
#Remove trip
trip_distances.remove(8)
print("update trip:",trip_distances)
#Sort
trip_distances.sort()
print("update trip:",trip_distances)
#ARRAYS
print("ARRAY-TAXI TRIP")
import array
trip_distances_array=array.array('i',[12,8,15,20])
print("trip_distances:",trip_distances_array )
#DICTIONARIES
print("DICTIONARIES_TAXI TRIP")
trip_distances=[{"id":1,"name":"tripA","value":12},
{"id":2,"name":"tripB","value":8},
{"id":3,"name":"tripC","value":15},
{"id":4,"name":"tripD","value":20}]
print("original trip:",trip_distances)
#Update one record
trip_distances[2]["value"]=10
print("update trip:",trip_distances)
#Delet one record
del trip_distances[3]
print("update trip:",trip_distances)
