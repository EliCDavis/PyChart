import operator


class Chart:

    def __init__(self, name):

        self._name = name

        self._chart_type = "Line"

        self._data_entries = {}

        self._all_data_sets = []

        self._label_entry_order = {}

    def get_name(self):

        return self._name

    def add_data_entry(self, data, label, data_set="DEFAULT"):

        if label not in self._data_entries.keys():

            self._data_entries[str(label)] = {}

            self._label_entry_order[str(label)] = len(self._label_entry_order)

        self._data_entries[str(label)][str(data_set)] = float(data)

        if data_set not in self._all_data_sets:

            self._all_data_sets.append(data_set)

    def get_data_sets(self):

        return self._all_data_sets

    def get_data_labels(self):

        labels = [None]*len(self._data_entries.keys())

        for label in self._data_entries.keys():

            labels[self._label_entry_order[label]] = label

        return labels

    def get_all_data_from_set(self, data_set):

        data = [None]*len(self._data_entries.keys())

        for x in self._data_entries.keys():

            if self._data_entries[x][data_set] is None:

                data[self._label_entry_order[x]] = 0

            else:

                data[self._label_entry_order[x]] = self._data_entries[x][data_set]

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

        return data

    def sorted_dict(self):

        sort1 = sorted(self._data_entries.items(), key=operator.itemgetter(0))

        return sorted(sort1, key=lambda x: float(x[0]))

    def set_chart_type(self, type_of_chart):

        self._chart_type = type_of_chart

    def get_chart_type(self):

        return self._chart_type

    def can_sort_data_numerically(self):

        for l in self.get_data_labels():

            if self.is_number(l) is False:

                return False

        return True

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False
