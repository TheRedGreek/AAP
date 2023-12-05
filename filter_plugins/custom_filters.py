# custom_filters.py
class FilterModule(object):
    def filters(self):
        return {
            'extract_dict_from_list': self.extract_dict_from_list,
        }

    def extract_dict_from_list(self, list_of_dicts, key):
        """
        Extracts a list of items corresponding to a given key from each dictionary in a list.
        If the input is a string, it returns the string as is.
        Args:
            list_of_dicts: A list of dictionaries or a string.
            key: The key to extract items for.
        Returns:
            A list of extracted items, or the original string if the input is a string.
        """
        # Return the input as is if it's a string
        if isinstance(list_of_dicts, str):
            return list_of_dicts

        # Proceed with the original logic if the input is a list
        if not isinstance(list_of_dicts, list):
            raise ValueError("Input must be a list of dictionaries")

        for dict_item in list_of_dicts:
            if key in dict_item:
                return dict_item[key]
