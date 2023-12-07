# custom_filters.py
class FilterModule(object):
    def filters(self):
        return {
            'extract_dict': self.extract_dict,
            'extract_list': self.extract_list
        }
    
    def extract_list(self, item, key):
        """
        Extracts a list of items corresponding to a given key from each dictionary in a list.
        If the input is a string, it returns the string as is.
        Args:
            list_of_dicts: A list of dictionaries or a string.
            key: The key to extract items for.
        Returns:
            A list of extracted items, or the original string if the input is a string.
        """
        # Proceed with the original logic if the input is a list
        if not isinstance(item, dict):
            raise ValueError("Input must be a dictionary !!!")
        
        if not isinstance(key, str):
            raise ValueError("Key must be a string !!!")

        if item.get(key) is None:
            raise ValueError(f'Your value: "{key}" not found in dictionary !!!')       
        
        extracted_items = []
        list_of_dicts = item.get(key)

        for dic in list_of_dicts:
            org = dic.get('organization')
            if 'organization' not in dic:
                dic['organization'] = org
            extracted_items.append(dic)
        
        return extracted_items

    def extract_dict(self, dic, key):
        """
        Extracts a list of items corresponding to a given key from each dictionary in a list.
        If the input is a string, it returns the string as is.
        Args:
            list_of_dicts: A list of dictionaries or a string.
            key: The key to extract items for.
        Returns:
            A list of extracted items, or the original string if the input is a string.
        """

        # Proceed with the original logic if the input is a list
        if not isinstance(dic, dict):
            raise ValueError("Input must be a dictionary")
        
        if not isinstance(key, str):
            raise ValueError("Key must be a string")        
        
        extracted_items = []
        org = dic.get('organization')

        if key not in dic:
            raise ValueError(f'Your value: "{key}" not found in dictionary')

        if isinstance(dic[key], dict):
            if 'organization' not in dic[key]:
                dic[key]['organization'] = org
            extracted_items.append(dic[key])
        else:
            raise ValueError(f'Your value: "{key}" is not dictionary')
        
        return extracted_items