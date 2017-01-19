import csv
import graphviz
import pprint
import os
from graph_routines import *

INF = 1000000

# Building the graph from the CSV file
print("Getting list of trains from CSV")
all_papers = []
IITM_prof_names = []
number_of_pubs = {}
prof_ids = {}

curr_dir = os.getcwd()
data_dir = curr_dir + '/../Data/'
filename = 'Train_details.csv'

stations = set()

with open(data_dir + filename, newline = '', encoding = 'utf-8') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		stations.add(row['Source Station Name'].strip())
		stations.add(row['Destination Station Name'].strip())

	stations = list(stations)
	stations = dict([(stations[i], i) for i in range(len(stations))])

G = Graph(len(stations))

with open(data_dir + filename, newline = '', encoding = 'utf-8') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		u = stations[row['Source Station Name'].strip()]
		v = stations[row['Destination Station Name'].strip()]
		w = int(row['Distance'].strip())
		G.add_edge(u, v, w)

print("Processed information")
print(G.dijkstra(0))
print('\n\n')
print(G.BFS(0))
