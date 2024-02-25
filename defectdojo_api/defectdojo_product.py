from datetime import date
from defectdojo_response import DefectDojoResponse
from defectdojo_enums import DefectDojoEngagementStatus, DefectDojoEngagementOrder, DefectDojoEngagementType
from defectdojo_request import DefectDojoRequest

class DefectDojoProduct:

    def __init__(self :object, request :DefectDojoRequest):
        """ Initializes the defectdojoproduct object
        :param request: DefectDojoRequest this Engagement will use for queries
        """
        self._defectdojo_request = request

    def set_metadata(self :object, product_id :int, name :str =None, value :str =None) -> DefectDojoResponse:
        """Add a custom field to a product.

        :param product_id: int, Product ID.
        :param name: (Optional) str, name for the metadata to set
        :param value: (Optional) str, value for the metdata to set

        """
        data = {
            'product': product_id,
            'name': name,
            'value': value
        }
        headers = {
            'product_id': '{}'.format(product_id)
        }

        return self._defectdojo_request.request('POST', 'metadata/', data=data, custom_headers=headers)

    def list(self :object, name :str =None, limit :int =200, offset :int =0) -> DefectDojoResponse:

        """Retrieves all the products.

        :param name: (Optional) str, Search by product name.
        :param limit: (Optional) int, Number of records to return.
        :param offset: (Optional) int, The initial index from which to return the results.

        """

        params  = {}
        if limit:
            params['limit'] = limit

        if offset:
            params['offset'] = offset

        if name:
            params['name'] = name


        return self._defectdojo_request.request('GET', 'products/', params)

    def get(self :object, id :int) -> DefectDojoResponse:
        """Retrieves a product using the given product id.

        :param id: int, Product identification.

        """
        return self._defectdojo_request.request('GET', 'products/' + str(id) + '/')

    def get(self :object, name :str) -> DefectDojoResponse:
        """Retrieves a product list by using the product name 
        :param name: str, the name of the product

        """
        return self._defectdojo_request.request('GET', 'products/?name=' + str(name))


    def create(self :object, name :str, description :str, type :int) -> DefectDojoResponse:
        """Creates a product with the given properties.

        :param name: Product name.
        :param description: Product key id..
        :param type: Product type.

        """

        data = {
            'name': name,
            'description': description,
            'prod_type': type
        }

        return self._defectdojo_request.request('POST', 'products/', data=data)

    def update(self :object, id :int, name :str=None , description :str=None, prod_type :int=None) -> DefectDojoResponse:
        """Updates a product with the given properties.

        :param id: Product ID
        :param name: Product name.
        :param description: Product key id..
        :param prod_type: Product type.

        """

        data = {}

        if name:
            data['name'] = name

        if description:
            data['description'] = description

        if prod_type:
            data['prod_type'] = prod_type

        return self._defectdojo_request.request('PUT', 'products/' + str(id) + '/', data=data)

    def delete(self :object, id :int) -> DefectDojoResponse:
        """
        Deletes a product the given id
        """
        return self._defectdojo_request.request('DELETE', 'products/' + str(id) + '/')