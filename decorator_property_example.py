class CompanyNameTooLong(Exception):
    pass

class Business:
    """Example class to demonstrate how to use properties

    Using properties you can filter the access to class attribute
    
    Returns:
        Business -- Simple business object
    """
    def __init__(self, cnpj, name):
        self.cnpj = cnpj
        self.company_name = name
    
    @property
    def company_name(self):
        return self.name

    @company_name.setter
    def company_name(self, name):
        if len(name) > 254:
            raise CompanyNameTooLong("Company name should has less than 255 characters")
        self.name = name

    def __repr__(self):
        return f'{self.cnpj}, {self.name}'


if __name__ == "__main__":
    b = Business('9999', 'Test LTDA')

    # Example of protected attribute using a property decorator to limit the attribute length
    b.company_name = 'A' * 255

    print(b.__dict__)