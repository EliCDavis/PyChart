from ChartConfiguration import ChartConfiguration
import operator


class Chart:

    def __init__(self, name):

        self._name = name

        self._chart_type = ""

        # Initialize the dictionary for storing data
        self._data_entries = {}

        self._configuration = ChartConfiguration('blue')

        self._all_data_sets = []

    def get_name(self):

        return self._name

    def get_data(self):

        return self._data

    def get_labels(self):

        return self._labels

    def add_data_entry(self, data, label):

        self.add_data_entry(data, label, "DEFAULT")

    def add_data_entry(self, data, label, data_set):

        if label not in self._data_entries.keys():

            self._data_entries[str(label)] = {}

        self._data_entries[str(label)][str(data_set)] = float(data)

        if data_set not in self._all_data_sets:

            self._all_data_sets.append(data_set)

    def get_data_sets(self):

        return self._all_data_sets

    def get_data_labels(self):

        labels = []

        for label in self._data_entries.keys():

            labels.append(label)

        return labels

    def get_all_data_from_set(self, data_set):

        data = []

        for x in self._data_entries.keys():

            if self._data_entries[x][data_set] is None:

                data.append(0);

            else:

                data.append(self._data_entries[x][data_set])

        return data

    def get_sorted_labels(self):

        sorted_dict = self.sorted_dict()

        data = []

        for x in sorted_dict:

            data.append(x[0])

        return data

    def sort_data_set_by_label(self, dset):

        """
        Sorts the data set by the label and returns an array of values corresponding to the
        data in that data set
        :param dset:
        :return:
        """

        sorted_dict = self.sorted_dict()

        data = []

        for x in sorted_dict:

            if dset in x[1]:

                data.append(x[1][dset])

            else:

                data.append(0)

        print(data)

        return data

    def sorted_dict(self):

        sort1 = sorted(self._data_entries.items(), key=operator.itemgetter(0))

        return sorted(sort1, key=lambda x: float(x[0]))
