class NormalizingValues(object):
    def __init__(self):
        self.lines = []
        self.max_value = 0

    def normalize_all_actions(self, list_of_files):
        for filename in list_of_files:
            self.find_max_value(filename)
            self.divine_values_on_max()
            self.write_fixed_graph('results/fixed_' + filename.split('/')[1])

    def find_max_value(self, path_to_graph):
        self.lines = []
        with open(path_to_graph) as file:
            lines = file.read().splitlines()
        for line in lines:
            self.lines.append([int(value) for value in line.split('\t')])
            value = self.lines[-1][2]
            if value > self.max_value:
                self.max_value = value

    def divine_values_on_max(self):
        for line in self.lines:
            value = line.pop()
            line.append(round(value / (self.max_value * 1.0), 3))

    def write_fixed_graph(self, path_to_file='fixed_graph.txt'):
        with open(path_to_file, 'w') as file:
            for line in self.lines:
                file.write('\t'.join(map(str, line)))
                file.write('\n')

list_of_files = ['../result_for_click.txt', '../result_for_time.txt']

noramilizer = NormalizingValues()
noramilizer.normalize_all_actions(list_of_files)