from datetime import date
from defectdojo_response import DefectDojoResponse
from defectdojo_enums import DefectDojoEngagementStatus, DefectDojoEngagementOrder, DefectDojoEngagementType
from defectdojo_request import DefectDojoRequest
from typing import List

class DefectDojoProductType:

    def __init__(self :object, request :DefectDojoRequest) -> None:
        """ Initializes the defectdojoproducttype object
        :param request: DefectDojoRequest this producttype will use for queries
        """

        self._defectdojo_request = request


    def list(self :object, **kwargs :dict) -> DefectDojoResponse:
        """Retrieves all the product types.
           :param kwargs: (Optional) keyword arguments that can be any of the following:
            
            :param id: int, product type id
            :param limit: int, maximum product types to return
            :param offset: int, offset into the returned product types
            :param name: str, name of the product types
            :param critical_product: bool, True or False indicating the product type is a critical product
            :param key_product: bool, True or False indicating the product type is a key product            
            :param updated: date, when the product type was updated
            :param created: date, when the product type was created
            :param prefetch: list[str], list of fields for which to prefetch model instances, can be 'authorization_groups' and/or 'members'
        """

        params  = {}
        
        if kwargs:
            num_args = len(kwargs)
            args_found = 0

            param = kwargs.get('id')
            if param:
                params['id'] = param
                args_found+=1
            
            if args_found < num_args:    
                param = kwargs.get('limit')
                if param:
                    params['limit'] = param
                    args_found+=1

            if args_found < num_args:   
                param = kwargs.get('offset')
                if param:
                    params['offset'] = param
                    args_found+=1

            if args_found < num_args:   
                param = kwargs.get('name')
                if param:
                    params['name'] = param
                    args_found+=1
            
            if args_found < num_args:   
                param = kwargs.get('critical_product')
                if param:
                    params['critical_product'] = param
                    args_found+=1

            if args_found < num_args:   
                param = kwargs.get('key_product')
                if param:
                    params['key_product'] = param
                    args_found+=1

            if args_found < num_args:   
                param = kwargs.get('updated')
                if param:
                    params['updated'] = param.strftime("%Y-%m-%d")
                    args_found+=1

            if args_found < num_args:   
                param = kwargs.get('created')
                if param:
                    params['created'] = param.strftime("%Y-%m-%d")
                    args_found+=1

            if args_found < num_args:   
                param = kwargs.get('prefetch')
                if param:
                    params['prefetch'] = param
                    args_found+=1

        return self._defectdojo_request.request('GET', 'product_types/', params)

    def get(self :object, id :int, prefetch :List[str]=None) -> DefectDojoResponse:
        """Retrieves a product type.
            :param id: int, product type id

            :param prefetch: list[str], list of fields for which to prefetch model instances, can be 'authorization_groups' and/or 'members'
        """
        params = {}
        if prefetch and len(prefetch) > 0:
            params['prefetch'] = prefetch

        return self._defectdojo_request.request('GET', 'product_types/' + str(id), params)
    
    def create(self :object, name :str, description :str, critical_product :bool=False, key_product :bool=False) -> DefectDojoResponse:
        """Creates a product type.
            :param name: str, product type name
            :param description: str, description of the product type
            :param critical_product: bool, True if this is a critical product type
            :param key_product: bool, True if this is a key product type            
        """
        params = {
            'name' : name,
            'description' : description,
            'critical_product' : critical_product,
            'key_product' : key_product
        }

        return self._defectdojo_request.request('POST', 'product_types/', params)
    
    def update(self :object, name :str=None, description :str=None, critical_product :bool=None, key_product :bool=None) -> DefectDojoResponse:
        """Creates a product type.
            :param name: str, product type name
            :param description: str, description of the product type
            :param critical_product: bool, True if this is a critical product type
            :param key_product: bool, True if this is a key product type            
        """
        params = {
            'name' : name,
            'description' : description,
            'critical_product' : critical_product,
            'key_product' : key_product
        }

        return self._defectdojo_request.request('PUT', 'product_types/', params)
    
    def delete(self :object, id :int) -> DefectDojoResponse:
        """ Deletes the product type identified by id
            :param id: int, as unique integer value identifying this product_ type.
        """
        return self._defectdojo_request.request('DELETE', 'product_types/' + str(id))
    
    def preview_delete(self :object, id :int, limit :int=200, offset :int=0) -> DefectDojoResponse:
        """ Preview deletion of the product type identified by id
            :param id: int, as unique integer value identifying this product_ type
            :param limit: int, number of results to return per page
            :param offset: int, initial index from which to return the results
        """

        params = {
            'limit': limit,
            'offset': offset
        }
        return self._defectdojo_request.request('GET', 'product_types/' + str(id) + "/delete_preview", params)
    
    def generate_report(self :object, id :int, include_notes :bool=False, include_images :bool=False, include_exec_summary :bool=False, include_toc :bool=False) -> DefectDojoResponse:
        """ Generate a report for the product type indicated by id
            :param id: int, as unique integer value identifying this product_ type

            :param include_notes: bool (Optional), include finding notes
            :param include_images: bool (Optional), include finding images
            :param include_exe_summary: bool (Optional), include executive summary
            :param include_toc: bool (Optional), include table of contents
        """

        params = {
            'include_finding_notes': include_notes,
            'include_finding_images': include_images,
            'include_executive_summary': include_exec_summary,
            'include_table_of_contents': include_toc
        }

        return self._defectdojo_request.request('POST', f'product_types/{id}/generate_report/', params)